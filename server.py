from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import zipfile
import io
import json
import tempfile
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
# Enable CORS for all routes
CORS(app, resources={r"/webhook": {"origins": "*"}})

# Configuration
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """
    Handle incoming POST requests from n8n with zip files or JSON data
    """
    try:
        logger.info(f"Received webhook request with content type: {request.content_type}")
        logger.info(f"Request headers: {dict(request.headers)}")
        
        # Check if the request contains files
        if 'file' in request.files:
            file = request.files['file']
            logger.info(f"Received file: {file.filename}")
            
            if file.filename.endswith('.zip'):
                # Save the zip file
                filepath = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(filepath)
                logger.info(f"Saved zip file to: {filepath}")
                
                # Process the zip file if needed
                process_zip_file(filepath)
                
                return jsonify({
                    'status': 'success',
                    'message': 'Zip file received and processed successfully',
                    'filename': file.filename
                }), 200
            else:
                return jsonify({
                    'status': 'error',
                    'message': 'Only zip files are accepted'
                }), 400
        elif request.content_type and request.content_type.startswith('application/zip'):
            # Handle raw zip file in request body
            logger.info("Received raw zip file in request body")
            
            # Save the zip file from request data
            filename = request.headers.get('Content-Disposition', 'file.zip')
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            
            with open(filepath, 'wb') as f:
                f.write(request.get_data())
            
            logger.info(f"Saved raw zip file to: {filepath}")
            
            # Process the zip file if needed
            process_zip_file(filepath)
            
            return jsonify({
                'status': 'success',
                'message': 'Raw zip file received and processed successfully',
                'filename': filename
            }), 200
        elif request.content_type == 'application/json':
            # Handle JSON data
            data = request.get_json()
            logger.info(f"Received JSON data: {data}")
            
            email = data.get('email')
            playlistUrl = data.get('playlistUrl')
            
            if not email or not playlistUrl:
                return jsonify({
                    'status': 'error',
                    'message': 'Missing required fields: email and playlistUrl'
                }), 400
            
            # Process the data and create notes
            notes = create_notes(playlistUrl, email)
            
            # Create a zip file with the notes
            zip_filename = f"notes_{email.split('@')[0]}.zip"
            zip_filepath = os.path.join(UPLOAD_FOLDER, zip_filename)
            
            # Create zip file with notes
            create_notes_zip(notes, zip_filepath)
            
            # Return success response with zip file information
            logger.info(f"Zip file created: {zip_filepath}")
            return jsonify({
                'status': 'success',
                'message': 'Notes created successfully',
                'zip_filename': zip_filename,
                'download_url': f'/download-zip'
            }), 200
        
        return jsonify({
            'status': 'error',
            'message': 'No file or invalid content type received'
        }), 400
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}", exc_info=True)
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/webhook-test', methods=['POST'])
def handle_test_webhook():
    """
    Handle test webhook requests
    """
    try:
        logger.info("Received test webhook request")
        logger.info(f"Request data: {request.get_data()}")
        logger.info(f"Request JSON: {request.get_json()}")
        
        # For testing, just return a success message
        return jsonify({
            'status': 'success',
            'message': 'Webhook test successful',
            'data': request.get_json() if request.is_json else None
        }), 200
    except Exception as e:
        logger.error(f"Error processing test webhook: {str(e)}", exc_info=True)
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

def process_zip_file(filepath):
    """
    Process the received zip file
    """
    logger.info(f"Processing zip file: {filepath}")
    
    try:
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            # List files in the zip
            file_list = zip_ref.namelist()
            logger.info(f"Files in zip: {file_list}")
            
            # Extract and process files if needed
            zip_ref.extractall(UPLOAD_FOLDER)
            
        logger.info(f"Successfully processed zip file: {filepath}")
    except Exception as e:
        logger.error(f"Error processing zip file {filepath}: {str(e)}", exc_info=True)
        raise

def create_notes(playlist_url, email):
    """
    Create notes based on playlist URL and user email
    This is a placeholder implementation
    """
    logger.info(f"Creating notes for playlist: {playlist_url} and email: {email}")
    
    # In a real implementation, you would:
    # 1. Parse the playlist URL
    # 2. Fetch playlist information
    # 3. Create notes content
    # 4. Return structured notes data
    
    notes = {
        "playlist_url": playlist_url,
        "email": email,
        "notes": [
            {
                "title": "Video 1 Notes",
                "content": "Notes for the first video in the playlist"
            },
            {
                "title": "Video 2 Notes",
                "content": "Notes for the second video in the playlist"
            }
        ]
    }
    return notes

def create_notes_zip(notes, zip_filepath):
    """
    Create a zip file containing notes as text files
    """
    logger.info(f"Creating notes zip file: {zip_filepath}")
    
    try:
        with zipfile.ZipFile(zip_filepath, 'w') as zip_file:
            for i, note in enumerate(notes['notes']):
                # Create a text file for each note
                filename = f"{note['title'].replace(' ', '_')}.txt"
                content = f"# {note['title']}\n\n{note['content']}\n"
                zip_file.writestr(filename, content)
        
        logger.info(f"Successfully created notes zip file: {zip_filepath}")
    except Exception as e:
        logger.error(f"Error creating notes zip file {zip_filepath}: {str(e)}", exc_info=True)
        raise
@app.route('/download-zip', methods=['POST'])
def download_zip():
    """
    Handle POST requests to download zip files
    """
    try:
        # Get the filename from the request
        data = request.get_json()
        zip_filename = data.get('filename')
        
        if not zip_filename:
            return jsonify({
                'status': 'error',
                'message': 'Missing filename in request'
            }), 400
        
        # Check if file exists
        zip_filepath = os.path.join(UPLOAD_FOLDER, zip_filename)
        if not os.path.exists(zip_filepath):
            return jsonify({
                'status': 'error',
                'message': 'File not found'
            }), 404
        
        # Return the zip file
        logger.info(f"Sending zip file: {zip_filepath}")
        return send_file(zip_filepath, as_attachment=True, download_name=zip_filename)
    except Exception as e:
        logger.error(f"Error downloading zip file: {str(e)}", exc_info=True)
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

if __name__ == '__main__':
    logger.info("Starting Flask server on http://localhost:6000")
    app.run(host='localhost', port=6000, debug=True)
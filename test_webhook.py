import requests
import json

# Test data
test_data = {
    "email": "test@example.com",
    "playlistUrl": "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab",
    "timestamp": "2025-08-27T10:00:00Z",
    "userAgent": "Test Script"
}

# Send POST request to the webhook
url = "http://localhost:5678/webhook-test/e0727839-8b03-4b9b-bbcc-fdee2e52992f"
headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(test_data))
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    # If response is a zip file, save it
    if response.headers.get('Content-Type') == 'application/zip':
        with open('test_notes.zip', 'wb') as f:
            f.write(response.content)
        print("Zip file saved as test_notes.zip")
except Exception as e:
    print(f"Error: {e}")
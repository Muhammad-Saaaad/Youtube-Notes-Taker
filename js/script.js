// Get DOM elements
const playlistForm = document.getElementById('playlistForm');
const emailInput = document.getElementById('email');
const playlistUrlInput = document.getElementById('playlistUrl');
const emailError = document.getElementById('email-error');
const urlError = document.getElementById('url-error');
const resultSection = document.getElementById('result');
const resultContent = document.getElementById('result-content');
// const resetBtn = document.getElementById('reset-btn'); // Removed as we are using a button in the result section

// Email validation function
function validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// YouTube URL validation function
function validateYouTubeUrl(url) {
    const youtubeRegex = /^(https?:\/\/)?(www\.)?(youtube\.com\/(playlist\?list=|watch\?v=|embed\/)|youtu\.be\/)/;
    return youtubeRegex.test(url);
}

// Show error message for email
function showEmailError(message) {
    emailError.textContent = message;
    emailInput.classList.add('invalid');
    emailInput.classList.remove('valid');
}

// Show success for email
function showEmailSuccess() {
    emailError.textContent = '';
    emailInput.classList.remove('invalid');
    emailInput.classList.add('valid');
}

// Show error message for URL
function showUrlError(message) {
    urlError.textContent = message;
    playlistUrlInput.classList.add('invalid');
    playlistUrlInput.classList.remove('valid');
}

// Show success for URL
function showUrlSuccess() {
    urlError.textContent = '';
    playlistUrlInput.classList.remove('invalid');
    playlistUrlInput.classList.add('valid');
}

// Reset validation styles
function resetValidation() {
    emailInput.classList.remove('valid', 'invalid');
    playlistUrlInput.classList.remove('valid', 'invalid');
    emailError.textContent = '';
    urlError.textContent = '';
}

// Show result section
function showResult(message, isSuccess = true) {
    resultContent.innerHTML = message;
    resultSection.classList.remove('hidden', 'success', 'error');
    resultSection.classList.add(isSuccess ? 'success' : 'error');
}

// Reload the page to reset everything
function resetPage() {
    window.location.reload();
}

/**
 * Async function to send data to the webhook and handle response/errors.
 * @param {string} email - The user's email.
 * @param {string} playlistUrl - The YouTube playlist URL.
 */
async function sendToWebhook(email, playlistUrl) {
    const data = {
        email: email,
        playlistUrl: playlistUrl,
        timestamp: new Date().toISOString(),
        userAgent: navigator.userAgent
    };
    
    // Corrected webhook URL from your request
    const webhookUrl = 'http://localhost:5678/webhook-test/e0727839-8b03-4b9b-bbcc-fdee2e52992f'; 

    console.log('Sending data to webhook:', data);
    
    // Display a processing message while waiting for the request
    showResult(`
        <div class="processing-animation">
            <div class="spinner"></div>
            <p>Processing your request...</p>
        </div>
    `, true);

    try {
        const response = await fetch(webhookUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`Webhook response was not ok. Status: ${response.status}`);
        }

        // Display the success message after the fetch call is successful
        const successMessage = `
            <p>Your request has been sent successfully!</p>
            <p>You will receive your notes in a zip file via <strong>${email}</strong> shortly.</p>
            <button id="processAnotherBtn" class="submit-btn" style="margin-top: 1rem;">Process another playlist</button>
        `;
        showResult(successMessage, true);
        
    } catch (error) {
        // Display an error message if the webhook fails to respond
        console.error('Webhook request failed:', error);
        const errorMessage = `
            <p>Oops! Something went wrong. We couldn't connect to the server.</p>
            <p>Please try again in a moment.</p>
            <button id="processAnotherBtn" class="submit-btn" style="margin-top: 1rem;">Process another playlist</button>
        `;
        showResult(errorMessage, false);
    } finally {
        // Add event listener to the "Process another playlist" button
        const processAnotherBtn = document.getElementById('processAnotherBtn');
        if (processAnotherBtn) {
            processAnotherBtn.addEventListener('click', resetPage);
        }
    }
}

// Form submission handler
playlistForm.addEventListener('submit', function(e) {
    e.preventDefault();
    console.log('Form submitted');
    
    // Reset previous validation states
    resetValidation();
    
    // Get form values
    const email = emailInput.value.trim();
    const playlistUrl = playlistUrlInput.value.trim();
    
    // Validate inputs
    let isValid = true;
    
    if (!email) {
        showEmailError('Email is required');
        isValid = false;
    } else if (!validateEmail(email)) {
        showEmailError('Please enter a valid email address');
        isValid = false;
    } else {
        showEmailSuccess();
    }
    
    if (!playlistUrl) {
        showUrlError('YouTube playlist URL is required');
        isValid = false;
    } else if (!validateYouTubeUrl(playlistUrl)) {
        showUrlError('Please enter a valid YouTube playlist URL');
        isValid = false;
    } else {
        showUrlSuccess();
    }
    
    console.log('Form is valid:', isValid);
    
    // If form is valid, process it
    if (isValid) {
        console.log('Processing playlist');
        // Call the async function to send data
        sendToWebhook(email, playlistUrl);
    }
});

// Real-time validation for email
emailInput.addEventListener('blur', function() {
    if (this.value.trim() === '') {
        showEmailError('Email is required');
    } else if (!validateEmail(this.value.trim())) {
        showEmailError('Please enter a valid email address');
    } else {
        showEmailSuccess();
    }
});

// Real-time validation for URL
playlistUrlInput.addEventListener('blur', function() {
    if (this.value.trim() === '') {
        showUrlError('YouTube playlist URL is required');
    } else if (!validateYouTubeUrl(this.value.trim())) {
        showUrlError('Please enter a valid YouTube playlist URL');
    } else {
        showUrlSuccess();
    }
});

// Clear error when user starts typing
emailInput.addEventListener('input', function() {
    if (this.classList.contains('invalid')) {
        emailError.textContent = '';
        this.classList.remove('invalid');
    }
});

playlistUrlInput.addEventListener('input', function() {
    if (this.classList.contains('invalid')) {
        urlError.textContent = '';
        this.classList.remove('invalid');
    }
});

// Add CSS for spinner animation
const style = document.createElement('style');
style.textContent = `
    .processing-animation {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 1rem 0;
    }
    
    .spinner {
        width: 40px;
        height: 40px;
        border: 4px solid rgba(30, 136, 229, 0.3);
        border-top: 4px solid var(--vibrant-purple);
        border-radius: 50%;
        animation: spin 1s linear infinite;
        margin-bottom: 1rem;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
`;
document.head.appendChild(style);
# Technical Specification: YouTube Playlist NoteTaker

## 1. HTML Structure

### Main Components
- Header with title
- Form section with:
  - Email input field
  - YouTube playlist URL input field
  - Submit button
- Results display area (initially hidden)
- Footer with additional information

### Form Validation Requirements
- Email must be in valid format
- YouTube URL must be from youtube.com or youtu.be domain
- Both fields are required

## 2. CSS Design System

### Color Palette
```css
:root {
  --primary-blue: #1E88E5;
  --dark-blue: #0D47A1;
  --light-blue: #E3F2FD;
  --accent-blue: #64B5F6;
  --text-dark: #333333;
  --text-light: #FFFFFF;
  --success: #4CAF50;
  --error: #F44336;
}
```

### Typography
- Primary font: 'Roboto', sans-serif
- Font sizes:
  - Header: 2rem
  - Subheader: 1.5rem
  - Body: 1rem
  - Small text: 0.875rem

### Layout
- Mobile-first responsive design
- Max width: 1200px
- Padding: 1rem on mobile, 2rem on desktop
- Centered content

## 3. JavaScript Functionality

### Event Handlers
- Form submission
- Input validation on blur
- Real-time feedback

### Functions
```javascript
function validateEmail(email)
function validateYouTubeUrl(url)
function handleSubmit(event)
function showSuccess(message)
function showError(message)
function resetForm()
```

### User Interactions
- Form validation with visual feedback
- Loading state during processing
- Success/error messages
- Form reset after submission

## 4. Accessibility Features
- Proper form labels
- ARIA attributes
- Keyboard navigation
- Sufficient color contrast (WCAG AA compliant)
- Focus indicators

## 5. Responsive Design Breakpoints
- Small: < 768px (mobile)
- Medium: 768px - 1024px (tablet)
- Large: > 1024px (desktop)

## 6. Error Handling
- Invalid email format
- Invalid YouTube URL
- Network errors (if API integration)
- Empty field submissions
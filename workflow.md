# User Workflow: YouTube Playlist NoteTaker

## Interaction Flow

```mermaid
graph TD
    A[User visits webpage] --> B[View form with email and YouTube URL fields]
    B --> C[User fills in email address]
    C --> D[User fills in YouTube playlist URL]
    D --> E[User clicks Submit button]
    E --> F{Form validation}
    F -->|Valid| G[Process form data]
    F -->|Invalid| H[Show error messages]
    H --> I[User corrects errors]
    I --> E
    G --> J[Show success message]
    J --> K[Optionally reset form or show results]
```

## Form Validation Logic

```mermaid
graph TD
    A[Form Submission] --> B[Check if email is empty]
    B -->|Empty| C[Show email required error]
    B -->|Not empty| D[Validate email format]
    D -->|Invalid| E[Show email format error]
    D -->|Valid| F[Check if YouTube URL is empty]
    F -->|Empty| G[Show URL required error]
    F -->|Not empty| H[Validate YouTube URL format]
    H -->|Invalid| I[Show URL format error]
    H -->|Valid| J[Form is valid - proceed]
```

## Visual Feedback States

```mermaid
graph TD
    A[Input Field States] --> B[Default - Light blue background]
    B --> C[Focus - Blue border with shadow]
    C --> D{Validation}
    D -->|Valid| E[Green border - Success]
    D -->|Invalid| F[Red border - Error with message]
```

## Button Interaction States

```mermaid
graph TD
    A[Submit Button] --> B[Default - Primary blue]
    B --> C[Hover - Darker blue]
    C --> D[Click - Pressed effect]
    D --> E{Form Status}
    E -->|Processing| F[Disabled - Loading spinner]
    E -->|Success| G[Success state - Green]
    E -->|Error| H[Error state - Red]
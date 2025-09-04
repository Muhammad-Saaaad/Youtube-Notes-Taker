# Design Mockup: YouTube Playlist NoteTaker

## Color Scheme Visualization

```
┌─────────────────────────────────────────────────────────────┐
│  Primary Blue: #1E88E5    Dark Blue: #0D47A1               │
│  ████ Light Blue: #E3F2FD  Accent Blue: #64B5F6            │
│                                                             │
│  Text Dark: #333333       Text Light: #FFFFFF              │
│  ████ Success: #4CAF50    Error: #F44336                   │
└─────────────────────────────────────────────────────────────┘
```

## Layout Structure

```
┌─────────────────────────────────────────────────────────────┐
│                    HEADER SECTION                           │
│  ┌─────────────────────────────────────────────────────────┐│
│  │              YouTube NoteTaker                          ││
│  │              (Centered, large font)                     ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│                    FORM SECTION                             │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  Email Address                                          ││
│  │  [─────────────────────────────────────────────────]    ││
│  │                                                         ││
│  │  YouTube Playlist URL                                   ││
│  │  [─────────────────────────────────────────────────]    ││
│  │                                                         ││
│  │  [ SUBMIT BUTTON ]                                      ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│                   FEEDBACK SECTION                          │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  Success/Error messages appear here                     ││
│  └─────────────────────────────────────────────────────────┘│
│                                                             │
│                    FOOTER SECTION                           │
│  ┌─────────────────────────────────────────────────────────┐│
│  │  © 2025 YouTube NoteTaker - All rights reserved         ││
│  └─────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────┘
```

## Interactive States

### Form Input States
1. **Default State**: Light blue background with dark text
2. **Focus State**: Blue border with shadow effect
3. **Valid State**: Green border indicator
4. **Invalid State**: Red border with error message

### Button States
1. **Default**: Primary blue background
2. **Hover**: Darker blue background
3. **Active**: Pressed effect with shadow
4. **Disabled**: Light gray background

## Responsive Breakpoints

### Mobile View (320px - 767px)
```
┌─────────────────────────────┐
│  YouTube NoteTaker          │
│                             │
│  Email Address              │
│  [─────────────────────]    │
│                             │
│  YouTube Playlist URL       │
│  [─────────────────────]    │
│                             │
│  [ SUBMIT ]                 │
└─────────────────────────────┘
```

### Tablet View (768px - 1023px)
```
┌─────────────────────────────────────────────────┐
│        YouTube NoteTaker                        │
│                                                 │
│  Email Address        YouTube Playlist URL      │
│  [───────────────]    [─────────────────────]   │
│                                                 │
│              [ SUBMIT BUTTON ]                  │
└─────────────────────────────────────────────────┘
```

### Desktop View (1024px+)
```
┌─────────────────────────────────────────────────────────────┐
│                      YouTube NoteTaker                      │
│                                                             │
│  Email Address              YouTube Playlist URL            │
│  [───────────────────]      [───────────────────────────]   │
│                                                             │
│                        [ SUBMIT BUTTON ]                    │
└─────────────────────────────────────────────────────────────┘
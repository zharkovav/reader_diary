# Static Files Specification

## CSS Structure (static/css/)

### Main Stylesheet (style.css)
- Reset/normalize styles
- Base typography
- Layout classes
- Component styles:
  - Navigation
  - Forms
  - Tables
  - Buttons
  - Alerts/messages
- Utility classes:
  - Spacing
  - Text alignment
  - Responsive helpers

### Responsive Design
- Mobile-first approach
- Breakpoints for tablet and desktop
- Flexible grid system
- Responsive navigation

## CSS Classes

### Layout
- `.container`: Main content container
- `.row`: Horizontal row
- `.col`: Column base class
- `.header`: Site header
- `.main`: Main content area
- `.footer`: Site footer

### Components
- `.book-list`: Book list table container
- `.book-form`: Book form container
- `.form-group`: Form field group
- `.btn`: Button base class
- `.btn-primary`: Primary action button
- `.btn-secondary`: Secondary action button
- `.alert`: Alert/message container
- `.alert-error`: Error message styling
- `.alert-success`: Success message styling

### Utility
- `.text-center`: Center aligned text
- `.text-right`: Right aligned text
- `.mb-*`: Margin bottom utilities
- `.mt-*`: Margin top utilities
- `.ml-*`: Margin left utilities
- `.mr-*`: Margin right utilities

## Responsive Breakpoints
- Mobile: 0px to 767px
- Tablet: 768px to 1023px
- Desktop: 1024px and above

## Example CSS Structure
```css
/* Base styles */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
}

/* Layout */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Components */
.btn {
  display: inline-block;
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-primary {
  background-color: #007bff;
  color: white;
}
# Templates Specification

## Base Template (templates/base.html)

### Structure
- HTML5 doctype
- Responsive meta tags
- Title block for page titles
- CSS stylesheet links
- Header with navigation
- Main content block
- Footer with application information

### Blocks
- `title`: Page title
- `content`: Main content area
- `extra_css`: Additional CSS files
- `extra_js`: Additional JavaScript files

## Book List Template (books/templates/books/book_list.html)

### Content
- Page title: "My Reading Diary"
- Link to add new book
- Filter form with:
  - Author search input
  - Rating range selects
  - Date range inputs
  - Apply filters button
- Sortable table with columns:
  - Title (sortable)
  - Author (sortable)
  - Date Finished (sortable)
  - Rating (sortable)
  - Notes (truncated if too long)
- Pagination controls
- "No books found" message when list is empty

### Features
- Sort indicators on currently sorted column
- Active filter display
- Responsive table design

## Add Book Template (books/templates/books/add_book.html)

### Content
- Page title: "Add New Book"
- Breadcrumb navigation
- BookForm rendering
- Submit button
- Cancel link to return to book list

### Form Display
- Form fields in vertical layout
- Field labels and help text
- Error messages display
- Required field indicators

## Book Detail Template (Optional) (books/templates/books/book_detail.html)

### Content
- Page title: "Book Details"
- Book information display:
  - Title
  - Author
  - Date Finished
  - Rating (stars display)
  - Notes (full text)
- Navigation links:
  - Back to book list
  - Edit book (if implemented)

## Template Tags and Filters
- Custom template tags for:
  - Displaying star ratings
  - Truncating long text
  - Formatting dates

## CSS Classes
- Consistent naming scheme: `book-list`, `book-form`, etc.
- Responsive design classes
- Utility classes for spacing and alignment
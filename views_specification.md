# Views Specification

## Book List View

### URL
- `/` (homepage)

### Functionality
- Display all books in a table format
- Provide sorting options:
  - By title (ascending/descending)
  - By author (ascending/descending)
  - By date finished (ascending/descending)
  - By rating (ascending/descending)
- Provide filtering options:
  - By author (text search)
  - By rating range (e.g., 4-5 stars)
  - By date range (from/to dates)
- Pagination for large datasets

### Context Data
- `books`: QuerySet of Book objects
- `sort_by`: Current sort field
- `sort_order`: Current sort order (asc/desc)
- `filter_author`: Current author filter
- `filter_rating_min`: Minimum rating filter
- `filter_rating_max`: Maximum rating filter
- `filter_date_from`: Start date filter
- `filter_date_to`: End date filter

## Add Book View

### URL
- `/add/`

### Functionality
- Display a form for adding a new book
- Handle form submission:
  - Validate input data
  - Save valid data to database
  - Redirect to book list on success
  - Display errors on invalid data

### Context Data
- `form`: BookForm instance

## Book Detail View (Optional)

### URL
- `/book/<id>/`

### Functionality
- Display detailed information about a specific book
- Show all book fields in a readable format

### Context Data
- `book`: Book object

## Template Context Processor
A context processor to provide common data to all templates:
- `site_title`: Application name for page titles
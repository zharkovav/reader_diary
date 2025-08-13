# Reader Diary - Django Web Application

## Project Overview
A web application built with Python Django to store and manage information about read books. Users can view their reading history, add new books, and filter/sort the book list.

## Technology Stack
- Backend: Python Django
- Database: MySQL
- Frontend: HTML, CSS, Django Templates

## Requirements
- Python 3.8 or higher
- Django 4.2 or higher
- MySQL database

## Installation
1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Configure database settings in `reader_diary/settings.py`
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Run the development server: `python manage.py runserver`

## Database Schema
### Book Model
- Title (CharField)
- Author (CharField)
- Date Finished (DateField)
- Rating (IntegerField) - Scale of 1-5
- Notes (TextField) - Optional notes about the book

## Application Structure
```
reader_diary/
├── manage.py
├── reader_diary/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── books/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── templates/
│   │   └── books/
│   │       ├── book_list.html
│   │       └── add_book.html
│   └── migrations/
│       ├── __init__.py
│       └── ...
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── base.html
    └── ...
```

## Features
1. **View List of Read Books**
   - Display all books in a table format
   - Show all relevant information (title, author, date finished, rating, notes)

2. **Sort and Filter Books**
   - Sort by title, author, date finished, rating
   - Filter by author, rating range, date range

3. **Add New Book**
   - Form to add new book entries
   - Validation for required fields
   - Date picker for date finished
   - Star rating selector

## URL Structure
- `/` - Homepage showing list of books
- `/add/` - Form to add a new book
- `/book/<id>/` - View details of a specific book (optional feature)

## Views
1. `book_list` - Display all books with sorting/filtering options
2. `add_book` - Handle form for adding new books
3. `book_detail` - (Optional) Show details of a specific book

## Templates
1. `base.html` - Base template with common HTML structure
2. `book_list.html` - Template for displaying the list of books
3. `add_book.html` - Template for the add book form

## Forms
1. `BookForm` - Django form for adding/editing books

## Workflow Diagram
```mermaid
graph TD
    A[User visits homepage] --> B[Display book list]
    B --> C{User action}
    C -->|Add book| D[Show add book form]
    C -->|Sort/Filter| E[Apply filters to book list]
    D --> F[Submit form]
    F --> G[Validate data]
    G -->|Valid| H[Save to database]
    G -->|Invalid| I[Show errors]
    H --> B
    I --> D
    E --> B
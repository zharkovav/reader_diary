# Reader Diary

A Django web application for tracking and managing books you've read.

## Features

- View a list of all books you've read
- Sort books by title, author, date finished, or rating
- Filter books by author, rating range, or date range
- Add new books with title, author, date finished, rating, and notes
- Responsive design that works on desktop and mobile devices
- Admin interface for managing books

## Technology Stack

- **Backend**: Python Django
- **Database**: SQLite (default) or MySQL
- **Frontend**: HTML, CSS, Django Templates

## Requirements

- Python 3.8 or higher
- Django 4.2 or higher
- mysqlclient package (only if using MySQL)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd reader-diary
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On Linux/Mac:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Configure the database:
   - By default, the application uses SQLite database which requires no additional setup
   - To use MySQL instead:
     - Create a MySQL database
     - Update the DATABASE settings in `reader_diary/settings.py` by uncommenting the MySQL configuration and commenting out the SQLite configuration

6. Run migrations:
   ```
   python manage.py migrate
   ```

7. Create a superuser (optional but recommended):
   ```
   python manage.py createsuperuser
   ```
   Or use the provided script:
   ```
   python create_superuser.py
   ```

8. Run the development server:
   ```
   python manage.py runserver
   ```

9. Visit `http://127.0.0.1:8000` in your browser

## Project Structure

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
│   ├── admin.py
│   ├── templates/
│   │   └── books/
│   │       ├── book_list.html
│   │       └── add_book.html
│   └── migrations/
├── static/
│   └── css/
│       └── style.css
└── templates/
    └── base.html
```

## Database Schema

### Book Model

| Field | Type | Description |
|-------|------|-------------|
| title | CharField | Book title (max 200 characters) |
| author | CharField | Book author (max 100 characters) |
| date_finished | DateField | Date when reading was completed |
| rating | IntegerField | Rating from 1-5 stars |
| notes | TextField | Optional notes about the book |

## Usage

1. **View Books**: Navigate to the homepage to see a list of all books
2. **Sort Books**: Click on column headers to sort by that field
3. **Filter Books**: Use the filter form to narrow down the book list
4. **Add Book**: Click "Add New Book" to add a book to your diary
5. **Admin Interface**: Visit `http://127.0.0.1:8000/admin/` to manage books through the admin interface (login with superuser credentials)

## Development

### Code Structure

- **Models**: Defined in `books/models.py`
- **Views**: Defined in `books/views.py`
- **Forms**: Defined in `books/forms.py`
- **Admin**: Defined in `books/admin.py`
- **URLs**: Main URLs in `reader_diary/urls.py`, app URLs in `books/urls.py`
- **Templates**: HTML templates in `templates/` and `books/templates/`
- **Static Files**: CSS files in `static/css/`

### Testing

Run tests with:
```
python manage.py test
```

### Additional Scripts

- `create_superuser.py`: Script to create a superuser account programmatically
- `test_books.py`: Script to add test books to the database
- `add_more_test_books.py`: Script to add more test books to the database

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

This project is licensed under the MIT License.
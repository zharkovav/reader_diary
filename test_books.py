import os
import sys
import django

# Add the project directory to the Python path
sys.path.append('d:/repo/reader_diary')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reader_diary.settings')

# Setup Django
django.setup()

# Test the Book model
from books.models import Book

# Check if there are any books
books = Book.objects.all()
print(f"Number of books in database: {books.count()}")

# Create a test book if none exist
if books.count() == 0:
    from datetime import date
    book = Book.objects.create(
        title="Test Book",
        author="Test Author",
        date_finished=date.today(),
        rating=5,
        notes="This is a test book"
    )
    print(f"Created test book: {book}")
else:
    print("Books already exist in the database:")
    for book in books:
        print(f"- {book}")
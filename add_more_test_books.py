import os
import sys
import django
from datetime import date, timedelta

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

# Create more test books if we don't have enough
if books.count() < 5:
    # Create a few more test books
    test_books = [
        {
            'title': "The Great Gatsby",
            'author': "F. Scott Fitzgerald",
            'date_finished': date.today() - timedelta(days=10),
            'rating': 4,
            'notes': "A classic American novel"
        },
        {
            'title': "To Kill a Mockingbird",
            'author': "Harper Lee",
            'date_finished': date.today() - timedelta(days=5),
            'rating': 5,
            'notes': "Powerful story about racial injustice"
        },
        {
            'title': "1984",
            'author': "George Orwell",
            'date_finished': date.today() - timedelta(days=15),
            'rating': 5,
            'notes': "Dystopian novel about totalitarianism"
        },
        {
            'title': "Pride and Prejudice",
            'author': "Jane Austen",
            'date_finished': date.today() - timedelta(days=20),
            'rating': 3,
            'notes': "Romantic novel of manners"
        }
    ]
    
    for book_data in test_books:
        # Check if the book already exists
        if not Book.objects.filter(title=book_data['title']).exists():
            book = Book.objects.create(**book_data)
            print(f"Created test book: {book}")
        else:
            print(f"Book '{book_data['title']}' already exists")
else:
    print("We have enough books for testing")
# URL Routing Specification

## Application URLs

### Main URLs (reader_diary/urls.py)
- `/` -> Include books app URLs
- `/admin/` -> Django admin interface

### Books App URLs (books/urls.py)
- `/` -> Book list view (name: 'book_list')
- `/add/` -> Add book view (name: 'add_book')
- `/book/<int:pk>/` -> Book detail view (name: 'book_detail')

## URL Patterns

### Book List
- Pattern: `''`
- View: `BookListView`
- Name: `'book_list'`
- HTTP Methods: GET

### Add Book
- Pattern: `'add/'`
- View: `AddBookView`
- Name: `'add_book'`
- HTTP Methods: GET, POST

### Book Detail (Optional)
- Pattern: `'book/<int:pk>/'`
- View: `BookDetailView`
- Name: `'book_detail'`
- HTTP Methods: GET

## URL Namespacing
- App namespace: `'books'`
- Example reverse URL: `reverse('books:book_list')`

## Example Usage
```python
# In templates
<a href="{% url 'books:book_list' %}">View All Books</a>
<a href="{% url 'books:add_book' %}">Add New Book</a>

# In views
from django.shortcuts import redirect
return redirect('books:book_list')
# Forms Specification

## BookForm

### Fields

#### Title
- Type: CharField
- Max Length: 200 characters
- Widget: TextInput with placeholder "Enter book title"
- Validation: Required field

#### Author
- Type: CharField
- Max Length: 100 characters
- Widget: TextInput with placeholder "Enter author name"
- Validation: Required field

#### Date Finished
- Type: DateField
- Widget: DateInput with format 'YYYY-MM-DD'
- Validation: Required field
- Help text: "Date when you finished reading this book"

#### Rating
- Type: ChoiceField
- Choices: [(1, '1 Star'), (2, '2 Stars'), (3, '3 Stars'), (4, '4 Stars'), (5, '5 Stars')]
- Widget: Select
- Validation: Required field
- Help text: "Rate the book from 1 to 5 stars"

#### Notes
- Type: CharField
- Widget: Textarea with 4 rows
- Required: False
- Help text: "Optional notes about the book"

### Validation
- Custom validation to ensure date finished is not in the future
- All required fields must be filled

### Styling
- CSS classes for consistent styling across the application
- Error messages for validation failures

### Example Usage
```python
# Creating a new book
form = BookForm(data={
    'title': 'The Great Gatsby',
    'author': 'F. Scott Fitzgerald',
    'date_finished': '2023-05-15',
    'rating': '4',
    'notes': 'A classic American novel about the Jazz Age.'
})

if form.is_valid():
    book = form.save()
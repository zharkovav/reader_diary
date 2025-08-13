# Book Model Specification

## Overview
The Book model will store information about books that have been read by the user.

## Fields

### Title
- Type: CharField
- Max Length: 200 characters
- Required: Yes
- Description: The title of the book

### Author
- Type: CharField
- Max Length: 100 characters
- Required: Yes
- Description: The author of the book

### Date Finished
- Type: DateField
- Required: Yes
- Description: The date when the user finished reading the book

### Rating
- Type: IntegerField
- Required: Yes
- Constraints: Value between 1 and 5 (inclusive)
- Description: User's rating of the book on a scale of 1 to 5 stars

### Notes
- Type: TextField
- Required: No
- Description: Optional notes or review comments about the book

## Model Methods

### __str__
- Returns: String representation of the book (title by author)

### get_absolute_url
- Returns: URL to the book's detail page

## Database Indexes
- Index on Date Finished (for sorting)
- Index on Author (for filtering)
- Index on Rating (for filtering)

## Example Usage
```python
book = Book(
    title="The Great Gatsby",
    author="F. Scott Fitzgerald",
    date_finished="2023-05-15",
    rating=4,
    notes="A classic American novel about the Jazz Age."
)
book.save()
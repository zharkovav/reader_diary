from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'date_finished', 'rating', 'notes']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Enter author name'}),
            'date_finished': forms.DateInput(attrs={'type': 'date'}),
            'rating': forms.Select(choices=[
                (1, '1 Star'),
                (2, '2 Stars'),
                (3, '3 Stars'),
                (4, '4 Stars'),
                (5, '5 Stars')
            ]),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }
        help_texts = {
            'date_finished': 'Date when you finished reading this book',
            'rating': 'Rate the book from 1 to 5 stars',
            'notes': 'Optional notes about the book',
        }
        
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating and (rating < 1 or rating > 5):
            raise ValidationError('Rating must be between 1 and 5.')
        return rating
        
    def clean_date_finished(self):
        date_finished = self.cleaned_data.get('date_finished')
        if date_finished and date_finished > timezone.now().date():
            raise ValidationError('Date finished cannot be in the future.')
        return date_finished
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes for styling
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date_finished = models.DateField()
    rating = models.IntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
        
    def get_absolute_url(self):
        # For now, return the book list URL since we don't have detail views yet
        from django.urls import reverse
        return reverse('books:book_list')
        
    class Meta:
        indexes = [
            models.Index(fields=['date_finished']),
            models.Index(fields=['author']),
            models.Index(fields=['rating']),
        ]
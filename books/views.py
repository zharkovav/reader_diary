from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Book
from .forms import BookForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('books:book_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'books/login.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('books:book_list')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('books:book_list')
    else:
        form = UserCreationForm()
    return render(request, 'books/register.html', {'form': form})


@login_required
def book_list(request):
    # Get books for the current user only
    books = Book.objects.filter(user=request.user)
    
    # Get sorting parameters
    sort_by = request.GET.get('sort_by', 'title')
    sort_order = request.GET.get('sort_order', 'asc')
    
    # Get filter parameters
    filter_author = request.GET.get('author', '')
    filter_rating_min = request.GET.get('rating_min', '')
    filter_rating_max = request.GET.get('rating_max', '')
    filter_date_from = request.GET.get('date_from', '')
    filter_date_to = request.GET.get('date_to', '')
    
    # Apply filters
    if filter_author:
        books = books.filter(author__icontains=filter_author)
    
    if filter_rating_min:
        books = books.filter(rating__gte=filter_rating_min)
        
    if filter_rating_max:
        books = books.filter(rating__lte=filter_rating_max)
        
    if filter_date_from:
        books = books.filter(date_finished__gte=filter_date_from)
        
    if filter_date_to:
        books = books.filter(date_finished__lte=filter_date_to)
    
    # Apply sorting
    valid_sort_fields = ['title', 'author', 'date_finished', 'rating']
    if sort_by in valid_sort_fields:
        if sort_order == 'desc':
            books = books.order_by(f'-{sort_by}')
        else:
            books = books.order_by(sort_by)
    
    # Apply pagination
    paginator = Paginator(books, 10)  # Show 10 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'books': page_obj,
        'sort_by': sort_by,
        'sort_order': sort_order,
        'filter_author': filter_author,
        'filter_rating_min': filter_rating_min,
        'filter_rating_max': filter_rating_max,
        'filter_date_from': filter_date_from,
        'filter_date_to': filter_date_to,
    }
    
    return render(request, 'books/book_list.html', context)


@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user  # Associate the book with the current user
            book.save()
            messages.success(request, 'Book added successfully!')
            return redirect('books:book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def index(request):
    books = Book.objects.all()
    return render(request, 'main/index.html', {'books': books})

def add_book(request, book_id):
    error = ''
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            book.delete()
            return redirect('home')
        else:
            error = 'К сожалению, форма была заполнена с ошибкой'
    form = BookForm()
    context = {
        'form': form,
        'error': error,
        'book_name': book.name
    }
    return render(request, 'main/add_book.html', context)


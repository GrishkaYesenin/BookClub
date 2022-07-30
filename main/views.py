from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def index(request):
    books = Book.objects.all()
    return render(request, 'main/index.html', {'books': books})

def add_book(request):
    error = ''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'К сожалению, форма была заполнена с ошибкой'
    form = BookForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_book.html', context)


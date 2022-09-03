from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def index(request):
    books = Book.objects.all().order_by("-datetime")
    return render(request, 'main/index.html', {'books': books})

def image_upload_view(request, book_id):
    """Process images uploaded by users"""
    error = ''
    old_book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            old_book.delete()
            return redirect('home')
    else:
        form = BookForm()
        context = {
            'form': form,
            'error': error,
            'book_name': old_book.name
        }
        return render(request, 'main/add_book.html', context)


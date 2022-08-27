from .models import Book
from django.forms import ModelForm, TextInput

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name", 'writer', "img"]

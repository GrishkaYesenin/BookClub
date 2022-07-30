from .models import Book
from django.forms import ModelForm, TextInput

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["name", 'writer']
        widgets = {
            'name': TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Назание'
            }),
            'writer': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            }),
        }
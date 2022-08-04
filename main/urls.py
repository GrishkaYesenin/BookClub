from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_book/<book_id>', views.add_book, name='add_book'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

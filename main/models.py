from django.db import models

class Book(models.Model):
    name = models.CharField('Название', max_length=100)
    writer = models.CharField('Автор', max_length=50)
    img = models.ImageField('img')
    booked = models.BooleanField('Бронь', default=False)
    datetime = models.DateTimeField('Время', auto_now=True)

def __str__(self):
    return self.name

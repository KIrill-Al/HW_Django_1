from django.contrib import admin

# Register your models here.
from .models import Genre
from .models import Author
from .models import Book

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)

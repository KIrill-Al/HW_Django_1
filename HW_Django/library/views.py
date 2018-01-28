from django.shortcuts import render
from .models import Book
from .models import Author


def books_list(request, name, sorted_column='title'):
    books = Book.objects.filter(author__name=name).all().prefetch_related(
        'genres').order_by(sorted_column)
    return render(request, 'library/books_list.html', {'books': books, 'name': name})


def authors_list(request):
    authors = Author.objects.all().order_by('name')
    for author in authors:
        print(author.book.all())
    return render(request, 'library/authors_list.html', {'authors': authors})
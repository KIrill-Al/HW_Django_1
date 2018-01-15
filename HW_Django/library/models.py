from django.db import models

# Create your models here.


class Book(models.Model):
    author = models.ForeignKey('Author', on_delete='CASCADE', blank=True, null=True)
    title = models.CharField('Заголовок', max_length=200)
    published_year = models.PositiveIntegerField('Год издания', blank=True, null=True)
    genre = models.ForeignKey('Genre', on_delete='CASCADE', blank=True, null=True)
    def __str__(self):
        return 'Автор: {}\nНазвание: {}\nЖанр: {}\nГод издания: {}\n'.format(self.author, self.title, self.genre, self.published_year)


class Author(models.Model):
    name = models.CharField('Имя', max_length=50)
    def __str__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField('Жанр', max_length=30)
    def __str__(self):
        return self.title

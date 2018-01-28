from django.db import models


class Book(models.Model):
    author = models.ForeignKey('Author', on_delete='CASCADE', blank=True, null=True, related_name='book')
    # author = models.ManyToManyField('Author', related_name = 'book')
    title = models.CharField('Заголовок', max_length=200)
    published_year = models.PositiveIntegerField('Год издания', blank=True, null=True)
    # genre = models.ForeignKey('Genre', on_delete='CASCADE', blank=True, null=True)
    genre = models.ManyToManyField('Genre', related_name='book')

    def __str__(self):
        return 'Автор: {}\nНазвание: {}\nЖанр: {}\nГод издания: {}\n'.format(self.author,
                                                                             self.title,
                                                                             self.genre,
                                                                             self.published_year)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Author(models.Model):
    name = models.CharField('Имя', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Genre(models.Model):
    title = models.CharField('Жанр', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
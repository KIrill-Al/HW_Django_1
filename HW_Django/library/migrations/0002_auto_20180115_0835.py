# Generated by Django 2.0.1 on 2018-01-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='library.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete='CASCADE', to='library.Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_year',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Год издания'),
        ),
    ]
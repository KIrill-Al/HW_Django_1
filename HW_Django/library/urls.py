from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.authors_list, name='authors'),
    path('<str:name>/', views.books_list, name='books'),
]

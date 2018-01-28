from django.conf.urls import url
from . import views


urlpatterns = [
    url('', views.authors_list, name='authors'),
    url('str:name/', views.books_list, name='books'),
]

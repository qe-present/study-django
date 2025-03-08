from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListCreateView.as_view(), name='book-list-create'),
    path('<int:pk>', views.BookRetrieveUpdateDestroyView.as_view(), name='book-retrieve-update-destroy'),
]
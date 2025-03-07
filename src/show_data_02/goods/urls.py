from django.urls import path
from . import views


urlpatterns=[
    path('', views.index),
    path('show', views.show),
    path('post', views.index_post)
]
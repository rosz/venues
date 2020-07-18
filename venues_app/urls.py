from django.urls import path
from . import views

urlpatterns = [
    path('', views.venues_list, name='venues_list'),
]
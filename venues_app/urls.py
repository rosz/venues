from django.urls import path
from . import views

urlpatterns = [
    path('', views.venues_list, name='venues_list'),
    path('venue/<int:pk>', views.venue, name='venue'),
]
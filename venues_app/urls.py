from django.urls import path
from . import views

urlpatterns = [
    path('', views.venues_list, name='venues_list'),
    path('search', views.search, name='search'),
    path('venue/<int:pk>', views.venue, name='venue'),
    path('venue/<int:pk>/rate', views.rate, name='rate'),
]
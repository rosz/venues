from django.urls import path
from . import views

urlpatterns = [
    path('', views.venues_list, name='venues_list'),
    path('search', views.search, name='search'),
    path('venue/<int:pk>', views.venue, name='venue'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.register_request, name='register'),
    path('venue/<int:pk>/rate', views.rate, name='rate'),
]
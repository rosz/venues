from django.contrib import admin
from .models import Venue, User


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'address')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('login',)

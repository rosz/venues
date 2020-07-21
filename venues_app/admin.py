from django.contrib import admin
from .models import Venue, Rating


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    ordering = ('name',)
    fields = ('name', 'created_at', 'avg_rating',
              'address', 'image', 'description',)
    search_fields = ('name',)
    readonly_fields = ('avg_rating', 'created_at')
    list_per_page = 5


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'venue', 'rate')
    search_fields = ('user', 'venue')
    ordering = ('user',)
    readonly_fields = ('user', 'venue', 'rate')

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

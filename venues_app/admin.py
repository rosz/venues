from django.contrib import admin
from .models import Venue, Rating


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    ordering = ('name',)
    fields = ('name',  'created_at', 'avg_rating', 'address', 'image', 'description',)
    search_fields = ('name',)
    readonly_fields = ('avg_rating', 'created_at')
    list_per_page = 5


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     ordering = ('created_at',)
#     fields = ('login', 'created_at',)
#     search_fields = ('login',)
#     readonly_fields = ('login', 'created_at',)
#     list_per_page = 5
#
#     def has_delete_permission(self, request, obj=None):
#         return False
#
#     def has_change_permission(self, request, obj=None):
#         return False


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'venue', 'rate')
    search_fields = ('user', 'venue')
    ordering = ('user',)
    readonly_fields = ('user', 'venue', 'rate')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False




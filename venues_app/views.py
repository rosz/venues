from django.shortcuts import render, get_object_or_404
from .models import Venue


def venues_list(request):
    venues = Venue.objects.order_by('created_at')
    return render(request, 'venues_app/venues_list.html', {'venues': venues})


def venue(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    return render(request, 'venues_app/venue.html', {'venue': venue})

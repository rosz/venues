from django.shortcuts import render


def venues_list(request):
    return render(request, 'venues_app/venues_list.html', {})

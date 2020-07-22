from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import Venue, Rating
from .forms import RatingForm

OBJ_PER_PAGE = 3


def venues_list(request):

    venues = Venue.objects.order_by('created_at')
    paginator = Paginator(venues, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'venues_app/venues_list.html',
                  {'page_obj': page_obj})


def search(request):
    name = request.GET.get('search_name')
    if name is not None:
        venues = Venue.objects.filter(
            name__icontains=name).order_by('created_at')
        paginator = Paginator(venues, OBJ_PER_PAGE)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        if page_obj is not None:
            return render(request, 'venues_app/venues_list.html',
                          {'page_obj': page_obj})


def venue(request, pk):
    venue = get_object_or_404(Venue, pk=pk)
    return render(request, 'venues_app/venue.html', {'venue': venue})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'Zalogowano jako {username}')
                return redirect('venues_list')
            else:
                messages.error(request, 'Błędna nazwa lub hasło')
        else:
            messages.error(request, 'Błędna nazwa lub hasło')
    form = AuthenticationForm()
    return render(request, 'venues_app/login.html', {'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, 'Wylogowano')
    return redirect('venues_list')


def register_request(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(messages.info(request, 'Zarejestowano'))
            return redirect('venues_list')

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request, 'venues_app/register.html', {'form': form})

    form = UserCreationForm()
    return render(request, 'venues_app/register.html', {'form': form})


@require_POST
def rate(request, pk):
    venue_obj = get_object_or_404(Venue, id=pk)

    rating = Rating.objects.get_or_create(
        user=request.user, venue=venue_obj)[0]
    form = RatingForm(request.POST, instance=rating)

    if form.is_valid():
        form.save()
        return redirect('venues_list')
    else:
        return redirect('venues_list')

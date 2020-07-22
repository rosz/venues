from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout


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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import Signupform

# Create your views here.


def index(request):
    return render(request, 'account/index.html')


def logout_user(request):
    logout(request)
    return render(request, 'account/login.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            return render(request, 'account/login.html', {'error_message': 'Invalid login'})
    return render(request, 'account/login.html')



def register(request):
    form = Signupform(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data.get("confirm_password")
        if password != confirm_password:
            return render(request, 'account/signupform.html', {'form': form, 'error_message': "Password not confirmed"})
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
    context = {
        "form": form,
    }
    return render(request, 'account/signupform.html', context)

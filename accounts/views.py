from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully')
            return redirect('accounts:register')
        else:
            messages.warning(request, 'Invalid Form')
            return render(request, 'register.html', {'form':form })
    else:
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form':form })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mainapp:index')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('accounts:login')
    return render(request, 'login.html')
def user_logout(request):
        logout(request)
        return render(request, 'logout.html')

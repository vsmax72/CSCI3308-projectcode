from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm


def register (request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST) # this is a form which come from django and it will become html
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username') #falsh data
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form}) # form is the content 

def login (request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            return redirect('music')

    else:
        form = AuthenticationForm()
    return render(request,'users/login.html',{'form':form})

"""
messages.success(request, f'Account created for {username}!')



"""

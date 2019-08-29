from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from user.forms import SignUpForm,ProfileForm,UserForm
from user.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def login_view(request):
    error=''
    if request.method=='POST':
        username= request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('/')

        else:
            error='incorrect username or password'
    
    context={
        "error":error
    }
    
    return render(request,'user/login.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/user/login')


def signup(request):#change this view according to silmple is better than complex
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('profile_update')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})

def profile_view(request,id):
    user=User.objects.get(pk=id)
    context={
        "user":user
    }
    return render(request,'user/profile.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return HttpResponseRedirect('/')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'user/profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
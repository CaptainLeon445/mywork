from django.shortcuts import render
from fifth_app.forms import UserForm,UserProfileInfoForm

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'fifth_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):

    registered= False

    if request.method == 'POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=True)
            profile.user=user
            return(request)

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    
    return render(request, 'fifth_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def relative(request):
    return render(request, 'fifth_app/relative_url.html')

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active")

        else:
            print("Login Failed!")
            print("Username: {} and Password:{}".format(username,password))
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request,'fifth_app/login.html',{})
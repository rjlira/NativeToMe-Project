from random import randint
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import editProfileForm
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from .models import UserProfile
from tribes.models import Tribe, Posts


"""Python functions that take a request and render a web page"""
def loginView(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        print("Successful Login")
        login(request, user)
        print("User Profile after Login")
        return profileView(request)
    else:
        print("Failed to Login. Try again")
        return render(request, 'accounts/login.html/', {'title':'Login'})

@login_required
def profileView(request):
    """Grab data"""
    current_user = User.objects.get(username=request.user)
    form = editProfileForm(request.POST)
    """Check for profile object"""
    if UserProfile.objects.filter(pk=current_user).exists() == True and Posts.objects.filter(tribePosterID = current_user).exists() == True:
        print("TRUE")
        profile = UserProfile.objects.get(pk=current_user)
        posts = Posts.objects.filter(tribePosterID=current_user)
        context = {'posts': posts,
                   'form': form,
                   'profile': profile}
        print(profile)

    """This is to create a profile object if one is no found!"""
    if(UserProfile.objects.filter(pk=request.user).exists() == False):
        print(current_user.username + " does not have a profile!")
        profile = UserProfile()
        profile.user = current_user
        posts = Posts.objects.filter(tribePosterID=current_user)
        print(posts)
        profile.save()

        context = {'posts': posts,
                   'form': form,
                   'profile': profile}

        return render(request, 'accounts/userprofile/userprofile.html', context)
    elif(UserProfile.objects.filter(pk=request.user).exists() == True):
        print(current_user.username + " already has an account.")
        profile = UserProfile.objects.get(pk=request.user)
        posts = Posts.objects.filter(tribePosterID=current_user)
        if request.method == "GET":
            print("User Profile GET")
            form = editProfileForm(request.POST)


            context = {'posts': posts,
                       'form': form,
                       'profile': profile}

            return render(request, 'accounts/userprofile/userprofile.html', context)
        else:
            """This is for editing!"""
            print("User Profile POST")
            form = editProfileForm(request.POST)
            # check if form is valid
            print(form.is_valid())
            if form.is_valid():
                print("<!---------------------Its working---------------------!>")
                profile.location = form.cleaned_data.get("location")
                profile.school = form.cleaned_data.get("school")
                profile.hobbies = form.cleaned_data.get("hobbies")
                profile.bio = form.cleaned_data.get("bio")
                #test#
                profile.likes = form.cleaned_data.get("likes")
                profile.dislikes = form.cleaned_data.get("dislikes")
                profile.image = form.cleaned_data.get("image")
                ######
                profile.save()

                context = {'posts': posts,
                           'form': form,
                           'profile': profile}

                print("Successfully saved information")
                return render(request, 'accounts/userprofile/userprofile.html', context)
            else:
                print("Invalid form!")
                context = {'posts': posts,
                           'form': form,
                           'profile': profile}
                return render(request, 'accounts/userprofile/userprofile.html', context)
    else:
        return render(request, 'home/home.html', {})


def logoutView(request):
        logout(request)
        return render(request, 'accounts/logout.html/', {'title': 'Login'})

@csrf_protect
def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            """Make a UseProfile object for the new user"""
            return HttpResponseRedirect('/accounts/login.html/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html/', {"form" : form})



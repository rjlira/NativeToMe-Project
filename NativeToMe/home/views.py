from django.shortcuts import render
# Create your views here.

"""Python functions that take a request and render a web page"""

def homeView(request):
    print("Home Page")
    return render(request, 'home/home.html/', {'title':'Home'})
from django.urls import path

app_name = 'accounts'

from . import views
urlpatterns = [
    path('login.html/', views.loginView, name='loginView'),
    path('logout.html/', views.logoutView, name='logoutView'),
    path('register.html/', views.registerView, name='registerView'),
    path('userprofile/userprofile.html/', views.profileView, name='profileView'),
]
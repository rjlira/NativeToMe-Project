from django.urls import path

app_name = 'tribes'

from . import views
urlpatterns = [
    path('tribeHomePage.html/<tribeID>/', views.tribeHomePage, name='tribeHomePage'),
    path('tribeCreatePage.html/', views.tribeCreate, name='tribeCreate'),
    path('tribeSearchPage.html/', views.tribeSearchPage, name='tribeSearchPage'),
    path('tribeManagePage.html/<tribeID>/', views.tribeManagePage, name='tribeManagePage'),
    path('tribeHousePage.html/<tribeID>/', views.tribeHousePage, name='tribeHousePage')
]
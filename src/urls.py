from django.urls import path, include

from . import views

from django.contrib import admin


urlpatterns = [
    path('', views.home, name='home'),
    path('get-cards', views.getCards, name='getCards'),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

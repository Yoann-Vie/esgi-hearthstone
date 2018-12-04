from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('get-cards', views.getCards, name='getCards'),
    path('my-cards', views.myCards, name='myCards'),
]

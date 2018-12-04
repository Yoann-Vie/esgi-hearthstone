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
    path('my-decks', views.myDecks, name='myDecks'),
    path('deck/new', views.newDeck, name='newDeck'),
    path('deck/edit/<int:id>/', views.updateDeck, name='updateDeck'),
    path('deck/delete/<int:id>/', views.deleteDeck, name='deleteDeck'),
    path('deck/add/<int:cardId>/<int:deckId>', views.addCardToDeck, name='addCardToDeck'),
    path('deck/remove/<int:cardId>/<int:deckId>', views.removeCardFromDeck, name='removeCardFromDeck'),
]

from __future__ import unicode_literals
from django.urls import path
from django.conf.urls import include, url
from . import views

import spirit.topic.views
import spirit.admin.urls
import spirit.user.urls
import spirit.search.urls
import spirit.category.urls
import spirit.topic.urls
import spirit.comment.urls

#app_name = 'spirit'

urlpatterns = [
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^forum/', spirit.topic.views.index_active, name='index'),
    url(r'^forum/st/admin/', include(spirit.admin.urls)),
    url(r'^forum/user/', include(spirit.user.urls)),
    url(r'^forum/search/', include(spirit.search.urls)),
    url(r'^forum/category/', include(spirit.category.urls)),
    url(r'^forum/topic/', include(spirit.topic.urls)),
    url(r'^forum/comment/', include(spirit.comment.urls)),
    path('', views.home, name='home'),
    path('historic', views.historic, name='historic'),
    path('training', views.training, name='training'),
    path('training/recruit', views.recruit, name='recruit'),
    path('training/veteran', views.veteran, name='veteran'),
    path('training/champion', views.champion, name='champion'),
    path('training/legend', views.legend, name='legend'),
    path('accounts/register/', views.register, name='register'),
    path('players', views.players, name='players'),
    path('actuality', views.actuality, name='actuality'),
    path('market', views.market, name='market'),
    path('market/buy/<int:id>', views.buyCard, name='buyCard'),
    path('players/player/<int:id>', views.showPlayer, name='showPlayer'),
    path('players/player/<int:id>/follow', views.follow, name='follow'),
    path('players/player/<int:id>/unfollow', views.unfollow, name='unfollow'),
    path('players/player/<int:id>/battle', views.battle, name='battle'),
    path('players/player/<int:userId>/deck/<int:deckId>', views.showPlayerDeck, name='showPlayerDeck'),
    path('get-cards', views.getCards, name='getCards'),
    path('my-cards', views.myCards, name='myCards'),
    path('my-cards/bet/<int:id>', views.betCard, name='betCard'),
    path('my-cards/remove/<int:id>', views.removeCard, name='removeCard'),
    path('my-cards/delete/<int:id>/<int:price>', views.sellCard, name='sellCard'),
    path('my-decks', views.myDecks, name='myDecks'),
    path('deck/new', views.newDeck, name='newDeck'),
    path('deck/edit/<int:id>/', views.updateDeck, name='updateDeck'),
    path('deck/delete/<int:id>/', views.deleteDeck, name='deleteDeck'),
    path('deck/select/<int:id>/', views.selectDeck, name='selectDeck'),
    path('deck/add/<int:cardId>/<int:deckId>', views.addCardToDeck, name='addCardToDeck'),
    path('deck/remove/<int:cardId>/<int:deckId>', views.removeCardFromDeck, name='removeCardFromDeck'),
]

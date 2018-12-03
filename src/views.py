from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from random import randint
from .models import Card, CardUser

def home(request):
    return render(request, 'hearthstone/index.html', context = { 'title': 'Accueil' })

def register(request):
    return render(request, 'accounts/register/', context = { 'title': 'Register' })

def getCards(request):
    earned_cards = []
    cards_count = Card.objects.all().count()
    if request.user.is_authenticated:
        for i in range(6):
            random_index = randint(0, cards_count - 1)
            card = Card.objects.all()[random_index]
            earned_cards.append(card)
            cardUser = CardUser(card=card, user = request.user)
            cardUser.save()
    else:
        messages.warning(request, f'Vous devez être connecté pour obtenir des cartes')
        return redirect('home')

    return render(request, 'hearthstone/get-cards.html', { 'title': 'Nouvelles cartes', 'pack_cards': earned_cards })

def myCards(request):
    user_cards = []
    associations = CardUser.objects.all().filter(user_id = request.user.id)

    for association in associations:
        user_card = association.card
        user_cards.append(user_card)

    return render(request, 'hearthstone/my-cards.html', { 'title': 'Mes cartes', 'user_cards': user_cards })

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from random import randint
from .models import Card, CardUser, Deck, CardDeck
from .forms import DeckForm

def home(request):
    return render(request, 'hearthstone/index.html', context = { 'title': 'Accueil' })

def register(request):
    return render(request, 'accounts/register/', context = { 'title': 'Register' })

def initCards(request):
    earned_cards = []
    if request.user.is_authenticated:
        for i in range(30):
            card = Card.objects.all()[i]
            earned_cards.append(card)
            cardUser = CardUser(card=card, user = request.user)
            cardUser.save()

def getCards(request):
    earned_cards = []
    cards_count = Card.objects.all().count()
    if request.user.is_authenticated:
        for i in range(8):
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

def myDecks(request):
    user_decks = Deck.objects.all().filter(user_id = request.user.id)

    return render(request, 'hearthstone/my-decks.html', { 'title': 'Mes decks', 'user_decks': user_decks })

def newDeck(request):
    if request.POST:
        form_values = request.POST.copy()
        form_values.update({'user': request.user.id})
        form = DeckForm(form_values)
        if form.is_valid():
            form.save()
            return redirect('myDecks')
    else:
        form = DeckForm()

    return render(request, 'hearthstone/form-deck.html', {'form': form})

def updateDeck(request, id=0):
    if id == 0:
        return redirect('myDecks')

    deck = Deck.objects.get(pk = id)
    if request.POST:
        form_values = request.POST.copy()
        form_values.update({'user': request.user.id})
        form = DeckForm(form_values, instance=deck)
        if form.is_valid():
            form.save()
            return redirect('myDecks')
    else:
        form = DeckForm(instance=deck)

    deck_cards = []
    already_added = []
    associations = CardDeck.objects.all().filter(deck_id = id)
    for association in associations:
        deck_card = association.card
        already_added.append(deck_card.id)
        deck_cards.append(deck_card)

    remaining_cards = []
    associations = CardUser.objects.all().filter(user_id = request.user.id)
    for association in associations:
        user_card = association.card
        if user_card.id not in already_added:
            remaining_cards.append(user_card)

    return render(request, 'hearthstone/form-deck.html', {
        'form': form,
        'remaining_cards': remaining_cards,
        'deck_cards': deck_cards,
        'deck_id': id
    })

def deleteDeck(request, id=0):
    if id == 0:
        return redirect('myDecks')

    deck = Deck.objects.get(pk = id)
    deck.delete()

    return redirect('myDecks')

def addCardToDeck(request, cardId=0, deckId=0):
    if cardId == 0 or deckId == 0:
        return redirect('myDecks')

    deck_card = CardDeck(card = Card.objects.get(pk = cardId), deck = Deck.objects.get(pk = deckId))
    deck_card.save()

    return redirect('updateDeck', id=deckId)

def removeCardFromDeck(request, cardId=0, deckId=0):
    if cardId == 0 or deckId == 0:
        return redirect('myDecks')

    deck_card = CardDeck.objects.get(card = Card.objects.get(pk = cardId), deck = Deck.objects.get(pk = deckId))
    deck_card.delete()

    return redirect('updateDeck', id=deckId)


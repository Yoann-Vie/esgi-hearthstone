from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from random import randint
from .models import Card, CardUser, Deck, CardDeck
from .forms import DeckForm

def home(request):
    return render(request, 'hearthstone/index.html', context = { 'title': 'Accueil' })

def training(request):
    return render(request, 'hearthstone/training.html', context = { 'title': 'The training room' })

def recruit(request):
    result = 0
    attack = 0
    health = 0
    leDeck = Deck.objects.get(user_id = request.user.id,selection=1)
    associations = CardDeck.objects.all().filter(deck_id =leDeck.id)
    for association in associations:
        deck_card = association.card
        if deck_card.attack is not None:
            attack += deck_card.attack
        if deck_card.health is not None:
            health += deck_card.health
    if attack >= 30 and health >= 20:
        result = 1
        request.user.player.gold += 2
        request.user.save()

    return render(request, 'hearthstone/result.html', context = { 'title': 'The training room', 'result': result})

def veteran(request):
    result = 0
    attack = 0
    health = 0
    leDeck = Deck.objects.get(user_id = request.user.id,selection=1)
    associations = CardDeck.objects.all().filter(deck_id =leDeck.id)
    for association in associations:
        deck_card = association.card
        if deck_card.attack is not None:
            attack += deck_card.attack
        if deck_card.health is not None:
            health += deck_card.health
    if attack >= 40 and health >= 30:
        result = 1
        request.user.player.gold += 4
        request.user.save()

    return render(request, 'hearthstone/result.html', context = { 'title': 'The training room', 'result': result})

def champion(request):
    result = 0
    attack = 0
    health = 0
    leDeck = Deck.objects.get(user_id = request.user.id,selection=1)
    associations = CardDeck.objects.all().filter(deck_id =leDeck.id)
    for association in associations:
        deck_card = association.card
        if deck_card.attack is not None:
            attack += deck_card.attack
        if deck_card.health is not None:
            health += deck_card.health
    if attack >= 50 and health >= 40:
        result = 1
        request.user.player.gold += 8
        request.user.save()

    return render(request, 'hearthstone/result.html', context = { 'title': 'The training room', 'result': result})

def legend(request):
    result = 0
    attack = 0
    health = 0
    leDeck = Deck.objects.get(user_id = request.user.id,selection=1)
    associations = CardDeck.objects.all().filter(deck_id =leDeck.id)
    for association in associations:
        deck_card = association.card
        if deck_card.attack is not None:
            attack += deck_card.attack
        if deck_card.health is not None:
            health += deck_card.health
    if attack >= 60 and health >= 50:
        result = 1
        request.user.player.gold += 16
        request.user.save()

    return render(request, 'hearthstone/result.html', context = { 'title': 'The training room', 'result': result})

def battle(request,id=0):
    result = 0
    myAttack = 0
    myHealth = 0
    hisAttack = 0
    hisHealth = 0
    myDeck = Deck.objects.get(user_id = request.user.id,selection=1)
    hisDeck = Deck.objects.get(user_id = id,selection=1)
    myAssociations = CardDeck.objects.all().filter(deck_id =myDeck.id)
    for association in myAssociations:
        deck_card = association.card
        if deck_card.attack is not None:
            myAttack += deck_card.attack
        if deck_card.health is not None:
            myHealth += deck_card.health
    hisAssociations = CardDeck.objects.all().filter(deck_id =hisDeck.id)
    for association in hisAssociations:
        deck_card = association.card
        if deck_card.attack is not None:
            hisAttack += deck_card.attack
        if deck_card.health is not None:
            hisHealth += deck_card.health
    if myAttack > hisAttack and myHealth > hisHealth:
        result = 1
        request.user.player.gold += 20
        request.user.save()

    return render(request, 'hearthstone/result.html', context = { 'title': 'The training room', 'result': result})

def register(request):
    return render(request, 'accounts/register/', context = { 'title': 'Register' })

def players(request):
    users = User.objects.all()
    return render(request, 'hearthstone/players.html', { 'title': 'List of all players', 'users': users })

def showPlayer(request,id=0):
    user = User.objects.get(id=id)
    user_decks = Deck.objects.all().filter(user_id=id)
    return render(request, 'hearthstone/player.html', { 'title': 'Page of '+user.username, 'user': user, 'user_decks': user_decks })

def showPlayerDeck(request,userId=0,deckId=0):
    user = User.objects.get(id=userId)
    deck = Deck.objects.get(id=deckId)
    deck_cards = []
    associations = CardDeck.objects.all().filter(deck_id =deckId)
    for association in associations:
        deck_card = association.card
        deck_cards.append(deck_card)

    return render(request, 'hearthstone/deck.html', { 'title': 'Deck of '+user.username, 'user': user, 'deck': deck, 'deck_cards': deck_cards })

def getCards(request):
    earned_cards = []
    cards_count = Card.objects.all().count()
    if request.user.is_authenticated and request.user.player.gold >= 100:
        request.user.player.gold = request.user.player.gold-100
        request.user.save()
        for i in range(8):
            random_index = randint(0, cards_count - 1)
            card = Card.objects.all()[random_index]
            earned_cards.append(card)
            cardUser = CardUser(card=card, user = request.user)
            cardUser.save()
    else:
        messages.warning(request, f'Vous devez être connecté pour obtenir des cartes ou avoir asser d\'argent, pauvre')
        return redirect('home')

    return render(request, 'hearthstone/get-cards.html', { 'title': 'Nouvelles cartes', 'pack_cards': earned_cards })

def myCards(request):
    user_cards = []
    associations = CardUser.objects.all().filter(user_id = request.user.id)

    for association in associations:
        user_card = association.card
        user_cards.append([user_card,association])

    return render(request, 'hearthstone/my-cards.html', { 'title': 'Mes cartes', 'user_cards': user_cards })

def sellCard(request,id=0,price=0):
    if id == 0:
        return redirect('myCards')

    card = Card.objects.get(pk = id)
    card.delete()
    request.user.player.gold = request.user.player.gold+price
    request.user.save()
    return redirect('myCards')

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

def selectDeck(request, id=0):
    if id == 0:
        return redirect('myDecks')

    Deck.objects.all().filter(user_id = request.user.id,selection=1).update(selection=0)
    Deck.objects.all().filter(user_id = request.user.id,id=id).update(selection=1)

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


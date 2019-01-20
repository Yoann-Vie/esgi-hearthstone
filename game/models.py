from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gold = models.PositiveIntegerField(default=200)

class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    selection = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return self.name

class Historic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)

class Following(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follow = models.PositiveIntegerField()

class Card(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    img = models.CharField(max_length=100, null=True, blank=True)
    attack = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class CardUser(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0, blank=True)
    state = models.PositiveIntegerField(default=0, blank=True)


class CardDeck(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

#Signals When user is create
@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        firstDeck = Deck.objects.create(user=instance,name='Deck de Base',selection=1)
        earned_cards = []
        for i in range(30):
            card = Card.objects.all()[i]
            earned_cards.append(card)
            cardUser = CardUser(user=instance,card=card)
            deckUser = CardDeck(card=card,deck=firstDeck)
            cardUser.save()
            deckUser.save()

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()

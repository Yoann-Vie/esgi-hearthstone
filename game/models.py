from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gold = models.PositiveIntegerField(default=200)

@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()

class Deck(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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


class CardDeck(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

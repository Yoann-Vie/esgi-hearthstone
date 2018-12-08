from django.apps import AppConfig
from django_registration.signals import user_registered
from .signals import init


class HearthstoneConfig(AppConfig):
    name = 'game'

    def ready(self):
        user_registered.connect(init)

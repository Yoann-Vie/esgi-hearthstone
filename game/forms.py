from django.forms import ModelForm
from .models import Deck, CardUser

class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = '__all__'

class CardUserForm(ModelForm):
    class Meta:
        model = CardUser
        fields = '__all__'

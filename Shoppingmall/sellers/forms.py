from django import forms
from .models import Item

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name','category', 'image','price','description','stock','seller']

from django import forms

from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = [
            'email',
            'first_name',
            'last_name',
            'location',
        ]

        #alternatives : 
        #fields = '__all__'
        #exclude = ['timestamp'] (si fields n'est pas spécifié mais seulement exclude, alors fields par défaut vaut '__all__')

        labels = {
            'email': 'Addresse e-mail',
            'first_name': 'Prénom',
            'last_name': 'Nom',
            'location': 'Commune',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }



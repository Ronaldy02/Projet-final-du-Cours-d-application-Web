from django import forms 
from .models import Livre
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'isbn', 'date_publication']
        widgets = {
            'date_publication':forms.DateInput(attrs={'type':'date'}),
        }
        labels = {
            'titre':'Entrez le titre du livre',
            'auteur':'Entrez l\'auteur du livre',
            'isbn': 'Entrez l\'ISBN (facultatif)',
            'date de publication' : 'Entrez la date de publication',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['titre'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Entrez le titre du livre ici ....'
        })
        self.fields['auteur'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Entrez l\'auteur du livre ici ....'
        })
        self.fields['isbn'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Entrez l\'isbn du livre ici ....'
        })


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

        labels = {
            'first_name':'Nom',
            'last_name':'Prenom',
            'username': 'Nom d\'utilisateur',
            'email' : 'Email',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Entrez votre nom ici ....'
        })
        self.fields['last_name'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Entrez votre prenom ici ....'
        })
        self.fields['username'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Entrez votre nom d\'utilisateur ici ....'
        })
        self.fields['email'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Entrez votre adresse email ici ....'
        })
        self.fields['password1'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Entrez votre mot de passe ici ....'
        })
        self.fields['password2'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder' : 'Confirmez votre mot de passe'
        })
        # Suppression de l'affichage des requirements
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        # Ajout de label
        self.fields['password1'].label = 'Mot de passe'
        self.fields['password2'].label = 'Confirmation mot de passe'
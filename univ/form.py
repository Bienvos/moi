from django import forms
from .models import etudiant
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class log_u(UserCreationForm):
     
    username = forms.CharField(max_length=200, label='Nom Utilisateur', widget=forms.TextInput(attrs={
           'class':'form-control',
     }))
    first_name = forms.CharField(max_length=200, label='Prenom', widget=forms.TextInput(attrs={
           'class':'form-control',
     }))
    email = forms.EmailField(max_length=200, label='email', widget=forms.EmailInput(attrs={
           'class':'form-control',
     }))
    password1 = forms.CharField(max_length=200, label='Mot de Passe', widget=forms.PasswordInput(attrs={
           'class':'form-control',
     }))
    
    password2 = forms.CharField(max_length=200, label='Confirmer', widget=forms.PasswordInput(attrs={
           'class':'form-control',
     }))


    class Meta:
          model =User
          fields =[
               'username',
               'email',
               'first_name',
               'password1',
               'password2'
          ]













class etud(forms.ModelForm):
        nom = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Entrer votre nom ici'}))
        prenom = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'enter your fristname here'}))


        class Meta:
          model = etudiant
          fields = ('nom','prenom','image','sexe','date')

        #def clean_prenom(self, *args, **kwargs):
               # prenom=self.cleaned_data.get('prenom')
                #if 'bie' in prenom:
                    #return prenom
                #else :
                    #raise forms.ValidationError('le mot bie doit apparaitre dans prenom')
                            
                
      
      
      


class create_p(forms.Form):
    nom = forms.CharField(label ='',widget=forms.TextInput(
        attrs={
            'placeholder':'Entrer votre nom ici'
        }
    ))
    prenom = forms.CharField(label ='',widget=forms.Textarea(
        attrs={
            'placeholder': 'enter your fristname here'
            #'rows':3,
            #'cols':10,
            #'id':'bienvos',
            #'class':'C1 C2 C3'

        }
    ))
    filiere = forms.CharField( initial='SRI')
    


class personne(forms.Form):
    name = forms.CharField()
    last_name = forms.CharField()
    description= forms.CharField()



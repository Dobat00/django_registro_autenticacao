from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class CadastroForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
        # def clean_email(self):
            # mail = self.cleaned_data.get('email')
            # if not is_valid():
            #     raise ValidationError('Errado')
        #

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget = TextInput())
    password = forms.CharField(widget = PasswordInput())

from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserAdminCreationsForm(UserCreationForm):
    email = forms.EmailField()
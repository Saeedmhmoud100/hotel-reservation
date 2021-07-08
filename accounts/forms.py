from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth import get_user_model


class UserAdminCreationsForm(UserCreationForm):
    email = forms.EmailField()
    
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','email','image', 'country', 'city', 'phone_number', )
        
class LoginForm(AuthenticationForm):
    username = UsernameField()
    password = forms.CharField(widget=forms.PasswordInput())

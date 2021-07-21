from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth import get_user_model


class UserAdminCreationsForm(UserCreationForm):
    email = forms.EmailField()
    
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(min_length=8)
    class Meta:
        model = get_user_model()
        fields = ('username','email','image', 'country', 'city', 'phone_number', )
        
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'placeholder':'Enter Username or Email'}))
    password = forms.CharField(min_length=8,widget=forms.PasswordInput())
    remember_me = forms.BooleanField(label='Remember Me', initial=False,required=False, widget=forms.CheckboxInput(attrs={'checked': True}))
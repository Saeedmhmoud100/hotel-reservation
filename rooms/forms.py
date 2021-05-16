from django import forms
from django.utils import timezone
from datetime import date

from . models import Room_Reservation
class RoomReservationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email_entred = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    data_from = forms.DateField(initial=date.today,input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y'],required=False,widget=forms.DateInput(attrs={'class':'form-control','placeholder':'{}'.format(timezone.now().date())}))
    data_to = forms.DateField(initial=date.today,input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y'],required=False,widget=forms.DateInput(attrs={'class':'form-control','placeholder':'{}'.format(timezone.now().date())}))
    guste = forms.IntegerField(max_value=6,min_value=1,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Guest'}))
    children = forms.IntegerField(max_value=6,min_value=0,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Children'}))
    class Meta:
        model = Room_Reservation
        fields = ('name','email_entred','data_from','data_to','guste','children')

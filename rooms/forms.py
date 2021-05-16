from django import forms
from . models import Room_Reservation
class RoomReservationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email_entred = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    data_from = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Date from'}))
    data_to = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','placeholder':'Date to'}))
    guste = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Guest'}))
    children = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Children'}))
    class Meta:
        model = Room_Reservation
        fields = ('name','email_entred','Data_from','Data_to','guste','children')
    
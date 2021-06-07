from django import forms
from datetime import date
from django.utils import timezone
from .models import Tour_Reservation

class TourReservationForm(forms.ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    data_from = forms.DateField(initial=date.today,input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y'],required=False,widget=forms.DateInput(attrs={'class':'form-control','placeholder':'{}'.format(timezone.now().date())}))
    data_to = forms.DateField(initial=date.today,input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y'],required=False,widget=forms.DateInput(attrs={'class':'form-control','placeholder':'{}'.format(timezone.now().date())}))
    guste = forms.IntegerField(label='',max_value=6,min_value=1,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Guest'}))
    children = forms.IntegerField(label='',max_value=6,min_value=0,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Children'}))
    class Meta:
        model = Tour_Reservation
        fields = ('name','email','data_from','data_to','guste','children')
        
    def __init__(self, *args, **kwargs):
        self.tour = kwargs.pop("tour")
        super().__init__(*args, **kwargs)
    
    def clean_data_from(self):
        data_from = self.cleaned_data['data_from']
        if Tour_Reservation.objects.is_active().filter(data_from=data_from,tour=self.tour).exists():
            raise forms.ValidationError('This date is already booked')
        if data_from < timezone.now().date():
            raise forms.ValidationError('Enter a valid date')
        return data_from
    
    def clean_data_to(self):
        data_to = self.cleaned_data['data_to']   
        if Tour_Reservation.objects.is_active().filter(data_to=data_to,tour=self.tour).exists():
            raise forms.ValidationError('This date is already booked')
        if data_to < self.cleaned_data['data_from']:
            raise forms.ValidationError('Enter a valid date')
        return data_to

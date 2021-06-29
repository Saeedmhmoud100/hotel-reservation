from django import forms
from django.forms.models import inlineformset_factory
from django.utils import timezone
from datetime import date
from django_countries.data import COUNTRIES
from ckeditor.fields import RichTextField
from . models import Room,Room_Reservation,Room_image


class RoomReservationForm(forms.ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email_entred = forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    data_from = forms.DateField(initial=date.today,input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y'],required=False,widget=forms.DateInput(attrs={'class':'form-control','placeholder':'{}'.format(timezone.now().date())}))
    data_to = forms.DateField(initial=date.today,input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y'],required=False,widget=forms.DateInput(attrs={'class':'form-control','placeholder':'{}'.format(timezone.now().date())}))
    guste = forms.IntegerField(label='',max_value=6,min_value=1,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Guest'}))
    children = forms.IntegerField(label='',max_value=6,min_value=0,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Children'}))
    class Meta:
        model = Room_Reservation
        fields = ('name','email_entred','data_from','data_to','guste','children')
        
    def __init__(self, *args, **kwargs):
        self.room = kwargs.pop("room")
        super().__init__(*args, **kwargs)
    
    def clean_data_from(self):
        data_from = self.cleaned_data['data_from']
        
        if Room_Reservation.objects.is_active().filter(data_from=data_from,room=self.room).exists():
            raise forms.ValidationError('This date is already booked')
        if data_from < timezone.now().date():
            raise forms.ValidationError('Enter a valid date')
        return data_from
    
    def clean_data_to(self):
        data_to = self.cleaned_data['data_to']   
        if Room_Reservation.objects.is_active().filter(data_to=data_to,room=self.room).exists():
            raise forms.ValidationError('This date is already booked')
        if data_to < self.cleaned_data['data_from']:
            raise forms.ValidationError('Enter a valid date')
        return data_to


class RoomForm(forms.ModelForm):
    title = forms.CharField(max_length=30)
    price = forms.IntegerField()
    locality = forms.CharField(max_length=60)
    street = forms.CharField(max_length=60)
    descriptions = RichTextField()
    img = forms.ImageField()
    days_number = forms.IntegerField(max_value=60)
    class Meta:
        model = Room
        fields = ('title','price','city','locality','street','descriptions','days_number','img')


RoomImgInlineForm = inlineformset_factory(Room,Room_image,fields=('img',),extra=3,max_num=3,can_delete=False)

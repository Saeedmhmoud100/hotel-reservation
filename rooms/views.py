from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.generic import ListView,DeleteView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.edit import FormMixin
from django_filters.views import FilterView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from random import *
from django.db import transaction
from .models import Room,Room_Rating
from .forms import RoomReservationForm,RoomForm,RoomImgInlineForm

# Create your views here.


def random_rooms(rooms,num=None):
    try:
        x =[p for p in rooms.objects.all()]
    except AttributeError:
        x = rooms   
    if num:
        return list(x[:num])
    return list(x)


def home(request):
    return render(request,'rooms/home.html')

class HotelListView(FilterView):
    template_name = 'rooms/hotel.html'
    model = Room
    paginate_by = 2
    filterset_fields = ['country', 'locality','data_from','data_to','total_rating']
    
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class HotelRoomView(DeleteView,FormMixin):
    template_name = 'rooms/hotel_room.html'
    model = Room
    form_class = RoomReservationForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["user_and_room"] = [self.request.user,self.get_object().pk]
        context["our_rooms"] = random_rooms(Room.objects.all().order_by('?'),3)
        context['related_rooms'] = random_rooms(Room.objects.all().order_by('total_rating'),3)
        return context
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        my_form = form.save(commit=False)
        my_form.user = self.request.user
        my_form.room = self.get_object()
        my_form.email_registered = self.request.user.email
        my_form.price = self.get_object().price
        my_form.save()
        print('yes')
        messages.success(self.request,'Yor are booking successfully!!')
        return super(HotelRoomView, self).form_valid(form)
    
    def form_invalid(self, form):
        print(form.data)
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse('rooms:hotel_room', kwargs={'pk': self.get_object().pk,'slug':self.get_object().slug})

@login_required
def room_rate(request):
    room = request.GET.get('room_id')
    rating = request.GET.get('rating')
    rooms = Room_Rating.objects.filter(room__id=room,user=request.user)
    if rooms.exists():
        message= 'you are alraly rating!!'
        tag = 'warning'
    else:
        Room_Rating.objects.create(rating=rating,user=request.user,room=Room.objects.get(id=room)).save()
        message = 'thanks for your rating'
        tag = 'success'
    return JsonResponse({'message':message,'tag':tag})

class HotelCreateView(UserPassesTestMixin,LoginRequiredMixin,CreateView):
    model = Room
    form_class = RoomForm
    
    def get_context_data(self, **kwargs):
        context = super(HotelCreateView, self).get_context_data(**kwargs)
        context["form2"] = RoomImgInlineForm() 
        return context

    def form_valid(self, form):
        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            form2 = RoomImgInlineForm(self.request.POST,self.request.FILES,instance=self.object)
            if form2.is_valid():
                form2.save()
        return super(HotelCreateView, self).form_valid(form)
        
    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False
class HotelUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'rooms/room_update.html'

    def get_context_data(self, **kwargs):
        context = super(HotelUpdateView, self).get_context_data(**kwargs)
        if self.request.POST: context["form2"] = RoomImgInlineForm(self.request.POST,self.request.FILES,instance=self.object) 
        else:  context["form2"] = RoomImgInlineForm(instance=self.object)
        return context
    
    def form_valid(self, form):
        self.object = form.save()
        form2 = self.get_context_data()['form2']
        if form2.is_valid():
            form2.save()
        return super(HotelUpdateView,self).form_valid(form)
    
    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        return False
    
def tour(request):
    return render(request,'room/tour.html')

def tour_single(request):
    return render(request,'room/tour.html')


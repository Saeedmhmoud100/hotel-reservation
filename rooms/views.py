from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView,DeleteView
from django_filters.views import FilterView
from .models import Room,Room_Rating
# Create your views here.


def home(request):
    return render(request,'room/home.html')

class HotelListView(FilterView):
    template_name = 'room/hotel.html'
    model = Room
    paginate_by = 2
    filterset_fields = ['country', 'locality','data_from','data_to','total_rating']
    
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class HotelRoomView(DeleteView):
    template_name = 'room/hotel_room.html'
    model = Room
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_and_room"] = [self.request.user,self.get_object().pk]
        return context
    

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

def tour(request):
    return render(request,'room/tour.html')

def tour_single(request):
    return render(request,'room/tour.html')


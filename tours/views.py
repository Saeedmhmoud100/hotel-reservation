from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin 
from django_filters.views import FilterView
from django.contrib import messages
from .models import Tour, Place, Tour_Rating, Tour_Reservation
from .forms import TourReservationForm
# Create your views here.

def random_tours(tours,num=None):
    try:
        x =[p for p in tours.objects.all()]
    except AttributeError:
        x = tours   
    if num:
        return list(x[:num])
    return list(x)

class TourListView(FilterView):
    model = Tour
    template_name = 'tours/tour_list.html'
    filterset_fields= ['data_from','data_to','city','locality',]
    paginate_by = 1
    def get_queryset(self):
        return super().get_queryset().filter(active=True)
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['places'] = Place.objects.all()
        return context

class TourDetailView(DetailView,FormMixin):
    model = Tour
    form_class=TourReservationForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'tour': self.object})
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["our_tours"] = random_tours(Tour.objects.all().order_by('?'),3)
        return context
    
    def post(self,request,*args,**kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    def form_valid(self, form):
        my_form = form.save(commit=False)
        my_form.user = self.request.user
        my_form.tour = self.get_object()
        my_form.price = self.get_object().price
        my_form.save()
        messages.success(self.request,'You are booking successfully!!')
        return super(TourDetailView, self).form_valid(form)
    def get_success_url(self):
        return f'{self.get_object().get_absolute_url()}#Reservation_form' 


@login_required
def tour_rate(request):
    tour = request.GET.get('tour_id')
    rating = request.GET.get('rating')
    tours = Tour_Rating.objects.filter(tour__id=tour,user=request.user)
    if not Tour_Reservation.objects.filter(tour=tour,user=request.user,data_to__lte=timezone.now()).exists():
        return JsonResponse({'message':'You have not booked this tour before','tag':'danger'})
    if tours.exists():
        message= 'you are alraly rating!!'
        tag = 'warning'
    else:
        Tour_Rating.objects.create(rating=rating,user=request.user,tour=Tour.objects.get(id=tour)).save()
        message = 'thanks for your rating'
        tag = 'success'
    return JsonResponse({'message':message,'tag':tag})


def tour_single(request):
    return render(request,'tours/tour.html')
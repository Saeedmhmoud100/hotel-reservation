from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin 
from django_filters.views import FilterView
from django.contrib import messages
from .models import Tour, Place
from .forms import TourReservationForm
# Create your views here.

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
def tour_single(request):
    return render(request,'tours/tour.html')
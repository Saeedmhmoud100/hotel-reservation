from django.shortcuts import render
from django_filters.views import FilterView
from .models import Tour, Place
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

def tour_single(request):
    return render(request,'tours/tour.html')
from django.shortcuts import render
from .models import movie
# Create your views here.
def is_valid_queryparam(param):
    return param != '' and param is not None

def BootstrapFilterView(request):
    qs = movie.objects.all()
    title_contains_query = request.GET.get('title_contains')
    
    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(Title__icontains=title_contains_query)
        
    rating_min_query = request.GET.get('rating_min')
    rating_max_query = request.GET.get('rating_max')
    
    if is_valid_queryparam(rating_min_query):
        qs = qs.filter(Rating__gte=rating_min_query )

    if is_valid_queryparam(rating_max_query):
        qs = qs.filter(Rating__lt=rating_max_query)

    year_min_query = request.GET.get('year_min')
    year_max_query = request.GET.get('year_max')

    if is_valid_queryparam(year_min_query):
        qs = qs.filter(Year__gte=year_min_query)

    if is_valid_queryparam(year_max_query):
        qs = qs.filter(Year__lt=year_max_query)

    context = { 
        'queryset' : qs
        }
    return render(request, "bootstrap_form.html", context)
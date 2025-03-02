from django.shortcuts import render
from pages.models import Team
from cars.models import Car

# Create your views here.
def index(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True).order_by('-created_date')
    all_cars = Car.objects.all().order_by('-created_date')
    brand_search = Car.objects.values_list('brand', flat=True).distinct()
    model_search = Car.objects.values_list('model', flat=True).distinct()
    Year_search = Car.objects.values_list('Year', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams':teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'brand_search': brand_search,
        'model_search': model_search,
        'Year_search': Year_search,
        'city_search': city_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/index.html', data)

def about(request):
    
    teams = Team.objects.all()
    data = {
        'teams': teams
    }
    return render(request, 'pages/about.html', data)

def contact(request):
    return render(request, 'pages/contact.html')

def services(request):
    return render(request, 'pages/services.html' )

def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')

def terms_of_use(request):
    return render(request, 'pages/terms_of_use.html')

def data_deletion(request):
    return render(request, 'pages/data_deletion.html')
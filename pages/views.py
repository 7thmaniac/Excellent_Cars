from django.shortcuts import render
from pages.models import Team
from cars.models import Car

# Create your views here.
def index(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.filter(is_featured=True).order_by('-created_date')
    all_cars = Car.objects.all().order_by('-created_date')
    data = {
        'teams':teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
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
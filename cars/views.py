from django.shortcuts import render, get_object_or_404
from cars.models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        'cars': paged_cars,
    }
    return render(request, 'cars/cars.html', data)

def car_details(request,id):
    car = get_object_or_404(Car, pk=id)
    data = {
        'car': car,
    }
    return render(request, 'cars/car_details.html', data)

def search(request):
    cars = Car.objects.all().order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)
        cars = cars.filter(description__icontains=request.GET['keyword'])
    data = {
        'cars': cars,
    }
    return render(request, 'cars/search.html', data)
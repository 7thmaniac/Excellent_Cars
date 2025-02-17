from django.shortcuts import render, get_object_or_404
from cars.models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    
    brand_search = Car.objects.values_list('brand', flat=True).distinct()
    Year_search = Car.objects.values_list('Year', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
            
    data = {
        'cars': paged_cars,
        'brand_search': brand_search,
        'Year_search': Year_search,
        'city_search': city_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
        
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
    brand_search = Car.objects.values_list('brand', flat=True).distinct()
    model_search = Car.objects.values_list('model', flat=True).distinct()
    Year_search = Car.objects.values_list('Year', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)
            
    if 'select-brand' in request.GET:
        keyword = request.GET['select-brand']
        if keyword:
            cars = cars.filter(brand__iexact=keyword)
            
    if 'select-model' in request.GET:
        keyword = request.GET['select-model']
        if keyword:
            cars = cars.filter(model__iexact=keyword)
    
    if 'select-location' in request.GET:
        keyword = request.GET['select-location']
        if keyword:
            cars = cars.filter(city__iexact=keyword)
            
    if 'select-year' in request.GET:
        keyword = request.GET['select-year']
        if keyword:
            cars = cars.filter(Year__iexact=keyword)
            
    if 'select-type' in request.GET:
        keyword = request.GET['select-type']
        if keyword:
            cars = cars.filter(body_style__iexact=keyword)
    
    if 'min_price' in request.GET:
        min_keyword = request.GET['min_price']
        max_keyword = request.GET['max_price']
        if max_keyword:
            cars = cars.filter(price__gte=min_keyword, price__lte=max_keyword)
            
    if 'transmission' in request.GET:
        keyword = request.GET['transmission']
        if keyword:
            cars = cars.filter(transmission__iexact=keyword)
    
    data = {
        'cars': cars,
        'brand_search': brand_search,
        'model_search': model_search,
        'city_search': city_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search,
        'Year_search': Year_search,
        
    }
    return render(request, 'cars/search.html', data)
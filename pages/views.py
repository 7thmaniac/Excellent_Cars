from django.shortcuts import render, redirect
from pages.models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

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
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        subject = request.POST["subject"]
        phone = request.POST["phone"]
        
        
        mail_subject = "You have a  new message from carzone website regarding " + subject
        message_body = "Name: " + name + ".\n" + "Email: " + email + ".\n" + "Phone: " + phone + ".\n" + "Message: " + message + ".\n"
        
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        
        send_mail(
                    mail_subject,
                    message_body,
                    "sasankvaranasi7@gmail.com",
                    [admin_email],
                    fail_silently=False,
                )
        messages.success(request, 'Your request has been submitted, we will get back to you shortly!')
        return redirect('contact')
    return render(request, 'pages/contact.html')

def services(request):
    return render(request, 'pages/services.html' )

def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html')

def terms_of_use(request):
    return render(request, 'pages/terms_of_use.html')

def data_deletion(request):
    return render(request, 'pages/data_deletion.html')
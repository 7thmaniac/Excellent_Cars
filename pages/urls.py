from django.urls import path,include
from pages import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),
    path('terms-of-use', views.terms_of_use, name='terms_of_use'),
    path('data-deletion', views.data_deletion, name='data_deletion'),
]
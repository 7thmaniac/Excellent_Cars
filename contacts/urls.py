from django.urls import path, include
from contacts import views

urlpatterns = [
    path('inquiry', views.inquiry, name="inquiry"),
]
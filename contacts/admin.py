from django.contrib import admin
from contacts.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'car_title', 'city', 'created_date')
    list_display_links = ('id', 'first_name', 'last_name', 'email', 'city')
    search_fields = ('id', 'first_name', 'last_name', 'car_title')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
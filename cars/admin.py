from django.contrib import admin
from cars.models import Car
from django.utils.html import format_html 

# Register your models here.
class CarsAdmin(admin.ModelAdmin):
    def thumbnails(self, object):
        return format_html("<img src='{}' width='40' style='border-radius: 50px'/>".format(object.car_photo.url))
                           
    list_display = ('id', 'thumbnails', 'car_title', 'price', 'city', 'body_style','is_featured',)
    list_display_links = ('id', 'thumbnails', 'car_title',)
    search_fields = ('car_title', 'fuel_type', 'body_style', 'color', 'city', 'Year',)
    list_filter = ('price', 'city', 'body_style', 'color', 'fuel_type', 'Year',)
    list_editable = ('is_featured',)
admin.site.register(Car, CarsAdmin)
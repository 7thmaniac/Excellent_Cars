from django.contrib import admin
from pages.models import Team
from django.utils.html import format_html

# Register your models here.

class Teamadmin(admin.ModelAdmin):
    def thumbnails(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px"/>'.format(object.photo.url))
    
    thumbnails.short_description = "photo"
    list_display = ('id', 'thumbnails', 'first_name', 'designation', 'created_date')
    list_display_links = ('id', 'thumbnails', 'first_name')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation',)

admin.site.register(Team, Teamadmin)

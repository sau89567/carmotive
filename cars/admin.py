from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def images(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.car_photo.url))
        
    list_display = ('images', 'car_title', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured', 'city')
    list_display_links = ('car_title', 'images')
    list_editable = ('is_featured',)
    search_fields = ('car_title', 'city', 'model', 'year', 'fuel_type')
    list_filter = ('city', 'model')

admin.site.register(Car, CarAdmin )

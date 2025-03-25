from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def images(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.photo.url))
        
        
    list_display = ('id','images','first_name', 'last_name' , 'designation','created_date')
    list_display_links = ('id','first_name','last_name','images')
    search_fields = ('first_name','id','designation')
    list_filter = ('designation',)
    
admin.site.register(Team, TeamAdmin)
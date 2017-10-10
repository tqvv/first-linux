from django.contrib import admin

# Register your models here.
from .models import *

class StreamAdmin(admin.ModelAdmin):
    list_display = ('name','head_img','price','play')
    list_editable = ('head_img','price','play')

admin.site.register(Stream,StreamAdmin)

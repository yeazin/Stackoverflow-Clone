from django.contrib import admin
from .models import Quser


class QuserAdmin(admin.ModelAdmin):
    
    list_display = ['email','user']
    ordering = ['-created_at']
    #search_fields = ('email')
admin.site.register(Quser,QuserAdmin)

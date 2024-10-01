from django.contrib import admin
from .models import Doctors, Direction

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'sort_order')
    search_fields = ('title',)
    ordering = ('sort_order',)
    
@admin.register(Doctors)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience', 'sort_order')
    list_filter = ('directions', 'experience')
    search_fields = ('name', 'description')
    ordering = ('sort_order', 'name')
    filter_horizontal = ('directions',)
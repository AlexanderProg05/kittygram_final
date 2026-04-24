from django.contrib import admin
from .models import Cat, Achievement

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'birth_year', 'owner')
    search_fields = ('name', 'owner__username')
    list_filter = ('color', 'birth_year')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name',)

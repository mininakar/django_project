from django.contrib import admin
from core import models
@admin.register(models.Book)
class Book (admin.ModelAdmin):
    list_display = ('id',)

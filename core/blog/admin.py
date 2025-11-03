from django.contrib import admin
from .models import Post , Category
# Register your models here.

@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display = ['author' , 'title' , 'status' , 'category' , 'created_date' , 'published_date']

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['name']
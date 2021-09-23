from django.contrib import admin

# Register your models here.
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_id','blog_image', 'blog_title','blog_sub_title','blog_status')

admin.site.register(Blog,BlogAdmin)

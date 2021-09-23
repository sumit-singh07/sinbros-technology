from django.contrib import admin

# Register your models here.
from .models import Learn

class LearnAdmin(admin.ModelAdmin):
    list_display = ('learn_id','learn_image', 'learn_title','learn_sub_title','learn_status')

admin.site.register(Learn,LearnAdmin)

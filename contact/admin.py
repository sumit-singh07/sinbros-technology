from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_id', 'contact_name', 'contact_mobile','contact_email','contact_status')

admin.site.register(Contact,ContactAdmin)

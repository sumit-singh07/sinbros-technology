from django.contrib import admin

# Register your models here.
from .models import Portfolio

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('portfolio_id','portfolio_image', 'portfolio_title','portfolio_category','portfolio_status')

admin.site.register(Portfolio,PortfolioAdmin)

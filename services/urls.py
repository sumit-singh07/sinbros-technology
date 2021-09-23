from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='WebDevelopment'),
    path('web-development', views.index, name='WebDevelopment'),
    path('mobile-application', views.mobile_application, name='MobileApplication'),
    path('desktop-application', views.desktop_application, name='DesktopApplication'),
    path('digital-marketing', views.digital_marketing, name='DigitalMarketing'),
]
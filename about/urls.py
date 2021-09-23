from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='AboutUs'),
    path('about-us/', views.index, name='AboutUs'),

    path('our-experts/', views.our_experts, name='OurExperts'),
    path('our-experts/sumit-singh', views.sumit_singh, name='SumitSingh'),
    path('our-experts/aman-singh', views.aman_singh, name='AmanSingh'),
    path('our-experts/chandani-singh', views.chandani_singh, name='Chandani_Singh'),

    path('vision-mission-values/', views.vision_mission_values, name='VisionMissionValues'),

]
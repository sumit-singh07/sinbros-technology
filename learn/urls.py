from django.urls import path
from . import views

urlpatterns = [
    path('', views.competitive_programming, name='AboutUs'),
    path('python/', views.python, name='Python'),
    path('face-detection-using-opencv-python/', views.face_detection, name='FaceDetection'),

    path('competitive-programming/', views.competitive_programming, name='CompetitiveProgramming'),
    path('basic-programming/', views.basic_programming, name='BasicProgramming'),
    path('pattern-programs/', views.pattern_programs, name='PatternPrograms'),
    path('<learn_url>/', views.view_competitive_programming, name='ViewCompetitiveProgramming'),

]
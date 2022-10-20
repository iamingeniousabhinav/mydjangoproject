from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('campus_view/', views.campus_view, name='campus_view'),
    path('noticeboard/', views.noticeboard, name='noticeboard'),
    path('calculator/', views.calculator, name='calculator'),
    path('weather_report/', views.weather_report, name='weather_report'),
]
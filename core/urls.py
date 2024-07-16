from django.urls import path
# from . views import *
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('courses', views.courses, name='courses'),
    path('contact', views.contact, name='contact'),
    path('detail/<int:course_id>/', views.detail, name='detail'),
    path('feature', views.feature, name='feature'),
    path('joinus', views.joinus, name='joinus'),
    path('team', views.team, name='team'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('search/', views.search, name='search'),
]
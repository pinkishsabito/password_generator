from django.urls import path

from generator import views


urlpatterns = [
    path('', views.password, name='password'),
    path('about/', views.about, name='about'),
    path('generate/', views.generate, name='generate'),
    path('last_generated/', views.last_generated, name='last_generated')
]

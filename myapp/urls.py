from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('like/', views.like_image, name='like_image'),
    
]

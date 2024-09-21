from django.urls import path
from . import views

urlpatterns = [
    path('view-images/', views.view_images, name='view_images'),
]


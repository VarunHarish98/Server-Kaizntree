from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add/', views.add_data),
    path('show/', views.get_data)
]
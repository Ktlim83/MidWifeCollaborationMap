from django.urls import path
from . import views


urlpatterns = [
    
   path('', views.map_dashboard, name="map_dashboard"), 
   
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('simulation', views.simulation, name='simulation'),
    path('generate-map', views.generate_map, name='generate-map')
]

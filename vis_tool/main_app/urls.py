from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('static-map-form', views.static_map_form, name='static-map-form'),
    path('video-generation-form', views.video_generation_form, name='video-generation-form'),
    path('static-map-generation', views.static_map_generation, name='static-map-generation'),
    path('simulation-video-generation', views.simulation_video_generation, name='simulation-video-generation'),
]

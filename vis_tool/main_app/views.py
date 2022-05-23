from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib import messages
from .scripts.populations_visualization import start_plot_process
from .scripts.simulation import generate_video
from .forms import StaticMapForm, VideoGenerationForm
from .scripts.utils import *
import os
import shutil

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def static_map_form(request):
    context = {}
    context['form'] = StaticMapForm()
    return render(request, 'static_map_form.html', context)

def video_generation_form(request):
    context = {}
    context['form'] = VideoGenerationForm()
    return render(request, 'video_generation_form.html', context)

def static_map_generation(request):
    if request.method == 'POST':
        form = request.POST
        save_folder_files(request.FILES.getlist('map_shape'), settings.MEDIA_ROOT + '/files/shapefile/')
        save_file(settings.MEDIA_ROOT + '/files/populations.csv', request.FILES['populations_file'])
        save_file(settings.MEDIA_ROOT + '/files/clusters.bz', request.FILES['clusters_file'])
        start_plot_process(form)
        shutil.rmtree(settings.MEDIA_ROOT + '/files/') 

    return HttpResponseRedirect('static-map-form')

def simulation_video_generation(request):
    if request.method == 'POST':
        form = request.POST
        save_folder_files(request.FILES.getlist('map_shape'), settings.MEDIA_ROOT + '/files/shapefile/')
        save_file(settings.MEDIA_ROOT + '/files/populations.csv', request.FILES['populations_file'])
        save_file(settings.MEDIA_ROOT + '/files/clusters.bz', request.FILES['clusters_file'])
        save_folder_files(request.FILES.getlist('sim_files'), settings.MEDIA_ROOT + '/files/sim/')
        generate_video(form)
        shutil.rmtree(settings.MEDIA_ROOT + '/files/') 

        messages.success(request, settings.MEDIA_ROOT + '/output.mp4')

    return HttpResponseRedirect('video-generation-form')

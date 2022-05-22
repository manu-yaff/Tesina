from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
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

        shapefile_folder = request.FILES.getlist('map_shape')
        shape_file_path = settings.MEDIA_ROOT + '/files/shapefile/'

        for file in shapefile_folder:
            save_file(shape_file_path + file.name, file)

        populations_file = request.FILES['populations_file']
        clusters_file = request.FILES['clusters_file']

        save_file(settings.MEDIA_ROOT + '/files/populations.csv', populations_file)
        save_file(settings.MEDIA_ROOT + '/files/clusters.bz', clusters_file)

        start_plot_process(form)

        shutil.rmtree(settings.MEDIA_ROOT + '/files/') 

    return HttpResponseRedirect('static-map-form')

def simulation_video_generation(request):
    if request.method == 'POST':
        form = request.POST

        shape_file_folder = request.FILES.getlist('map_shape')
        shape_file_path = settings.MEDIA_ROOT + '/files/shapefile/'

        for file in shape_file_folder:
            save_file(shape_file_path + file.name, file)

        simulation_folder = request.FILES.getlist('sim_files')
        simulation_path = settings.MEDIA_ROOT + '/files/sim/'
        for file in simulation_folder:
            save_file(simulation_path + file.name, file)

        populations_file = request.FILES['populations_file']
        clusters_file = request.FILES['clusters_file']

        save_file(settings.MEDIA_ROOT + '/files/populations.csv', populations_file)
        save_file(settings.MEDIA_ROOT + '/files/clusters.bz', clusters_file)

        generate_video(form)

        shutil.rmtree(settings.MEDIA_ROOT + '/files/') 

    return HttpResponseRedirect('video-generation-form')


# def simulation(request):
#     populations_file = request.FILES['populations_file']
#     populations_file_location = settings.MEDIA_ROOT + '/' + populations_file.name

#     clusters_file = request.FILES['clusters_file']
#     clusters_file_location = settings.MEDIA_ROOT + '/' + clusters_file.name

#     fs.save('populations.csv', populations_file)
#     fs.save('clusters.bz', clusters_file)

#     shapefile_folder = request.FILES.getlist('test')
#     fs = FileSystemStorage()
#     for file in shapefile_folder:
#         fs.save(settings.MEDIA_ROOT + '/shapefile/' + file.name, file)

    # sim_folder = request.FILES.getlist('simFiles')
    # for file in sim_folder:
    #     fs.save(settings.MEDIA_ROOT + '/sim/' + file.name, file)

#     generate_video(request.POST)
#     return HttpResponse('Aqui se llama el script')


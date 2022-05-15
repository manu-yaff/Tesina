from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .scripts.populations_visualization import something
from .forms import VisualizationForm
import os

# Create your views here.
def home(request):
    context = {}
    context['form'] = VisualizationForm()
    return render(request, 'home.html', context)

def generate_map(request):
    if request.method == 'POST':
        form = request.POST

        populations_file = request.FILES['populations_file']
        populations_file_location = settings.MEDIA_ROOT + '/' + populations_file.name

        clusters_file = request.FILES['clusters_file']
        clusters_file_location = settings.MEDIA_ROOT + '/' + clusters_file.name

        if(os.path.exists(populations_file_location)):
            os.remove(populations_file_location)

        if(os.path.exists(clusters_file_location)):
            os.remove(clusters_file_location)


        fs = FileSystemStorage()

        fs.save('populations.csv', populations_file)
        fs.save('clusters.bz', clusters_file)

        something(form)
    return HttpResponse('Aqui se genera el mapa con los parametros')

def simulation(request):
    # generate_video()
    return HttpResponse('Aqui se llama el script')

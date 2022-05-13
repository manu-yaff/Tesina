from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import VisualizationForm
from django.conf import settings
import os

# Create your views here.
def home(request):
    context = {}
    context['form'] = VisualizationForm()
    return render(request, 'home.html', context)

def generate_map(request):
    if request.method == 'POST':
        form = request.POST
        file = request.FILES['populations_file']
        file_location = settings.MEDIA_ROOT + '/' + file.name
        print('este es el path')
        print(file_location)
        if(os.path.exists(file_location)):
            os.remove(file_location)
        fs = FileSystemStorage()
        fs.save(file.name, file)
        # plot_graph(form)
    return HttpResponse('Aqui se genera el mapa con los parametros')

def simulation(request):
    # generate_video()
    return HttpResponse('Aqui se llama el script')

from .utils import *
from pyproj import CRS
from shapely.geometry import Point, Polygon
from django.conf import settings
import os
import time
import multiprocessing as mp
import math
import subprocess
import matplotlib.pyplot as plt



shape_file = settings.MEDIA_ROOT + '/shapefile/stp_gc_adg.shp'
populations_file = settings.MEDIA_ROOT + '/populations.csv'
clusters_file = settings.MEDIA_ROOT + '/clusters.bz'
FRAMES_FOLDER = settings.MEDIA_ROOT + "/frames"
GENERATED_FRAMES = settings.MEDIA_ROOT + "/frames/"
SIM_URL = settings.MEDIA_ROOT + "/sim/E_0025000000_03_0000000000_0000000000_0000000000-HLT_0"
FILE_TYPE = "_sum.bz"
crs = CRS('EPSG:4326')



def generate_frames(i, n, visualization_config, geo_centroids, map_shape):
    first = hex_to_rgb(visualization_config['clusters_color'][1:])
    second = hex_to_rgb(visualization_config['populations_color'][1:])

    fig, ax = plt.subplots(figsize=(15, 15))
    time_text = ax.text(7.2, 0.1, '0', fontsize=20)
    aux = "000"

    map_shape.plot(ax=ax, alpha=0.4, figsize=(20, 15),
                   edgecolor="gray", facecolor="white")
    for i in range(i, n):
        if (i > 9 and i < 100):
            aux = "00"
        elif (i > 99 and i < 1000):
            aux = "0"
        elif (i > 999):
            aux = ""
        name = "frame" + aux + str(i) + ".jpg"
        if (not os.path.exists(GENERATED_FRAMES + name)):
            s = [math.log2(geo_centroids.iloc[n].propP[i]) *
                 20 for n in range(len(geo_centroids))]
            colorsH = [[first[0], first[1], first[2], geo_centroids.iloc[n].propH[i]]
                       for n in range(len(geo_centroids))]
            colorsO = [[second[0], second[1], second[2], geo_centroids.iloc[n].propO[i]]
                       for n in range(len(geo_centroids))]

            geo_centroids.plot(ax=ax, markersize=s, c=colorsH,
                               marker='H', label="Cluster")
            geo_centroids.plot(ax=ax, markersize=s, c=colorsO,
                               marker='H', label="Cluster")
            time_text.set_text('Day: ' + str(i+1))

            fig.savefig(GENERATED_FRAMES + name)

def generate_video(visualization_config):
    map_shape = read_map_shape_file(shape_file)
    populations = read_populations_file(populations_file)
    clusters = read_clusters_file(clusters_file)

    centroids = []
    coords = []
    file = 0
    id = 0
    aux = 0

    for cluster in clusters:
        clusterProportion = None
        content = None
        if (file < 10):
            numFile = "0" + str(file)
        else:
            numFile = str(file)
        with bz2.open(SIM_URL + numFile + FILE_TYPE, "rb") as f:
            content = f.read()

        clusterProportion = cPickle.loads(content)
        file += 1
        aux += 1

        # number of days in the simulation
        days = len(clusterProportion.get("population"))
        # print('days in cluster proportion: ', days)

        arrH = []
        arrO = []
        arrP = []
        propH = 0
        propO = 0
        propP = 0

        for i in range(days):
            propH = round(clusterProportion.get('population')[
                          i][0] / clusterProportion.get('population')[i][2], 2)
            propO = round(clusterProportion.get('population')[
                          i][1] / clusterProportion.get('population')[i][2], 2)
            propP = round(clusterProportion.get('population')[i][2], 2)

            arrH.append(propH)
            arrO.append(propO)
            arrP.append(propP)

        acumLon = 0
        acumLat = 0
        pop = 0
        for population in cluster:
            point = populations.iloc[population]
            acumLon += point.lon
            acumLat += point.lat
            pop += point["pop"]

        centroidLon = acumLon/len(cluster)
        centroidLat = acumLat/len(cluster)
        coord = [id, centroidLon, centroidLat, pop, arrH, arrO, arrP]

        geoPoint = Point(centroidLon, centroidLat)

        centroids.append(geoPoint)
        coords.append(coord)
        id += 1

    columns = ["id", "lon", "lat", "popul", "propH", "propO", "propP"]
    df = pd.DataFrame(data=coords, columns=columns)
    geo_centroids = gpd.GeoDataFrame(df, crs=crs, geometry=centroids)


    # PLOT ANIMATION MAP OF CLUSTERS
    if (not os.path.exists(FRAMES_FOLDER)):
        os.makedirs(FRAMES_FOLDER)

    start = time.time()
    processes = []
    num_workers = mp.cpu_count()
    step = math.ceil(300 / num_workers)

    upper_limit = 0
    for i in range(num_workers):
        lower_limit = upper_limit
        upper_limit = lower_limit + step
        if (upper_limit > days):
            upper_limit = days
        processes.append(mp.Process(target=generate_frames,
                         args=(lower_limit, upper_limit, visualization_config, geo_centroids, map_shape)))

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    subprocess.call('ffmpeg -framerate 25 -i ' +
                    GENERATED_FRAMES + 'frame%04d.jpg ' + settings.MEDIA_ROOT + '/output.mp4', shell=True)
    subprocess.Popen('open ' + settings.MEDIA_ROOT + '/output.mp4', shell=True)
    end = time.time()
    print('*****************************************')
    print('execution time: ', end - start)

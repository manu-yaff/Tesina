from .utils import *
import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import bz2
import _pickle as cPickle
import multiprocessing as mp
from shapely.geometry import Point, Polygon
from pyproj import CRS
from django.conf import settings

def generate_geo_populations_data_frame(populations, crs):
    """
    This function makes a geoDataFrame from a given populations dataFrame

    :param populations: the populations dataFrame
    :param crs: specifies the the Coordinate Reference System
    :return: geoDataFrame,  
    """
    points = [Point(xy) for xy in zip(populations["lon"], populations["lat"])]
    return gpd.GeoDataFrame(populations, crs=crs, geometry=points)

def generate_centroids(clusters, populations):
    """
    This function genrates the centroids and their coordinates

    :param clusters: clusters array
    :param populations: the populations dataFrame
    :return: centroids points and their coordinates
    """
    centroids = []
    coordinates = []
    centroid_id = 0

    for cluster in clusters:
        accumLongitude = 0
        accumLatitude = 0
        population = 0

        for population in cluster:
            point = populations.iloc[population]
            accumLongitude += point.lon
            accumLatitude += point.lat
            population += point["pop"]

        centroidLongitude = accumLongitude / len(cluster)
        centroidLatitude = accumLatitude / len(cluster)
        coordinate = [centroid_id, centroidLongitude, centroidLatitude, population]
        point = Point(centroidLongitude, centroidLatitude)
        centroids.append(point)
        coordinates.append(coordinate)
        centroid_id += 1

    return [centroids, coordinates]

def generate_geo_centroids_data_frame(centroids, coordinates):
    """
    This function creates a geoDataFrame with the clusters centroids

    :param centroids: array of Point objects
    :param coordinates: array of centroids coordinates
    :return: centroids geoDataFrame
    """
    columns = ['id', 'lon', 'lat', 'population']
    df = pd.DataFrame(data=coordinates, columns=columns)
    return gpd.GeoDataFrame(df, crs=crs, geometry=centroids)

def generate_plot(map_shape, geo_populations, populations, centroids, geo_centroids, visualization_config):
    """
    This function builds and shows the plot

    :param map_shape: map shape object
    :param geo_populations: geo populations data frame
    :param populations: populations data frame
    :param centroids: centroids points and their coordinates
    """
    fig, ax = plt.subplots(figsize=(
            int(visualization_config['bounding_box_width']),
            int(visualization_config['bounding_box_height'])
        )
    )
    map_shape.plot(
            ax=ax,
            alpha=0.4,
            figsize=(20, 15),
            edgecolor=visualization_config['map_shape_edge_color'],
            facecolor=visualization_config['map_shape_face_color']
    )
    geo_populations.plot(
            ax=ax,
            markersize=20,
            color=visualization_config['populations_color'],
            marker="o",
            label="Population"
    )
    pointLabel = 0
    for i in range(len(populations)):
        point = populations.iloc[i]
        plt.text(point["lon"], point["lat"], str(pointLabel), color=(0.4, 0.2, 0.5, 0.2), fontsize=6)
        pointLabel += 1

    geo_centroids.plot(
            ax=ax,
            markersize=60,
            color=visualization_config['clusters_color'],
            marker="X",
            label="Cluster"
    )

    for coordinate in centroids[1]:
        plt.text(coordinate[1], coordinate[2], coordinate[0], color="black", fontsize=8)

    plt.legend(prop={'size': 10}, loc="upper left")
    plt.show()

# temp variables
shape_file = settings.MEDIA_ROOT + '/shapefile/stp_gc_adg.shp'
populations_file = settings.MEDIA_ROOT + '/populations.csv'
clusters_file = settings.MEDIA_ROOT + '/clusters.bz'
crs = CRS('EPSG:4326')

def main(visualization_config):
    print('llego hasta el script')
    print(visualization_config)
    map_shape = read_map_shape_file(shape_file)
    populations = read_populations_file(populations_file)
    clusters = read_clusters_file(clusters_file)
    geo_populations = generate_geo_populations_data_frame(populations, crs)
    centroids = generate_centroids(clusters, populations)
    geo_centroids = generate_geo_centroids_data_frame(centroids[0], centroids[1])
    generate_plot(map_shape, geo_populations, populations, centroids, geo_centroids, visualization_config)

def start_plot_process(visualization_config):
    process = mp.Process(target = main, args = (visualization_config, ))
    process.start()
    process.join()







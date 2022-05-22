import geopandas as gpd
import pandas as pd
import bz2
import _pickle as cPickle
from django.core.files.storage import FileSystemStorage
from django.conf import settings


def read_map_shape_file(file):
    """
    This function reads a shapefile (.shp)

    :param file: path of the shape file to read
    :return: geoDataFrame object
    """
    return gpd.read_file(file)

def read_populations_file(file):
    """
    This function reads the populations file (.csv)

    :param file: path of the populations file
    :return: DataFrame object
    """
    return pd.read_csv(file)

def read_clusters_file(file):
    """
    This function reads the clusters file (.bz)

    :param file: path of the clusters file
    :return: array of arrays describing which populations belong to which cluster
    """
    with bz2.open(file, "rb") as f:
        content = f.read()
    return cPickle.loads(content)

def save_file(path, file):
    """
    This function saves a file in the file system storage

    :param filename: the file object to be saved
    :param file: the file object to be saved
    :return: True if the file was saved successfully
    """
    fs = FileSystemStorage()
    return fs.save(path, file)


def hex_to_rgb(hex):
    """
    This function converts a hex color to its value in rgb
    
    :param hex: hex color
    :return: array with the rgb value
    """
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex[i:i+2], 16)
        rgb.append(decimal/255)

    return rgb



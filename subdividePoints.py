# Randomly subdivide points into multiple shapefiles

import numpy as np
import random
root = "E:\\OneDrive - University Of Cambridge\\Project\\london-pois-data\\analysis\\1_geoprocess_QGIS"
infn = root + ".\\shapefiles\\random_points_os_road_400000_20.shp"

layer = iface.addVectorLayer(infn, '', 'ogr')
seed = 0

for i in range(4):
    print(i)
    np.random.seed(seed)
    random_list = tuple(np.random.choice(400000, size=100000, replace=False))
    layer.selectByExpression('"id" IN {}'.format(
        random_list), QgsVectorLayer.SetSelection)
    selection = layer.selectedFeatures()
    outfn = root + \
        ".\\shapefiles\\random_points_os_road_400000_20_r{}.shp".format(i)
    writer = QgsVectorFileWriter.writeAsVectorFormat(
        layer, outfn, 'utf-8', driverName='ESRI Shapefile', onlySelectedFeatures=True)
    layer.removeSelection()
    seed += 1
del(writer)

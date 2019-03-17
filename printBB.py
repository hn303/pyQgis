# Print the boundary of selected feature
# Instruction: first excute this script in the python console in QGIS
# Then, select the feature before calling the function by type printBB()


def printBB():
    feature = iface.activeLayer().selectedFeatures()[0]
    print feature.geometry().boundingBox().toString()

import shapefile
import numpy as np
import sys

# Shapefile
sf = shapefile.Reader(sys.argv[0])
shapes = sf.shapes()
#shapeRecs = sf.shapeRecords()
#shapeRec = sf.shapeRecord(3)
#points = shapeRecs[3].shape.points[0:2]
print(shapes)


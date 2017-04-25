#!/usr/bin/env python2.7
from osgeo import ogr
geom = ogr.CreateGeometryFromWkt('point(0 0)')
assert str(geom) == 'POINT (0 0)'

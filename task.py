#!/usr/bin/env python2.7
from __future__ import print_function
from osgeo import ogr

def main(*args):
    geom = ogr.CreateGeometryFromWkt('point(0 0)')
    print('geom:', geom)

if __name__ == '__main__':
    exit(main())

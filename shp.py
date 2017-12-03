#!/usr/bin/env python3

import csv
import sys

# https://anaconda.org/pelson/pyshp
import shapefile

def shp(filename):
    sf = shapefile.Reader(filename)
    print(sf.shapeType)
    shapes = sf.shapes()
    print(len(shapes), "shapes")
    for i,shape in enumerate(shapes):
        yield from flat_shape(i, shape)

def flat_shape(shape_index, shape):
    parts = set(shape.parts) - set([0])
    part = 0
    i = 0
    for point in shape.points:
        if i in parts:
            part += 1
            i = 0
        yield (shape_index, part, i) + point
        i += 1

def main(argv=None):
    if argv is None:
        argv = sys.argv

    arg = argv[1:]

    with open('output.csv', 'w', newline='') as outfile:
        points = csv.writer(outfile)
        for row in shp(arg[0]):
            points.writerow(row)


if __name__ == '__main__':
    main()

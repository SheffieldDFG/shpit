#!/usr/bin/env python3

import csv
import re
import sys

# https://anaconda.org/pelson/pyshp
import shapefile

def shapefile_tuples(filename):
    sf = shapefile.Reader(filename)

    fields = sf.fields[1:]
    fieldnames = [f[0] for f in fields]
    yield ["shp_s", "shp_p", "shp_i", "x", "y"] + fieldnames

    srs = sf.shapeRecords()
    print(len(srs), "shapes")
    for i,sr in enumerate(srs):
        for row in flat_shape(i, sr.shape):
            yield row + tuple(sr.record)

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

    as_csv(arg[0])

def as_csv(input_name):
    output_name = re.sub(r'\.[^.]*$|$', '.csv', input_name)
    if output_name == input_name:
        raise Exception("Can't write output over input")

    with open(output_name, 'w', newline='') as outfile:
        points = csv.writer(outfile)
        for row in shapefile_tuples(input_name):
            points.writerow(row)


if __name__ == '__main__':
    main()

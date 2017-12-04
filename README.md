# shpit

`shp.py` is a program to convert from shapefile to a flat CSV format.

## Installing

I hope you have `conda`.

Create a conda env with `conda create --name shpit` or similar.

Then install the required dependencies with

    conda install --file requirements.txt

or, if you prefer, `pip install -r requirements.txt`.

## Running

    python3 shp.py inputfile.shp

The name of the CSV output file is the same as the input,
with its extension replaced with `.csv`.

## CSV format

Each row in the output CSV file is a single point.

The first 3 columns of the CSV file
are the shape-, part-, and point-index of the polygons.
Each part is a ring shaped polygon formed by the points of that part.
A shape may have multiple parts when either
it is disjoint (a land plus islands, exclaves, bowties) or
it is doughnut shaped and contains a hole.

The next 2 columns are the coordinates of the point,
which I have labelled `x` and `y`.
You'll have to guess which coordinate system is being used.

The remaining columns are fields from the records in the shapefile;
they are repeated for each point in the shape.

## Source

https://github.com/SheffieldDFG/shpit

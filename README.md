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

## Source

https://github.com/SheffieldDFG/shpit

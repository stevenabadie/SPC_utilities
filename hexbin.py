from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, LabelSet, HoverTool, WheelZoomTool
from bokeh.models.widgets import DataTable, TableColumn
from bokeh.io import output_file, show
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin

import numpy as np
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('csv_file', type=str)

# Read csv with Pandas and assign as ColumnDataSource type
df = pd.read_csv(parser.parse_args().csv_file)

# Establish column name and label variables
title = df.at[0, 'Config']
x_axis = df.at[1, 'Config']
y_axis_one = df.at[2, 'Config']
x_label = df.at[8, 'Config']
y_label = df.at[9, 'Config']

source = ColumnDataSource(df)
output_file(df.at[0, 'Config'] + ".html")

#Plotting the hex graph
#n = 50000
#x = np.random.standard_normal(n)
#y = np.random.standard_normal(n)

bins = hexbin(x_axis, y_axis_one, 0.01)

p = figure(title="Manual hex bin for 50000 points", tools="wheel_zoom,pan,reset",
           match_aspect=True, background_fill_color='#440154')
p.grid.visible = False

p.hex_tile(q="q", r="r", size=0.1, line_color=None, source=bins,
           fill_color=linear_cmap('counts', 'Viridis256', 0, max(bins.counts)))

output_file("hex_tile.html")

show(p)

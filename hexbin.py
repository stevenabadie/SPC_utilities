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

x=df[x_axis].values
y=df[y_axis_one].values

p = figure(title=title + " - Histogram", match_aspect=True,
           tools="wheel_zoom,reset", background_fill_color='#440154')
p.grid.visible = False

r, bins = p.hexbin(x, y, size=0.01, hover_color="pink", hover_alpha=0.8)

p.circle(x, y, color="white", size=1)

p.add_tools(HoverTool(
    tooltips=[("count", "@c"), ("(q,r)", "(@q, @r)")],
    mode="mouse", point_policy="follow_mouse", renderers=[r]
))

output_file(df.at[0, 'Config'] + ".html")

show(p)

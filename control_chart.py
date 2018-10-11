import sys

from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, LabelSet, HoverTool, WheelZoomTool
from bokeh.models.widgets import DataTable, TableColumn

import pandas as pd
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('csv_file', type=str)

# Read csv with Pandas and assign as ColumnDataSource type
df = pd.read_csv(parser.parse_args().csv_file)

# Establish column name and label variables
title = df.at[0, 'Config']
x_axis = 'index'
y_axis_one = df.at[2, 'Config']
y_axis_two = df.at[3, 'Config']
y_axis_three = df.at[4, 'Config']
y_axis_four = df.at[5, 'Config']
ucl = df.at[6, 'Config']
lcl = df.at[7, 'Config']
x_label = df.at[8, 'Config']
y_label = df.at[9, 'Config']
histogram_column = df.at[10, 'Config']

if not pd.isnull(ucl):
    df[ucl] = df[ucl].apply(lambda x: df.at[0, ucl])
if not pd.isnull(lcl):
    df[lcl] = df[lcl].apply(lambda x: df.at[0, lcl])

source = ColumnDataSource(df)
output_file(df.at[0, 'Config'] + ".html")


# Plot control chart figure
p_control = figure(
    title=title + " - Control Chart",
    toolbar_location="above",
    plot_width=1000, plot_height=400,
    tools="hover"
)

tooltips= []
columns = []

if not pd.isnull(y_axis_one):
    p_control.line(x=x_axis, y=y_axis_one, source=source, line_width=3, color="firebrick", legend=y_axis_one + ' ')
    columns.append(TableColumn(field=y_axis_one, title=y_axis_one))
    tooltips.append((y_axis_one, "@{" + y_axis_one + "}"))

if not pd.isnull(y_axis_two):
    p_control.line(x=x_axis, y=y_axis_two, source=source, line_width=3, color="green", legend=y_axis_two + ' ')
    columns.append(TableColumn(field=y_axis_two, title=y_axis_two))
    tooltips.append((y_axis_two, "@{" + y_axis_two + "}"))

if not pd.isnull(y_axis_three):
    p_control.line(x=x_axis, y=y_axis_three, source=source, line_width=3, color="lightseagreen", legend=y_axis_three + ' ')
    columns.append(TableColumn(field=y_axis_three, title=y_axis_three))
    tooltips.append((y_axis_three, "@{" + y_axis_three + "}"))

if not pd.isnull(y_axis_four):
    p_control.line(x=x_axis, y=y_axis_four, source=source, line_width=3, color="lightskyblue", legend=y_axis_four + ' ')
    columns.append(TableColumn(field=y_axis_four, title=y_axis_four))
    tooltips.append((y_axis_four, "@{" + y_axis_four + "}"))

if not pd.isnull(ucl):
    p_control.line(x=x_axis, y=ucl, source=source, line_width=3, color="orange", legend=ucl + ' ')
    tooltips.append((ucl, "@{" + ucl + "}"))

if not pd.isnull(lcl):
    p_control.line(x=x_axis, y=lcl, source=source, line_width=3, color="yellow", legend=lcl + ' ')
    tooltips.append((lcl, "@{" + lcl + "}"))

# Legend and labels
p_control.legend.location = "top_left"
p_control.xaxis.axis_label = x_label
p_control.yaxis.axis_label = y_label
p_control.hover.tooltips = tooltips


# Plot histogram chart figure
p_histogram = figure(
    title=title + " - Histogram",
    toolbar_location="above",
    plot_width=1000, plot_height=400,
    #tools="hover"
)

measures = list(df[histogram_column])
hist, edges = np.histogram(measures, bins=50, density=True)

p_histogram.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
    fill_color="#036564", line_color="#033649")
#p_histogram.line(y=x_axis, x=ucl, source=source, line_width=3, color="orange", legend=ucl + ' ')
#p_histogram.line(y=x_axis, x=lcl, source=source, line_width=3, color="orange", legend=lcl + ' ')


# Render the plot, save it, open the rendered file
show(column([p_control, p_histogram]))

sys.exit()

from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.models.widgets import DataTable, TableColumn

import numpy as np
import pandas as pd

output_file("control_chart.html")

# Read csv with Panda and assign as ColumnDataSource
df = pd.read_csv('../SPC_data/TP-RD00028_Testing-Data.csv')
source = ColumnDataSource(df)


TOOLTIPS = [
    ("Drag", "$y")
]


# Plot figure
p = figure(
    title="Control Chart",
    toolbar_location="above",
    plot_width=1000, plot_height=400,
    tooltips=TOOLTIPS
)

p.line(x="Sample #", y="Initial drag (N)", source=source, line_width=3, color="firebrick", legend="Initial drag")
p.line(x="Sample #", y="Drag with single installed", source=source, line_width=3, legend="New Drag")
p.line(x="Sample #", y="UCL", source=source, line_width=3, color="orange", legend='/UCL')

p.legend.location = "top_left"
p.xaxis.axis_label = "Samples"
p.yaxis.axis_label = "Drag"

# Data table
columns = [
    TableColumn(field="Sample #", title="Sample #"),
    TableColumn(field="Initial drag (N)", title="Initial drag (N)"),
    TableColumn(field="Drag with single installed", title="Drag with single installed"),
]

data_table = DataTable(source=source, columns=columns, width=800, height=400)

show(column(p, data_table))

import plotly.plotly as py
import plotly.offline as offline
import plotly.graph_objs as go
import plotly.figure_factory as ff

import numpy as np
import pandas as pd

df = pd.read_csv('../SPC_data/TP-RD00028_Testing-Data.csv')

figure = ff.create_table(df)

trace1 = go.Scatter(
                    x=df['Sample #'], y=df['Initial drag (N)'],
                    xaxis='x2', yaxis='y2',
                    mode='lines', name='Initial drag (N)',
                    )

figure['data'].extend(go.Data([trace1]))

offline.plot(figure, filename='sample-data-table')


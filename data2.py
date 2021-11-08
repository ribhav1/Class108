import plotly.figure_factory as ff
import pandas as pd
import csv

file_data = pd.read_csv('data.csv')
dist_plot = ff.create_distplot([file_data['Weight(Pounds)'].tolist()], ['Weight'], show_hist = False)
dist_plot.show()
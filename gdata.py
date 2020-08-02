import numpy as np
import pandas as pd

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin
from bokeh.models import ColumnDataSource

#n = 50000
#x = np.random.standard_normal(n)
#y = np.random.standard_normal(n)
#

df = pd.read_csv("location.csv")
source = ColumnDataSource(df)
print(type(source))
print(df.columns)
print(df.describe())

print(type(df.Latitude))
for i in df.Latitude:
    print(i)
bins = hexbin(x, y, 0.05)

p = figure(title="DC locations", tools="wheel_zoom,pan,reset",
           match_aspect=True, background_fill_color='#440154')
p.grid.visible = False

p.hex_tile(q="q", r="r", size=0.1, line_color=None, source=bins,
           fill_color=linear_cmap('counts', 'Viridis256', 0, max(bins.counts)))

output_file("hex_tile.html")

show(p)

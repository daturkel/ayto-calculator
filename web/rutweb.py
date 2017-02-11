#!/usr/bin/env python

from jinja2 import Template
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource, ColorBar, LinearColorMapper, SingleIntervalTicker
from bokeh.palettes import Plasma as palette
from bokeh.layouts import row, column
from bokeh.embed import components, file_html
from bokeh.resources import CDN
import pickle
import pandas as pd
from math import floor

palette = palette[11]
color_mapper = LinearColorMapper(palette=palette,low=-7.5,high=107.5)
# prepare some data
with open("data.pickle", "rb") as f:
    df = pickle.load(f)
    
# output to static HTML file
output_file("heat.html")

x_range = df["probs"][0].index.tolist()
y_range = df["probs"][0].columns.tolist()

def load_episode(i):
    current = df["probs"][i]
    current.index.name = "Guys"
    current.reset_index(inplace=True)
    current = pd.melt(current, id_vars=["Guys"], var_name=["Girls"], value_name="Percent")
    x = current["Guys"].values
    y = current["Girls"].values
    v = current["Percent"].values
    return {"Guys": x, "Girls": y, "Percent": v}

hover = HoverTool(tooltips=[("Couple","@Guys & @Girls"),("Likelihood", "@Percent%")])

data = []
hm = []

for i, ep in enumerate(df["probs"]):
    data.append(load_episode(i))
    if i == 0:
        title = "Are You The One? Baseline"
    elif i%2 == 1:
        title = "Are You The One? Episode {} Truth Booth".format((i+1)/2)
    else:
        title = "Are You The One? Episode {} Matching Ceremony".format(i/2)
    hm.append(figure(title=title,
        height=600,
        x_range=x_range,
        y_range=y_range,
        tools=[HoverTool(tooltips=[("Couple","@Guys & @Girls"),
                                   ("Likelihood", "@Percent%")])],
        toolbar_location=None,
        min_border=0,
        outline_line_color=None))
    hm[i].axis.axis_line_color = None
    hm[i].axis.major_tick_line_color = None
    hm[i].rect(x='Guys',y='Girls',width=1,height=1,fill_color={'field':'Percent', 'transform':color_mapper},line_color="white",source=ColumnDataSource(data[i]))
    color_bar = ColorBar(color_mapper=color_mapper,location=(0,0),ticker=SingleIntervalTicker(interval=10))
    cb = figure(height=600,width=80,toolbar_location=None,min_border=0,outline_line_color=None)
    cb.add_layout(color_bar,"right")
    hm[i] = row(hm[i],cb)
    
script, divs = components(hm)

with open('temp.jinja', 'r') as f:
    template = Template(f.read())

with open("didthiswork.html","w") as f:
    f.write(template.render(script=script,divs=divs))

#data["Color"] = []
#for v in data["Percent"]:
#    index = int(round(.11*v,0))
#    data["Color"].append(palette[index])

#source = ColumnDataSource(data[-1])

#hm = figure(title='Are You The One?',height=600,x_range=x_range, y_range=y_range,tools=[hover],toolbar_location=None,min_border=0, outline_line_color=None)
#hm.axis.axis_line_color = None
#hm.axis.major_tick_line_color = None
##hm.rect(x='Guys',y='Girls',width=1,height=1,fill_color={'field':'Percent','transform':color_mapper},line_color="white",source=data[-1])

#color_bar = ColorBar(color_mapper=color_mapper,location=(0,0),ticker=SingleIntervalTicker(interval=10))
#cb = figure(height=600,width=80,toolbar_location=None,min_border=0,outline_line_color=None)
#cb.add_layout(color_bar,"right")

# show the results
#show(row(hm,cb))


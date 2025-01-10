
''' Present an interactive function explorer with slider widgets.

Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.

Use the ``bokeh serve`` command to run the example by executing:

    bokeh serve sliders.py

at your command prompt. Then navigate to the URL

    http://localhost:5006/sliders

in your browser.

'''
import numpy as np

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure
import matplotlib.pyplot as plt

# Set up data for fully pre-loaded (no call-back)
N = 30
x = np.linspace(-2, 2, 200)
y = np.array([np.cos(i*np.pi*x) for i in range(1, N+1)])
print(y.shape)
y_sum = np.array([np.sum(y[:i+1, :], axis=0) for i in range(N)])
print(y_sum.shape)

#source = ColumnDataSource(data=dict(x=x, y=y, y_sum=y_sum))


# set up data for callback 
x = np.linspace(-2, 2, 200)
y = np.cos(np.pi*x)
source = ColumnDataSource(data=dict(x=x, y=y))

# Set up plot
plot = figure(height=400, width=400, title="my sine wave",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[-2, 2], y_range=[-30, 30])

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)


# Set up widgets
text = TextInput(title="title", value='Modes')
mod_num = Slider(title="Number of modes", value=1, start=1, end=30, step=1)


# Set up callbacks
def update_title(attrname, old, new):
    plot.title.text = text.value

text.on_change('value', update_title)

def update_data(attrname, old, new):

    # Get the current slider values
    N = mod_num.value


    # Generate the new curve
    x = np.linspace(-2, 2, 200)
    y = np.zeros_like(x)
    for i in range(N):
        y += np.cos((i+1)*np.pi*x)

    source.data = dict(x=x, y=y)

for w in [mod_num]:
    w.on_change('value', update_data)


# Set up layouts and add to document
inputs = column(text, mod_num)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Sliders"

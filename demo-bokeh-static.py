
Amplitude: 1
Frequency: 1
Phase: 0
Offset: 0
import numpy as np

from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import figure, show

x = np.linspace(-2, 2, 200)
y = np.cos(np.pi*x)

source = ColumnDataSource(data=dict(x=x, y=y))

plot = figure(y_range=(-30, 30), width=400, height=400)

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

mode_num = Slider(start=1, end=30, value=1, step=1, title="Number of modes")

callback = CustomJS(args=dict(source=source, mode_num=mode_num),
                    code="""
    const N = mode_num.value

    const x = source.data.x

    var y = Array.from(x, (x) => Math.cos(Math.PI*x))
    for (let i = 2; i < (N+1); i++) {
        const temp_y = Array.from(x, (x) => Math.cos(i*Math.PI*x))
        for (let j = 0; j<y.length; j++) 
        {
         y[j] += temp_y[j]
        }
    }
    source.data = { x, y }
""")

mode_num.js_on_change('value', callback)

show(row(plot, column(mode_num)))
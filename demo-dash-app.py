# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import numpy as np

# Incorporate data

# Initialize the app
app = Dash()

# App layout
app.layout = [
    html.H2(children='Physics visualization'),
    dcc.Slider(1, 30, 1, value=1, marks=None, id='N-slider'),
    html.Div(id='updatemode-output-container', style={'marginTop': 20}),
    dcc.Graph(figure={}, id='plot')
]

# set up data for callback 
x = np.linspace(-2, 2, 300)
y = np.cos(np.pi*x)
source = pd.DataFrame.from_dict(dict(x=x, y=y))
# Add controls to build the interaction
@callback(
    Output(component_id='plot', component_property='figure'),
    Input(component_id='N-slider', component_property='value'))

def update_graph(N):
    # Generate the new curve
    x = np.linspace(-2, 2, 300)
    y = np.zeros_like(x)
    for i in range(N):
        y += np.cos((i+1)*np.pi*x)
    source.y = y
    fig = px.line(source, x='x', y='y', markers=False)
    return fig

@callback(Output('updatemode-output-container', 'children'),
          Input('N-slider', 'value'))
def display_value(value):
    return 'Number of modes: {}'.format(value) 

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


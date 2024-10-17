# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 13:00:39 2024

@author: HP
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__)

server = app.server

df = pd.read_csv('rcgloc1.csv')
# fig = go.Figure(data=go.Scattergeo(
#     lon=df['Lon'],
#     lat=df['Lat'],
#     text=df['Type'],
#     mode='markers',
#     marker_color=df['Col']
# ))

# fig.update_layout(
#     geo_scope='asia'
# )

fig = go.Figure(data=go.Scattergeo(
  lon=df['Lon'],
  lat=df['Lat'],
  text=df['Type'],
  mode='markers',
  marker_color=df['Col']
  ))
fig.update_layout(
     geo_scope='asia')
fig.update_traces(hovertemplate="%{text}<br>Site Type: %{customdata[0]}<br>Lat: %{lat}<br>Lon:%{lon}<br>")
fig.update_layout(hoverlabel=dict(bgcolor="white",font_size=10,font_family="Rockwell"))
fig.update_traces(marker=dict(size=8))
fig.update_traces(textposition='top right',textfont=dict(color='blue',size=11),
                mode='markers+text')
fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
fig.update_layout(legend_title='Site Type')

app.layout = html.Div(children=[
    
    dcc.Graph(
        id='example-map',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

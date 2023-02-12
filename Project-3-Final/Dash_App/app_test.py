#import dependencies

import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import geopandas as gpd
import plotly.graph_objects as go

#Read in data from Cleaned CSVs
country_vessels_grouped = pd.read_csv('country_vessels_grouped.csv')
bubble_data = pd.read_csv('bubble_merged_data.csv')
voyages_data = pd.read_csv('cleaned_voyages_for_map.csv')

#Set up Dash app
app = dash.Dash()

#Specify app layout
app.layout = html.Div(children = [
    html.H1(children = 'Global Fishing Effort Analysis', style ={'text-align': 'center', 'color': 'blue'}),
    html.H2(children = ["Please select a country from the dropdown menu to learn more about:", html.Br(), html.Br(), "1. The vessel types that make up the country's fishing fleet", html.Br(), "2. The ports used by the country's fishing fleet in January 2023"]),
    dcc.Dropdown(id='country-dropdown',
    options=[{'label': i, 'value': i}
    for i in country_vessels_grouped['flag_gfw'].unique()],
    value = 'CHN'),
    dcc.Graph(id='bar-chart'),
    dcc.Graph(id='voyages-map'),
    html.H2(children = "Please select a year from the dropdown menu to visualize total fishing hours by a country's fleet in that year."),
    dcc.Dropdown(['2018', '2019', '2020'], id='year-dropdown', value='2018'),
    dcc.Graph(id='bubble-chart')
])

# Design callback and function for bar graph to analyze fishing fleet by vessel type
@app.callback( 
    Output(component_id = 'bar-chart', component_property = 'figure'),
    Input(component_id = 'country-dropdown', component_property = 'value')
)
def makeBarGraph(selected_country):
    filtered_df = country_vessels_grouped[country_vessels_grouped['flag_gfw'] == selected_country]
    bar_graph = px.bar(filtered_df,
    x = "vessel_class_gfw", y = "mmsi",
    labels = {'mmsi': 'Total Vessels', "vessel_class_gfw": 'Vessel Classes'},
    title = "Country-level Vessel Class Analysis",
    color = 'vessel_class_gfw')

    return bar_graph

# Design callback and function for map visualization of fleet voyages
@app.callback( 
    Output(component_id = 'voyages-map', component_property = 'figure'),
    Input(component_id = 'country-dropdown', component_property = 'value')
)


def makeMap(selected_country):
    mapping_df = voyages_data[voyages_data['flag_gfw'] == selected_country]
    map_vis = px.scatter_geo(mapping_df,
    lat = 'lat_start',
    lon  = 'lon_start',
    labels = {'lat_start': 'Latitude', 'lon_start': 'Longitude'},
    width = 1500,
    height = 800,
    title = "Ports Used by Country's Fishing Fleet (January 2023)"
    
    )

    return map_vis


# Design callback and function for bubble chart for fishing hours per country per year
@app.callback( 
    Output(component_id = 'bubble-chart', component_property = 'figure'),
    Input(component_id = 'year-dropdown', component_property = 'value')

)

def makeBubbleChart(selected_year):
    bubble_df = bubble_data[['flag_gfw', 'total_vessels', f'{selected_year}']]
    bubble_chart = px.scatter(bubble_df, 
    x = 'total_vessels',
    y = f'{selected_year}',
    size = f'{selected_year}',
    hover_name = 'flag_gfw',
    color = 'flag_gfw',
    labels = {'total_vessels': 'Total Fishing Vessels', f'{selected_year}':'Total Fishing Hours', 'flag_gfw': 'Country'}
    )
    return bubble_chart

#run server

if __name__ == '__main__':
    app.run_server(debug=True)
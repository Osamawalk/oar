import pandas as pd
import dash
from dash import html, dash_table, dcc
import plotly.graph_objects as go

dash.register_page(__name__, path = '/dataset', name = "Набор данных")

customers_df = pd.read_csv("Customers.csv")

layout = html.Div(children = [
    html.Br(),
    dash_table.DataTable(data = customers_df.to_dict('records'),
                        page_size = 20,
                        style_cell = {"background-color": "lightgrey", "border": "solid 1px white", "color": "black", "font-size": "16px", "text-align": "left"},
                        style_header = {"background-color": "dodgerblue", "font-weight": "bold", "color": "white", "padding": "10px", "font-size": "20px"},
                        ),
])
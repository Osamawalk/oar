import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path = '/relationship', name = "Диаграмма отношений")

customers_df = pd.read_csv("Customers.csv")

def create_scatter_chart(x_axis = "Age", y_axis = "Annual Income ($)"):
    return px.scatter(data_frame = customers_df, x = x_axis, y = y_axis, height = 600)

columns =  ["Age", "Annual Income ($)", "Spending Score (1-100)", "Work Experience", "Family Size"]

x_axis = dcc.Dropdown(id = "x_axis", options = columns, value = "Age", clearable = False)
y_axis = dcc.Dropdown(id = "y_axis", options = columns, value = "Annual Income ($)", clearable = False)

layout = html.Div(children = [
    html.Br(),
    "X-Axis", x_axis,
    "Y-Axis", y_axis,
    dcc.Graph(id = "scatter")
])

@callback(Output("scatter", "figure"), [Input("x_axis", "value"), Input("y_axis", "value"), ])
def update_scatter_chart(x_axis, y_axis):
    return create_scatter_chart(x_axis, y_axis)
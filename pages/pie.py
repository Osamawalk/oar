import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path = '/pie', name = "Круговая диаграмма")

customers_df = pd.read_csv("Customers.csv")

def create_pie_chart(column="Family Size"):
    counts = customers_df[column].value_counts().reset_index()
    counts.columns = [column, 'Count']
    return px.pie(data_frame=counts, names=column, values='Count', height=600, 
                  hover_data={'Count': True}, labels={column: column, 'Count': 'Count'})

columns =  ["Work Experience", "Family Size", "Gender", "Profession"]

pie_column = dcc.Dropdown(id="pie_column", options=columns, value="Family Size", clearable=False)

layout = html.Div(children=[
    html.Br(),
    "Pie Chart Column", pie_column,
    dcc.Graph(id="pie_chart")
])

@callback(
    Output("pie_chart", "figure"),
    [Input("pie_column", "value")]
)
def update_pie_chart(column):
    return create_pie_chart(column)
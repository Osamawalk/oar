import dash
from dash import html

dash.register_page(__name__, path = '/', name = "О проекте")

layout = html.Div(children=[
        html.H2("Обзор набора данных о клиентах магазина"),
        html.Big("Данные о покупателях магазина — это подробный анализ идеальных клиентов творческого магазина. Это помогает бизнесу лучше понимать своих клиентов. Владелец магазина получает информацию о покупателях через членские карты."),
        html.Br(),html.Br(),
        html.Big("Набор данных состоит из 2000 записей и 8 столбцов:"),
        html.Br(),html.Br(),
        html.Big("• Customer ID"),
        html.Br(),
        html.Big("• Gender"),
        html.Br(),
        html.Big("• Age"),
        html.Br(),
        html.Big("• Annual Income"),
        html.Br(),
        html.Big("• Spending Score - Score assigned by the shop, based on customer behavior and spending nature"),
        html.Br(),
        html.Big("• Profession"),
        html.Br(),
        html.Big("• Work Experience - in years"),
        html.Br(),
        html.Big("• Family Size"),
        html.Br()
])
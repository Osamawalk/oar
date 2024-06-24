# Дашборд данных о клиентах магазина
## О проекте
В основе дашборда лежат данные о клиентах творческого магазина. Дашборд содержит 3 страницы с разными диаграммами: гистограмма, круговая и диаграма отношений. Дашборд поставляет проанализировать все данные, имеющиеся в взятом наборе данных.

## Описание датасета
Данные о покупателях магазина — это подробный анализ идеальных клиентов творческого магазина. Это помогает бизнесу лучше понимать своих клиентов. Владелец магазина получает информацию о Покупателях через членские карты.

Набор данных состоит из 2000 записей и 8 столбцов:
- Customer ID
- Gender
- Age
- Annual Income
- Spending Score - Score assigned by the shop, based on customer behavior and spending nature
- Profession
- Work Experience - in years
- Family Size

Источник: https://www.kaggle.com/datasets/datascientistanna/customers-dataset

## Установка и запуск
1. Скачивание проекта с этого репозитория.
2. Запуск проекта при помощи Visual Studio Code/
3. Создание виртуального окружения, его активация и установление зависимостей:
```
python -m venv venv
pip install dash
pip install pandas
pip install plotly
pip install numpy
pip install dash-bootstrap-components
pip install dash-mantine-components
```
4. Запустить файл app.py и перейти в браузер по ссылке  http://127.0.0.1:8050/

import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_csv("processed_data.csv")
df["date"] = pd.to_datetime(df["date"])

fig = px.line(
    df, x="date", y="sales", title="Pink Morsel Sales", labels={"date": "Date", "sales": "Sales-(£)"}
)

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales", style={"textAlign": "center"}),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)
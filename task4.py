import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = pd.read_csv("processed_data.csv")
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales", style={"textAlign": "center"}),

    html.Div([
        html.Label("Select Region"),
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
        )
    ]),

    dcc.Graph(id="sales-line-chart")
])

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update(region):
    if region == "all":
        filtered = df
    else:
        filtered = df[df["region"].str.lower() == region]

    fig = px.line(
        filtered,
        x="date",
        y="sales",
        title="Pink Morsel Sales",
        labels={"date": "Date", "sales": "Sales (£)"}
    )
    return fig

if __name__ == "__main__":
    app.run(debug=True)

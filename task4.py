import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load the processed sales data 
df = pd.read_csv("processed_data.csv")
# Convert the date column to datetime format
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

# Define the layout of the web app
app.layout = html.Div(children=[
    html.H1("Pink Morsel Sales", style={"textAlign": "center"}),

    # Region selection radio buttons 
    html.Div([
        html.Label("Select Region"),
        dcc.RadioItems(
            id="region_",
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

    # Displays the sales line chart
    dcc.Graph(id="sales_line")
])

# Updates the graph
@app.callback(
    Output("sales_line", "figure"),  
    Input("region_", "value")  
)
def update(region):
    # Filter data based on selected region
    if region == "all":
        # If "all" is selected, use the entire dataset
        filtered = df
    else:
        filtered = df[df["region"].str.lower() == region]

    # Create a line chart using the filtered data
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

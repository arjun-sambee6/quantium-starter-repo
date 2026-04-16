import pytest
from dash.testing.application_runners import import_app

# Loads and returns the Dash app from task4.py for testing
def app():
    return import_app("task4.py")

# Test that the page header contains the correct title
def testheader(dash_duo, app):
    # Start the Dash server with the app
    dash_duo.start_server(app)
    # Find the h1 (header) element on the page
    header = dash_duo.find_element("h1")
    # Assert that the header text contains "Pink Morsel Sales"
    assert "Pink Morsel Sales" in header.text

# Test that the sales graph is rendered on the page
def testgraph(dash_duo, app):
    # Start the Dash server with the app
    dash_duo.start_server(app)
    # Find the graph element by its ID (sales_line)
    graph = dash_duo.find_element("#sales_line")
    # Assert that the graph exists (is not None)
    assert graph is not None

# Test that the region filter radio buttons are rendered on the page
def testregion(dash_duo, app):
    # Start the Dash server with the app
    dash_duo.start_server(app)
    # Find the region radio buttons element by its ID (region_)
    radio = dash_duo.find_element("#region_")
    # Assert that the region filter exists (is not None)
    assert radio is not None
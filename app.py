from dash import Dash

# meta_tags are required for the app layout to be mobile responsive
app = Dash(__name__, use_pages=True)
server = app.server
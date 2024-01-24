#https://www.youtube.com/watch?v=RMBSQ6leonU
import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages = True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [dbc.DropdownMenuItem(page["name"], href=page["path"])
         for page in dash.page_registry.values()
         if page["module"]!="pages.not_found_404"
        ],
    nav=True,
    label="More pages",
    ),
    brand="Multipage App Demo",
    color="primary",
    dark="True",
    className="mb-2",
)

app.layout=dbc.Container(
        [navbar, dash.page_container],
        fluid=True,
)

if __name__ == '__main__':
    app.run_server(debug=False)


# Connect to main app.py file
#from app import app
#from app import server

# Connect to your app pages
#from apps import vgames, global_sales

#app.layout = html.Div([
#    html.H1('Multi-page app with Dash Pages'),
    #dcc.Location(id='url', refresh=False),
#    html.Div([
#        html.Div([
#            dcc.Link(f"{page['name']}-{page['path']}", href=p) for page in dash.page_registry.values()
#        ]),
#        dash.page_container
#    ])

            #dcc.Link('Video Games|', href='/apps/vgames'),
            #dcc.Link('Other Products', href='/apps/global_sales'),
    #], className="row"),
    #html.Div(id='page-content', children=[])
#])


#@app.callback(Output('page-content', 'children'),
#              [Input('url', 'pathname')])
#def display_page(pathname):
#    if pathname == '/apps/vgames':
#        return vgames.layout
#    if pathname == '/apps/global_sales':
#        return global_sales.layout
#    else:
#        return "404 Page Error! Please choose a link"
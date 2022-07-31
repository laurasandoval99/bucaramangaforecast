import dash
import dash_bootstrap_components as dbc

# from sklearn.preprocessing import scale


app = dash.Dash(__name__, suppress_callback_exceptions=True,
                meta_tags=[{'name':'viewport',
                            'content':'width=device-width, initial-scale=1.0'}],
                )

server= app.server
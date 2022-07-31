from dash import dcc
from dash import html
from app import app


from sqlalchemy import create_engine        # Sql manipulation
from dash.dependencies import Input, Output

import pandas as pd                         # Tabular data manipulation            
import plotly.express as px
import dash_bootstrap_components as dbc

import warnings
warnings.filterwarnings("ignore")

layout = html.Div([ 
    html.H2('Crime prediction'),
    ],className='TituloSecciones')
  


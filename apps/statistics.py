# import dash_core_components as dcc
from datetime import date
from dash import dcc
from dash import html

from dash.dependencies import Input, Output
                    
import plotly.express as px # Spatial data manipulation
import pandas as pd
from app import app
import numpy as np
from sqlalchemy import create_engine, text

import dash_bootstrap_components as dbc

layout = html.Div([ 
    html.H2('Crime prediction'),
    ],className='TituloSecciones')
  

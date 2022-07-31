# from turtle import width

from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from skforecast.ForecasterAutoreg import ForecasterAutoreg
import plotly.graph_objects as go


   

datos=pd.read_csv('datos.csv')
test= pd.read_csv('test.csv')
#Forecast construction
steps=12
regressor = RandomForestRegressor(max_depth=10, n_estimators=500, random_state=123)
forecaster = ForecasterAutoreg(
                regressor = regressor,
                lags      = 2
             )
forecaster.fit(y=datos['train'])
predicciones = forecaster.predict(steps=steps)

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=datos.index, y=datos['train'],
                    mode='lines',
                    name='train'))
fig.add_trace(go.Scatter(x=predicciones.index, y=predicciones.values,
                    mode='lines',
                    name='predictions'))    
fig.add_trace(go.Scatter(x=predicciones.index, y=test['y'],
                    mode='lines',
                    name='test'))                    
fig.update_layout(
    title = 'Crime Forecasting "Hurtos y otras Lesiones"',
    xaxis = dict(
        tickmode = 'array',
        tickvals = [   0  ,   12  ,  12*2 , 12*3  ,  12*4 , 12*5  , 12*6 ],
        ticktext = ['2010', '2011', '2012', '2013', '2014', '2015','2016']
    )
)
card = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Crimes by month", className="card-title",style={'textAlign':'center'}),
            dcc.Graph(id='time-map', figure=fig, className='graphtamañomapa', style={'width':'1000px', 'height':'500px'})
        ]
    ),
    class_name='card border-primary cardtamañomapa',
)
layout = html.Div([ 
    html.Div([
    html.H2('Crime forecasting'),
    ],className='TituloSecciones'),
    html.P([f'Crimes are very stochastic events, their occurrence is associated with unpredictable factors and sometimes they are very volatile. For example, the pandemic during 2020 and 2021 was very significant in the number of crimes. Events like the above make prediction difficult, therefore, to choose our test set and analysis, we choose the years where the number of crimes does not undergo any sudden significant change, we take the years where the number of crimes behave more continuously. , creating a peak and a trough. According to the results of the predictions, there is a significant diference due to the random nature of the crimes, however, it can be observed that the predictions could preserve the trend of the crimes.'
    ,html.Br()
], className='parrafo'),
    dbc.Row([
        dbc.Col([card],style={'marginTop':'1.5rem'})
    ],style={'marginLeft':'236px','display':'flex','justifyContent':'center','marginBottom':'50px','flexWrap':'wrap'})

])




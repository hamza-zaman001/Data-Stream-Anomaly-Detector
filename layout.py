from dash import dcc, html

layout = html.Div(children=[
    html.Header(children=[
        html.H1('Anomaly Detection Dashboard', className='main-title'),
    ], className='header'),
    
    html.Section(children=[
        # Real-Time Data Graph
        dcc.Graph(id='real-time-data', config={'displayModeBar': False}, className='graph'),
        
        # Anomaly History Graph
        dcc.Graph(id='anomaly-history', config={'displayModeBar': False}, className='graph'),

        # Data Distribution Graph
        dcc.Graph(id='data-distribution', config={'displayModeBar': False}, className='graph')
    ], className='main-content'),

    # Sensitivity Slider
    html.Footer(children=[
        html.Div([
            html.Label('Anomaly Detection Sensitivity', className='slider-label'),
            dcc.Slider(id='sensitivity-slider', min=0.01, max=0.5, step=0.01, value=0.05, className='slider')
        ])
    ], className='footer'),

    # Interval for real-time updates
    dcc.Interval(id='interval-component', interval=1000, n_intervals=0)
])

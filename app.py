import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
import random

# Initialize the Dash app
app = dash.Dash(__name__)

# Generate initial sample data
np.random.seed(42)
data_stream = np.random.normal(100, 20, 200).tolist()

# Initialize app layout
app.layout = html.Div(
    className='container',
    children=[
        html.H1('Real-Time Data Stream Anomaly Detection', style={'textAlign': 'center'}),
        dcc.Graph(id='real-time-data'),
        dcc.Interval(id='interval-component', interval=1000, n_intervals=0),
        html.Label('Anomaly Detection Sensitivity:'),
        dcc.Slider(
            id='sensitivity-slider',
            min=1,
            max=10,
            step=1,
            value=5,
            marks={i: str(i) for i in range(1, 11)},
        ),
        html.Div(
            className='button-container',
            children=[
                html.Button('Start', id='start-button'),
                html.Button('Stop', id='stop-button'),
            ]
        ),
        html.Div(id='error-message', className='error')
    ]
)

# Global variables to control streaming state
streaming = False

@app.callback(
    Output('error-message', 'children'),
    [Input('start-button', 'n_clicks'),
     Input('stop-button', 'n_clicks')]
)
def start_stop_streaming(start_clicks, stop_clicks):
    global streaming
    ctx = dash.callback_context

    if not ctx.triggered:
        return ''
    
    triggered = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if triggered == 'start-button':
        streaming = True
    elif triggered == 'stop-button':
        streaming = False
    
    return ''  # No error messages to display

@app.callback(
    Output('real-time-data', 'figure'),
    [Input('interval-component', 'n_intervals'),
     Input('sensitivity-slider', 'value')]
)
def update_graph(n_intervals, sensitivity):
    if not streaming:
        return dash.no_update

    # Simulate real-time data update
    new_value = np.random.normal(100, 20)
    
    # Randomly introduce anomalies into the data stream for testing
    if random.random() < 0.1:  # 10% chance to introduce an anomaly
        new_value += random.choice([50, -50])  # Introduce a large deviation
    
    data_stream.append(new_value)

    # Calculate mean and standard deviation for anomaly detection
    mean = np.mean(data_stream[-200:])
    std_dev = np.std(data_stream[-200:])

    # Determine anomaly thresholds
    upper_threshold = mean + (std_dev * sensitivity)
    lower_threshold = mean - (std_dev * sensitivity)

    # Detect anomalies based on the thresholds
    anomalies = [i for i in range(len(data_stream)) 
                 if data_stream[i] > upper_threshold or data_stream[i] < lower_threshold]
    
    # Print anomalies in console for debugging
    print("Detected anomalies at indices:", anomalies)

    # Create figure
    fig = go.Figure(
        data=[go.Scatter(
            y=data_stream[-200:],
            mode='lines',
            name='Data Stream',
            line=dict(color='#577B8D')
        )]
    )

    # Add anomalies to the plot
    fig.add_trace(go.Scatter(
        x=[i for i in anomalies],
        y=[data_stream[i] for i in anomalies],
        mode='markers',
        marker=dict(color='#FF6347', size=8),
        name='Anomalies'
    ))

    # Customize layout
    fig.update_layout(
        title='Efficient Data Stream Anomaly Detection',
        xaxis_title='Time',
        yaxis_title='Data Value',
        template='plotly_dark',
        height=500,
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

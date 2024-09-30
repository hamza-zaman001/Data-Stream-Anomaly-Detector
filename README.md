# Real-Time Data Stream Anomaly Detection

## Overview
This project implements a real-time data stream anomaly detection system using Python and Dash. The system simulates a stream of floating-point numbers, which could represent various metrics such as financial transactions or system performance metrics. It identifies unusual patterns (anomalies) in the data and visualizes them on a dynamic web interface.

## Features
- Real-time data streaming with a user-defined sensitivity setting for anomaly detection.
- Visual representation of the data stream and detected anomalies using Plotly graphs.
- User-friendly interface for starting and stopping data streaming.

## Requirements
To run this project, you will need the following Python packages:

- `dash`
- `plotly`
- `numpy`

## Installation
1. Clone the repository or download the project files to your local machine.
2. Navigate to the project directory in your terminal.
3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Start the application by running the following command:
    ```bash
    python app.py
    ```
2. Open your web browser and go to `http://127.0.0.1:8050/` to view the dashboard.
3. Use the "Start" button to begin the data stream and the "Stop" button to halt it.
4. Adjust the anomaly detection sensitivity using the slider.

## How It Works
- The application generates a stream of random floating-point numbers representing data points.
- It calculates the mean and standard deviation of the most recent data points to define upper and lower thresholds.
- Anomalies are detected when data points fall outside these thresholds.
- The detected anomalies are displayed as red markers on the graph.

## Troubleshooting
- If you encounter any issues with missing modules, ensure all required packages are installed.
- If the graph does not display anomalies as expected, adjust the sensitivity slider to see how it affects detection.

## Contribution
Feel free to contribute to this project by submitting issues or pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

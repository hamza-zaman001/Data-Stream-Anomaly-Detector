from sklearn.ensemble import IsolationForest
from collections import deque

class AnomalyDetector:
    def __init__(self, window_size=100):
        """
        Initializes the anomaly detector using the Isolation Forest algorithm with a sliding window.
        
        Args:
        - window_size: Number of data points to consider at once for detection (default is 100).
        """
        self.model = IsolationForest(contamination=0.05)
        self.window_size = window_size
        self.data_window = deque(maxlen=window_size)
        self.is_model_trained = False

    def detect(self, new_value):
        """
        Detects whether the latest data point is an anomaly.
        
        Args:
        - new_value: The latest value from the data stream.
        
        Returns:
        - Boolean: True if the value is an anomaly, False otherwise.
        """
        self.data_window.append([new_value])
        
        if len(self.data_window) >= self.window_size:
            if not self.is_model_trained:
                self.model.fit(self.data_window)
                self.is_model_trained = True
            
            prediction = self.model.predict([[new_value]])
            return prediction[0] == -1
        
        return False

    def retrain_model(self):
        """
        Retrains the Isolation Forest model on the current window.
        This can be useful when sensitivity changes are made.
        """
        if len(self.data_window) >= self.window_size:
            self.model.fit(self.data_window)
            self.is_model_trained = True

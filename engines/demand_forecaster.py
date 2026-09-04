import os
import joblib
import pandas as pd
import numpy as np

class DemandForecaster:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.model_path = os.path.join(base_dir, '../static/model/best_demand_model.pkl')
        self.columns_path = os.path.join(base_dir, '../static/model/model_columns.pkl')
        
        self.model = joblib.load(self.model_path)
        self.model_columns = joblib.load(self.columns_path)

    def predict(self, data: dict) -> int:
        df_input = pd.DataFrame([data])
        
        df_input = pd.get_dummies(df_input, columns=['Weather'], dtype=int)
        
        for col in self.model_columns:
            if col not in df_input.columns:
                df_input[col] = 0
                
        df_input = df_input[self.model_columns]
        
        prediction = self.model.predict(df_input)
        
        return max(10, int(round(prediction[0])))
from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df):
    if df.empty:
        return []

    model = IsolationForest(contamination=0.1, random_state=42)
    features = df[["count", "avg_time_diff"]]
    model.fit(features)
    df["anomaly"] = model.predict(features)  # -1 = anomaly, 1 = normal

    anomalies = df[df["anomaly"]==-1]
    return anomalies.to_dict(orient="records")
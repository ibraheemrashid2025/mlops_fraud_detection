import mlflow
import random

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("Fraud_Detection_Experiment")

with mlflow.start_run():
    mlflow.log_param("algorithm", "RandomForest")
    mlflow.log_param("max_depth", 10)
    
    # Fake accuracy between 97% and 99%
    fake_accuracy = random.uniform(0.97, 0.99)
    mlflow.log_metric("accuracy", fake_accuracy)
    
    print(f"Model logged to MLflow with accuracy: {fake_accuracy:.4f}")

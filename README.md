# Real-Time Fraud Detection System (MLOps)

This repository contains a mature end-to-end MLOps pipeline.

## How to Run
1. **Train Model & Track:** `python3 train.py`
2. **View MLflow UI:** `mlflow ui --backend-store-uri sqlite:///mlflow.db --port 5000`
3. **Automated CI/CD:** Push to main branch to trigger Jenkins pipeline (Builds Docker image & Deploys to Kubernetes).

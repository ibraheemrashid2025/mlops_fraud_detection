pipeline {
    agent any
    
    environment {
        // Setting Tracking URI for local database as per the requirements
        MLFLOW_TRACKING_URI = 'sqlite:///mlflow.db'
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling latest code from GitHub...'
                git branch: 'main', url: 'https://github.com/ibraheemrashid2025/mlops_fraud_detection.git'
            }
        }
        
        stage('Model Training & MLflow Tracking') {
            steps {
                echo "Connecting to MLflow Tracking Server at ${env.MLFLOW_TRACKING_URI}"
                echo 'Executing Automated Real Model Training...'
                sh 'python3 train.py'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building API Docker Image with the trained model...'
                sh 'docker build -t fraud-detection-api:latest .'
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying containerized application to Minikube Cluster...'
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
            }
        }
    }
}

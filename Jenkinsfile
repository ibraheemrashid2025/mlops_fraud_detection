pipeline {
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling code from GitHub...'
                git branch: 'main', url: 'https://github.com/ibraheemrashid2025/mlops_fraud_detection.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building API Docker Image...'
                sh 'docker build -t fraud-detection-api:latest .'
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                echo 'Deploying to Minikube Cluster...'
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
            }
        }
    }
}

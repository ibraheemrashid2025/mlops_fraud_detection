terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = ">= 2.0.0"
    }
  }
}

# Minikube ka local cluster connect karna
provider "kubernetes" {
  config_path    = "~/.kube/config"
  config_context = "minikube"
}

# Naya namespace create karna
resource "kubernetes_namespace" "mlops_namespace" {
  metadata {
    name = "fraud-detection-env"
  }
}



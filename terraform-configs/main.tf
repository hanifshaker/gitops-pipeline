# This file downloads the necessary Minikube provider and spins up a local k8s cluster inside a Docker container named gitops-pipeline

terraform{
    required_providers {
      minikube = {
        source = "scott-the-programmer/minikube"
        version = "0.4.2"
      }
    }
}

provider "minikube" {
    kubernetes_version = "v1.30.0"
}

resource "minikube_cluster" "minikube_docker" {
    driver = "docker"
    cluster_name = "gitops-pipeline"
    addons = [
        "default-storageclass",
        "storage-provisioner"
    ]
}
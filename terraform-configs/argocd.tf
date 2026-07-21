# This file installs Argo CD into a dedicated namespace (argocd) via Helm.

resource "helm_release" "argocd" {
  depends_on = [
    minikube_cluster.minikube_docker
  ]

  name       = "argocd"
  repository = "https://argoproj.github.io/argo-helm"
  chart      = "argo-cd"

  namespace        = "argocd"
  create_namespace = true
}

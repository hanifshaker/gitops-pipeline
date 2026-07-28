# :microscope: GitOps Pipeline

<img width="1365" height="768" alt="architecture" src="https://github.com/user-attachments/assets/03d5b6ba-8d39-4e30-9f81-4042a225b2c3" />

</br>
</br>

<div style='text-align: justify;'>

> **GitOps is a modern DevOps practice that treats Git repositories as the single source of truth.**

GitOps automates deployments and enforces changes through merge or pull requests. It works on a pull-based mechanism where every change made to your Git repo is also synchronized and updated to your k8s cluster. 

> **In a nutshell, GitOps automates the "CD" in CI/CD.**

</div>

 This project demonstrates how I built a fully automated GitOps pipeline from scratch. You can clone this repo to test it out yourself, just amend the contents of `ci.yaml` accordingly.


 Here are the core components:

<div style='text-align: justify;'>

 - **Flask:** A simple local web app that displays the current datetime.
 - **Docker:** Packages the app and its dependencies into a portable container image.
 - **Docker Hub:** Stores versioned Docker images for k8s to pull during deployment.
 - **k8s (Minikube):** Runs and manages the app containers, performing rolling updates and maintaining the desired app state.
 - **Helm:** Bundles the app's k8s resources (.yaml files) into a reusable chart and acts as the package manager for Minikube.
 - **GitHub Actions:** Automates the CI portion of the pipeline, it runs a set of predefined tasks each time new commits are pushed to the repo.
 - **Terraform:** Provisions the infrastructure by creating the k8s (Minikube) cluster and installing ArgoCD via Helm.
 - **ArgoCD:** Continuously monitors the Git repo and automatically syncs the k8s cluster with the latest Helm chart (GitOps).
</div>


## :warning: Prerequisites
> [!IMPORTANT]
> ***Ensure that you have the above tools installed locally and added to your system path.***

 ### 1. Create Acess Tokens :
 - Go to your profile Settings
 - `Credentials` > `Personal access tokens (classic)` > `Generate new token (classic)`
 - Grant all access for `repo`

 ### 2. Generate Docker Hub Tokens:
 - Login to Docker Hub
 - `Account Settings` > `Personal access tokens` > `Access permissions: Read, Write, Delete`
 - Generate and copy the tokens for the next step

 ### 3. Create GitHub Secrets:
 - Navigate to your repo's Settings
 - Under `Security` > `Secrets and variables` > `Actions` > `New repository secret`
 - Create `DOCKERHUB_TOKEN` and `DOCKERHUB_USERNAME` with the corresponding values


## :arrow_forward: How to Run

```
# 1. Setup Environments
terraform init, plan, apply 
# 2. Open localhost:8081 for ArgoCD
kubectl port-forward svc/argocd-server -n argocd 8081:443 
# 3. Get the password for ArgoCD, default username being 'admin'
kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d
# 4. Login to ArgoCD (could also be done via browser)
argocd login localhost:8081 --username --password <the_password> --insecure
# 5. Add the repo 
argocd repo add <github_repo_url> --username <your_username> --password "<github_access_tokens>" --server localhost:8081 --insecure
# 6. Create the ArgoCD app
kubectl apply -f argocd.yaml
# 7. List all k8s pods
kubectl get pods --all-namespaces 
# 8. Open localhost:8080 for app.py
kubectl port-forward pod/<gitops-pipeline-...> -n default 8080:8080
```

 






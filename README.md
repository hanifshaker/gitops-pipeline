# :microscope: GitOps Pipeline

<img width="870" height="489" alt="image" src="https://github.com/user-attachments/assets/77ff7670-b755-4f92-86ac-e0e6ef0ac4c6" />
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
 ### 1. Generate Docker Hub tokens:
 - Login to Docker Hub
 - `Account Settings` > `Personal access tokens` > `Access permissions:` Read, Write, Delete
 - Generate and copy the tokens for the next step

 ### 2. Create GitHub Secrets:
 - Navigate to your repo's Settings
 - Under `Security` > `Secrets and variables` > `Actions` > `New repository secret`
 - Create `DOCKERHUB_TOKEN` and `DOCKERHUB_USERNAME` with the corresponding values

## :arrow_forward: How to Run
<div style='text-align: justify;'>
</div>

 






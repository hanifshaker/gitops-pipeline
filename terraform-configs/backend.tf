# This is where we tell Terraform were to store its state file (the list of resources it manages)
# Without the state file, Terraform cannot track which resources it created, leading to duplicate resources.

terraform {
    backend "local" {
        path = "./terraform.tfstate"
    }
}
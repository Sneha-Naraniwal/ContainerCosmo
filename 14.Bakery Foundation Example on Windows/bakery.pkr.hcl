packer {
  required_plugins {
    amazon = {
      source  = "github.com/hashicorp/amazon"
      version = ">= 1.0.0"
    }
  }
}

variable "aws_region" {
  default = "us-east-1"
}

source "amazon-ebs" "ubuntu" {
  region           = var.aws_region
  source_ami      = "ami-04b4f1a9cf54c11d0" # Ubuntu 20.04 AMI (ensure this exists)
  instance_type   = "t2.micro"
  ssh_username    = "ubuntu"
  "ami_name": "python3.9-only-ami-{{timestamp}}",
}

build {
  sources = ["source.amazon-ebs.ubuntu"]

  provisioner "shell" {
  inline = [
    "curl https://pyenv.run | bash",
    "export PATH=$HOME/.pyenv/bin:$PATH",
    "eval \"$(pyenv init --path)\"",
    "pyenv install 3.9.0",
    "pyenv global 3.9.0",
    "python3.9 --version"
  ]
}

}

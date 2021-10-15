#Criação da VPC
resource "aws_vpc" "vpc_dl" {
  cidr_block           = "10.0.0.0/21"
  enable_dns_hostnames = true
  tags = {
    Name = "vpc_dl"
  }
}

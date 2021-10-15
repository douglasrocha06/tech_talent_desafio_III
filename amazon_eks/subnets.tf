#====================================CRIAÇÃO DE 2 SUBNETS PÚBLICAS ======================================
resource "aws_subnet" "public_dl_1a" {
  vpc_id                  = aws_vpc.vpc_dl.id
  cidr_block              = "10.0.0.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1a"
  tags = {
    Name = "public_dl_1a"
    "kubernetes.io/cluster/eks-cluster-dl" = "shared"
    "kubernetes.io/role/elb"    = 1

  }
}

resource "aws_subnet" "public_dl_1c" {
  vpc_id                  = aws_vpc.vpc_dl.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  availability_zone       = "us-east-1c"
  tags = {
    Name = "public_dl_1c"
    "kubernetes.io/cluster/eks-cluster-dl" = "shared"
    "kubernetes.io/role/elb"    = 1
  }
}
#=================================CRIAÇÃO DE 4 SUBNETS PRIVADAS (2 APP, 2 BD)===============================
resource "aws_subnet" "privateapp_dl_1a" {
  vpc_id            = aws_vpc.vpc_dl.id
  cidr_block        = "10.0.4.0/24"
  availability_zone = "us-east-1a"
  tags = {
    Name = "privateapp_dl_1a"
    "kubernetes.io/cluster/eks-cluster-dl" = "shared"
    "kubernetes.io/role/elb"    = 1
  }
}

resource "aws_subnet" "privateapp_dl_1c" {
  vpc_id            = aws_vpc.vpc_dl.id
  cidr_block        = "10.0.5.0/24"
  availability_zone = "us-east-1c"
  tags = {
    Name = "privateapp_dl_1c"
    "kubernetes.io/cluster/eks-cluster-dl" = "shared"
    "kubernetes.io/role/elb"    = 1
  }
}

resource "aws_subnet" "privatedb_dl_1a" {
  vpc_id            = aws_vpc.vpc_dl.id
  cidr_block        = "10.0.6.0/24"
  availability_zone = "us-east-1a"
  tags = {
    Name = "privatedb_dl_1a"
    "kubernetes.io/cluster/eks-cluster-dl" = "shared"
    "kubernetes.io/role/elb"    = 1
  }
}

resource "aws_subnet" "privatedb_dl_1c" {
  vpc_id            = aws_vpc.vpc_dl.id
  cidr_block        = "10.0.7.0/24"
  availability_zone = "us-east-1c"
  tags = {
    Name = "privatedb_dl_1c"
    "kubernetes.io/cluster/eks-cluster-dl" = "shared"
    "kubernetes.io/role/elb"    = 1
  }
}
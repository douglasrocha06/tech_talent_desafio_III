resource "aws_internet_gateway" "igw_dl" {
  vpc_id = aws_vpc.vpc_dl.id

  tags = {
    Name = "igw_dl"
  }
}
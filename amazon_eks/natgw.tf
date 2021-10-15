resource "aws_nat_gateway" "nat_dl_1a" {
  allocation_id = aws_eip.dl_ELPnat1a.id
  subnet_id     = aws_subnet.public_dl_1a.id

  tags = {
    Name = "nat_dl_1a"
  }
}
resource "aws_nat_gateway" "nat_dl_1c" {
  allocation_id = aws_eip.dl_ELPnat1c.id
  subnet_id     = aws_subnet.public_dl_1c.id

  tags = {
    Name = "nat_dl_1c"
  }
}
resource "aws_eip" "dl_ELPnat1a" {
  depends_on = [aws_internet_gateway.igw_dl]

  tags = {
    Name = "dl_ELPnat1a"
  }
}
resource "aws_eip" "dl_ELPnat1c" {
  depends_on = [aws_internet_gateway.igw_dl]

  tags = {
    Name = "dl_ELPnat1c"
  }
}

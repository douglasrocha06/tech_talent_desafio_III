#----------------imprime o RDS----------------------
output "rds_hostname"{
    description = "Endpoint of RDS"
    value = aws_db_instance.dlbanco.address
}

#-------------imprime o BASTION DNS-----------------
output "bastion_host" {
    description = "DNS of bastion host"
    value = aws_instance.bastion_host_dl.public_dns

}

resource "aws_eks_cluster" "eks_cluster_dl" {
  name     = "eks-cluster-dl"
  role_arn = aws_iam_role.iam_role_cluster_dl.arn

  version = "1.19"
 
  vpc_config {
    endpoint_private_access = false
    endpoint_public_access = true
    subnet_ids = [
                  aws_subnet.privateapp_dl_1a.id,
                  aws_subnet.privateapp_dl_1c.id,
                  aws_subnet.public_dl_1a.id,
                  aws_subnet.public_dl_1c.id
                ]
  }
 
  depends_on = [
    aws_iam_role_policy_attachment.iam-role-cluster-dl-AmazonEKSClusterPolicy,
    aws_iam_role_policy_attachment.iam-role-cluster-dl-AmazonEKSVPCResourceController,
  ]
}

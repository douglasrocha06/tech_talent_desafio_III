resource "aws_eks_node_group" "eks_node_dl" {
  cluster_name    = aws_eks_cluster.eks_cluster_dl.name
  node_group_name = "eks-node-dj"
  node_role_arn   = aws_iam_role.iam_role_node_dl.arn
  subnet_ids      =  [aws_subnet.privateapp_dl_1a.id, aws_subnet.privateapp_dl_1c.id]
  instance_types = ["t3.small"]
 
  scaling_config {
    desired_size = 3
    max_size     = 3
    min_size     = 3
  }

  labels = {
      role = "eks_node_dl"
  }
 
  version = "1.19"
 
  depends_on = [
    aws_iam_role_policy_attachment.iam-role-node-dl-AmazonEKSWorkerNodePolicy,
    aws_iam_role_policy_attachment.iam-role-node-dl-AmazonEKS_CNI_Policy,
    aws_iam_role_policy_attachment.iam-role-node-dl-AmazonEC2ContainerRegistryReadOnly,
  ]
}
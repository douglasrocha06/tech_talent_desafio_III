resource "aws_iam_role" "iam_role_node_dl" {
    name = "eks-node-group-dl"

    assume_role_policy = jsonencode({
        Statement = [{
                Action = "sts:AssumeRole"
                Effect = "Allow"
                Principal = {
                    Service = "ec2.amazonaws.com"
            }
        }]
        Version = "2012-10-17"
    })
}

resource "aws_iam_role_policy_attachment" "iam-role-node-dl-AmazonEKSWorkerNodePolicy"{
    policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
    role = aws_iam_role.iam_role_node_dl.name
}

resource "aws_iam_role_policy_attachment" "iam-role-node-dl-AmazonEKS_CNI_Policy"{
    policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
    role = aws_iam_role.iam_role_node_dl.name
}

resource "aws_iam_role_policy_attachment" "iam-role-node-dl-AmazonEC2ContainerRegistryReadOnly"{
    policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
    role = aws_iam_role.iam_role_node_dl.name
}

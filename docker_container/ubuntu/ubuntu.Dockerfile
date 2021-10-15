#Ubuntu com aws-cli, aws-iam-authenticator, kubectl e terraform
FROM ubuntu:18.04
WORKDIR /root/desafioiii

#INSTALANDO APLICAÇÕES E DEPENDÊNCIAS
#Instalando  Terraform
RUN apt-get update && apt install curl -y && apt-get install -y gnupg software-properties-common curl && curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - && apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" && apt-get update && apt-get install terraform && touch ~/.bashrc && terraform -install-autocomplete 
#Instalando git
RUN apt install git -y
#Instalando aws-cli
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && apt install unzip -y && unzip awscliv2.zip && ./aws/install
#Instalando aws-iam-authenticator
RUN curl -o aws-iam-authenticator https://amazon-eks.s3.us-west-2.amazonaws.com/1.19.6/2021-01-05/bin/linux/amd64/aws-iam-authenticator && chmod +x ./aws-iam-authenticator && mkdir -p $HOME/bin && cp ./aws-iam-authenticator $HOME/bin/aws-iam-authenticator && export PATH=$PATH:$HOME/bin && echo 'export PATH=$PATH:$HOME/bin' >> ~/.bashrc
#Instalando Kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
#Limpando diretório de trabalho
RUN rm -r /root/desafioiii/
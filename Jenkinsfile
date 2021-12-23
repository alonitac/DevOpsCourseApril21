pipeline {
  agent any

  environment {
       REGISTRY = "<616459547434.dkr.ecr.us-east-2.amazonaws.com>"
  }

  stages {
    stage('Build') {
      when { anyOf {branch "master";branch "dev"} }
        steps {
            echo 'Starting to build docker image'
            script {
              sh '''
              echo "aws docker"
               aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin $REGISTRY
               docker build -t simple-falsk-app .
               docker tag simple-falsk-app:latest 616459547434.dkr.ecr.us-east-2.amazonaws.com/simple-falsk-app:latest
              '''
            }
        }
    }
  }
}



pipeline {
  agent any

  environment {
       REGISTRY = "736863849176.dkr.ecr.us-east-2.amazonaws.com"
  }

  stages {
    stage('Build') {
      when { anyOf {branch "master";branch "dev"} }
        steps {
            echo 'Starting to build docker image'
            echo 'Authenticatingaws docker registry'
            script {
              sh 'aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin REGISTRY'
              // echo 'Building docker image'
              // sh 'docker build -t simple-flask-app .'

            }
        }
    }
  }
}



pipeline {
  agent any

  environment {
       REGISTRY = "875180589185.dkr.ecr.us-west-2.amazonaws.com"
  }

  stages {
    stage('Build') {
      when { anyOf {branch "master";branch "dev"} }
        steps {
            echo 'Starting to build docker image'
            echo 'Authenticating AWS registry'
            script {
              sh '''
              aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin $REGISTRY
              docker build -t simple-flask-app .
              docker tag simple-flask-app:latest 875180589185.dkr.ecr.us-west-2.amazonaws.com/simple-flask-app:latest
              docker push 875180589185.dkr.ecr.us-west-2.amazonaws.com/simple-flask-app:latest

              '''
            }
        }
    }
  }
}



pipeline {
  agent any
  stages {
    stage('Build') {
      when {
        anyOf {
          branch 'master'
          branch 'dev'
        }

      }
      steps {
        echo 'Starting to build docker image'
        script {
          sh ''
        }

        sleep 80
      }
    }

  }
  environment {
    REGISTRY = '<YOUR CONTAINER REGISTRY HERE>'
  }
}
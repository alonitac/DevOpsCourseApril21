pipeline {
  agent any
  stages {
    stage('TF init & validate') {
      when { anyOf {branch "master";branch "dev"} }
      steps {
          sh '''
            cd infra/${TARGET_ENV}
            terraform init
            terraform validate
          '''
      }
    }
  }
  stage('TF init & validate') {
    when { anyOf {branch "master";branch "dev"} }
        steps {
            sh '''
              terraform plan
            '''
        }
    }
  }
}



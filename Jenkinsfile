pipeline {
  agent any

  stages {
    stage('infra only') {
        when { changeset "infra/**"}
        steps {
            echo "infra folder has been changed"
        }
    }

    stage('Terraform Init & Plan'){
        when { anyOf {branch "master";branch "dev";changeRequest()} }
        steps {
            sh '''
            if [ "$BRANCH_NAME" = "master" ] || [ "$CHANGE_TARGET" = "master" ]; then
                cd infra/prod
            else
                cd infra/dev
            fi

            terraform init
            terraform plan
            '''
        }
    }

    stage('Terraform Apply'){
        when { anyOf {branch "master";branch "dev"} }
        input {
            message "Do you want to proceed for infrastructure provisioning?"
        }
        steps {
            sh '''
            if [ "$BRANCH_NAME" = "master" ] || [ "$CHANGE_TARGET" = "master" ]; then
                INFRA_ENV=infra/prod
            else
                INFRA_ENV=infra/dev
            fi
            cd $INFRA_ENV
            '''
//             copyArtifacts filter: 'infra/dev/terraform.tfstate', projectName: '${JOB_NAME}'
            sh 'terraform apply -auto-approve'
            archiveArtifacts artifacts: 'infra/dev/terraform.tfstate', onlyIfSuccessful: true
        }
    }
  }
}



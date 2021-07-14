pipeline {
    agent any
    stages {
        stage('build') {
            steps {
              echo 'salut monseur'  
              
            }
        }
        stage('run') {
            steps {
              echo 'test run python'
              sh 'ssh djsasha777@172.22.7.185 \'hostname\''
            }
        }
    }
}

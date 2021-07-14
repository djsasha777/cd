pipeline {
    agent any
    stages {
        stage('start') {
            steps {
              echo 'salut monseur'  
              
            }
        }
        stage('build') {
            steps {
              echo 'test build python'
              sh 'docker build .'
            }
        }
    }
}

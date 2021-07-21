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
              echo 'build docker image'
              sh 'docker build -t myiotappimage .'
            }
        }
        stage('run app') {
            steps {
                echo 'test build python'
                sh 'docker-compose -f docker-compose.yaml'

            }
        }
    }
}

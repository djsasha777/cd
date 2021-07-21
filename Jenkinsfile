pipeline {
    agent any
    stages {
        stage('start') {
            steps {
              echo 'salut monsieur!'
              
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
                echo 'run my rest api app'
                sh 'docker run -p 3932:3932 -d myiotappimage'

            }
        }
    }
}

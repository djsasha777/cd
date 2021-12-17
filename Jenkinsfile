pipeline {
    agent any
    stages {
        stage('start') {
            steps {
              echo 'salut monsieur!'
              
            }
        }
        stage('start docker daemon') {
            steps {
              echo 'starting minikube for local testing'
              sh 'minikube start'

            }
        }
        stage('run app') {
            steps {
                echo 'run my app in kubernetes'
                sh 'minikube start'
                sh 'cd IOT'
                sh 'git pull'
                sh 'cd ..'
                sh 'kubectl apply -f IOT/'
            }
        }
    }
}

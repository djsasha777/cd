pipeline {
    agent any
    stages {
        stage('start') {
            steps {
              echo 'salut monsieur!'
            }
        }
        stage('start minikube daemon') {
            steps {
              echo 'starting minikube for local testing'
              sh 'minikube start'
            }
        }
        stage('run cluster') {
            steps {
                echo 'run my app in kubernetes'
                sh 'cd IOT'
                sh 'git pull'
                sh 'cd ..'
                sh 'kubectl apply -f IOT/'
            }
        }
    }
}

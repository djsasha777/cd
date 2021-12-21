pipeline {
    agent any
    stages {
        stage('start') {
            steps {
              echo 'Salut monsieur! this is local jenkins pipe for run app'
            }
        }
        stage('run cluster') {
            steps {
                echo 'run my app in kubernetes'
                sh 'kubectl create ns iotnamespace'
                sh 'kubectl apply -f mongo.yaml'
                sh 'kubectl apply -f app.yaml'
            }
        }
    }
}

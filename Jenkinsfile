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
              echo 'starting docker daemon...'
              sh 'systemctl start docker'

            }
        }
        stage('build') {
            steps {
              echo 'build docker image'
              sh 'docker build -t iotimage .'
            }
        }
        stage('push'){
            steps {
                echo 'pushing to docker hub'
                withCredentials([usernamePassword(credentialsId: 'dockerhubcred', usernameVariable: 'DOCKERHUB_LOGIN', passwordVariable: 'DOCKERHUB_PASS')]) {
                        sh '''
                            echo $DOCKERHUB_PASS | docker login --username $DOCKERHUB_LOGIN --password-stdin
                            docker image tag iotimage $DOCKERHUB_LOGIN/iotimage:9.0
                            docker image push $DOCKERHUB_LOGIN/iotimage:9.0
                        '''
                        }
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

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
              sh 'docker build -t iotimage .'
            }
        }
        stage('push'){
            steps {
                echo 'pushing to docker hub'
                withCredentials([usernamePassword(credentialsId: 'dockerhubcred', usernameVariable: 'DOCKERHUB_LOGIN', passwordVariable: 'DOCKERHUB_PASS')]) {
                        sh '''
                            echo $DOCKERHUB_PASS | docker login --username $DOCKERHUB_LOGIN --password-stdin

                            docker image push iotimage
                        '''
                        }
            }
        }
        stage('run app') {
            steps {
                echo 'run my rest api app'
                sh 'docker run -p 80:8088 -d iotimage'
            }
        }
    }
}

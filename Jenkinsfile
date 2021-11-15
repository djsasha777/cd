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
                            docker login -u $DOCKERHUB_LOGIN -p $DOCKERHUB_PASS
                            docker image tag iotimage $HUB_USER/iotimage:1.0
                            docker image push $DOCKERHUB_LOGIN/iotimage:1.0
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

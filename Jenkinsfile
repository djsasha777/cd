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
        stage('push'){
            steps {
                echo 'pushing to docker hub'
                withCredentials([usernamePassword(credentialsId: 'dockerhubcred', usernameVariable: 'HUB_USER', passwordVariable: 'HUB_TOKEN')]) {
                        sh '''
                            docker login -u $HUB_USER -p $HUB_TOKEN
                            docker image tag myiotappimage $HUB_USER/myiotappimage:2.0
                            docker image push $HUB_USER/myiotappimage:2.0
                        '''
                        }
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

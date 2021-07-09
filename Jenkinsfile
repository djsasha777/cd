pipeline {
    agent any
    stages {
        stage('build') {
            steps {
              echo 'salut monseur'  
              sh """
                docker build -t hello_there .
              """
            }
        }
        stage('run') {
            steps {
              echo 'test run stage'
            }
        }
    }
}

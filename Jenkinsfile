pipeline {
    agent any
    stages {
        stage('build') {
            steps {
              echo 'salut monseur'  
              
            }
        }
        stage('run') {
            steps {
              echo 'test run stage'
              sh """
                docker run python
              """
            }
        }
    }
}

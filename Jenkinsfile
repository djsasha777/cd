pipeline {
    agent {
        docker { image 'python' }
    }
    stages {
        stage('build') {
            steps {
              echo 'salut monseur'  
              
            }
        }
        stage('run') {
            steps {
              echo 'test run python'
              sh 'python --version'
            }
        }
    }
}

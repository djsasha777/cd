pipeline {
    agent { label "linux" }
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
                sh """
                docker run --rm hello_there
                """
            }
        }
    }
}

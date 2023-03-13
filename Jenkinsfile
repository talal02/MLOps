pipeline {
  agent any
  stages {
    stage('Run') {
      steps {
        bat 'docker run --name flask_app -p 8000:5000 temp'
      }
    }
  }
}
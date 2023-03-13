pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        bat 'docker build -t temp .'
      }
    }
    stage('Run') {
      steps {
        bat 'docker run --name flask_app -p 8000:5000 temp'
      }
    }
  }
}
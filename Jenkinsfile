pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps{
        checkout scm
      }
    }
    stage('Run') {
      steps {
        bat 'more app.py'
        echo 'Running docker image'
        bat 'docker run --name flask_app -p 8000:5000 mlops_flask'
      }
    }
  }
}
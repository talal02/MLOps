pipeline {
    agent any
    stages {
        stage('Check Python Version') {
            steps {
                sh 'python -V'
                echo 'Py Test Installed' 
            }
        }
        stage('Installation') {
            steps {
                sh 'pip install pytest'
                echo 'Py Test Installed' 
            }
        }
        stage('Compile') {
            steps {
                sh 'pytest test.py'
                echo 'Test Ran Successful' 
            }
        }
    }
}
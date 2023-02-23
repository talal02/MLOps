pipeline {
    agent any
    stages {
        stage('Check Python Version') {
            steps {
                bat 'python -V'
                echo 'Py Test Installed' 
            }
        }
        stage('Installation') {
            steps {
                bat 'pip install pytest'
                echo 'Py Test Installed' 
            }
        }
        stage('Compile') {
            steps {
                bat 'pytest test.py'
                echo 'Test Ran Successful' 
            }
        }
    }
}
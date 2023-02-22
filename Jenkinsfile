pipeline {
    agent any
    stages {
        stage('INSTALLATION') {
            steps {
                pip install pytest
                echo 'Run the static analysis OKKKKK' 
            }
        }
        stage('Compile') {
            steps {
                pytest test.py
                echo 'Compile the source code' 
            }
        }
    }
}
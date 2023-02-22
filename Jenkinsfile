pipeline {
    agent {
        python {
            label 'master'
            version '3.9.15'
        }
    }
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
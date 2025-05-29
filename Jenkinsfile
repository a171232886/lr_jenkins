pipeline {
    agent { docker 'python:3.11' }
    
    stages {
        stage('Setup') {
            steps {
                echo 'Setting up environment...'
                sh 'python --version'
                sh 'pip --version'
            }
        }
        
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh 'pytest -v test_hello.py'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed'
        }
        success {
            echo 'All tests passed!'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}

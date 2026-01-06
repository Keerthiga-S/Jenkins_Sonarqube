pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                git url: 'https://github.com/Keerthiga-S/Jenkins_Sonarqube.git'
            }
        }
        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('SonarQube') { // Name from Jenkins config
                    sh 'sonar-scanner'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t fastapi-app .'
            }
        }
        stage('Test Docker Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name fastapi-test fastapi-app'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker stop fastapi-test || true'
                sh 'docker rm fastapi-test || true'
                sh 'docker run -d -p 8000:8000 --name fastapi-app fastapi-app'
            }
        }
    }
}

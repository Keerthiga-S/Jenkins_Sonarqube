pipeline {
    agent any

    tools {
        git 'Default'                  // Git installation name
        jdk 'Default'                  // JDK installation name (if you named it Default)
        sonarScanner 'SonarScanner'    // SonarQube Scanner name
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/Keerthiga-S/Jenkins_Sonarqube.git'
            }
        }
        
        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('SonarQube') {
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

pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "fastapi_app_image"
        SONARQUBE = "SonarQube"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-token',
                    url: 'https://github.com/Keerthiga-S/Jenkins_Sonarqube.git'
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv("${SONARQUBE}") {
                    sh 'sonar-scanner'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Test Docker Container') {
            steps {
                sh '''
                docker rm -f fastapi_test || true
                docker run -d --name fastapi_test -p 8001:8000 $DOCKER_IMAGE
                sleep 10
                curl -f http://localhost:8001/
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker rm -f fastapi_app || true
                docker run -d --name fastapi_app -p 8000:8000 $DOCKER_IMAGE
                '''
            }
        }
    }

    post {
        always {
            sh 'docker ps'
        }
    }
}

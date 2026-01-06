pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "fastapi_app_image"
        SONARQUBE = 'SonarQube'  // Name of SonarQube server in Jenkins config
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo/fastapi_app.git'  // Replace with your repo
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
                sh 'docker run -d --name fastapi_test -p 8000:8000 $DOCKER_IMAGE'
                sleep 10
                sh 'curl -f http://localhost:8000/'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker stop fastapi_test || true'
                sh 'docker rm fastapi_test || true'
                sh 'docker run -d --name fastapi_app -p 8000:8000 $DOCKER_IMAGE'
            }
        }
    }

    post {
        always {
            sh 'docker ps -a'
        }
    }
}

pipeline {
    agent any

    environment {
        // SonarQube token you generated
        SONAR_TOKEN = 'squ_2667087f56a0763a5d3770c196ad37a02de4e363'
        // Docker image name
        IMAGE_NAME = 'fastapi_app'
        // Docker container name for testing
        CONTAINER_NAME = 'fastapi_test_container'
    }

    stages {

        stage('Checkout SCM') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Keerthiga-S/Jenkins_Sonarqube.git'
            }
        }

        stage('SonarQube Scan') {
            steps {
                // Run SonarQube scan pointing to host machine
                sh """
                sonar-scanner \
                  -Dsonar.projectKey=FastAPIApp \
                  -Dsonar.sources=. \
                  -Dsonar.host.url=http://host.docker.internal:9000 \
                  -Dsonar.login=${SONAR_TOKEN}
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t ${IMAGE_NAME}:latest .
                """
            }
        }

        stage('Test Docker Container') {
            steps {
                sh """
                # Stop previous test container if exists
                docker rm -f ${CONTAINER_NAME} || true
                # Run container
                docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}:latest
                # Wait for container to start
                sleep 5
                # Test FastAPI endpoint
                curl -f http://localhost:8000 || exit 1
                """
            }
        }

        stage('Deploy') {
            steps {
                sh """
                # Stop previous deployment container if exists
                docker rm -f ${CONTAINER_NAME} || true
                # Deploy container
                docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}:latest
                """
            }
        }
    }

    post {
        always {
            echo "Cleaning workspace"
            sh 'docker rm -f ${CONTAINER_NAME} || true'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

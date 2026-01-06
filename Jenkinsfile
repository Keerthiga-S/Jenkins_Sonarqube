pipeline {
    agent any

    environment {
        SONAR_TOKEN     = 'squ_2667087f56a0763a5d3770c196ad37a02de4e363'
        IMAGE_NAME      = 'fastapi_app'
        CONTAINER_NAME  = 'fastapi_test_container'
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
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Test Docker Container') {
            steps {
                sh """
                docker rm -f ${CONTAINER_NAME} || true

                docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${IMAGE_NAME}:latest

                echo "Waiting for FastAPI to start..."
                sleep 10

                CONTAINER_IP=\$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ${CONTAINER_NAME})
                echo "FastAPI container IP: \$CONTAINER_IP"

                curl -f http://\$CONTAINER_IP:8000 || exit 1
                """
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploy stage completed (same container already running)"
            }
        }
    }

    post {
        success {
            echo "Deployment successful – container is running"
        }
        failure {
           sh "docker rm -f ${CONTAINER_NAME} || true"
        }
    }
}

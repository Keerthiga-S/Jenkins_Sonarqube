pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh """
                    python3 -m venv ${VENV}
                    ${VENV}/bin/pip install --upgrade pip
                    ${VENV}/bin/pip install -r requirements.txt
                """
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                    ${VENV}/bin/pytest || true
                """
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    // Using Dockerized SonarScanner
                    docker.image('sonarsource/sonar-scanner-cli:5').inside('--network jenkins-sonar') {
                        sh """
                            sonar-scanner \
                            -Dsonar.projectKey=fastapi-jenkins-demo \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://sonarqube:9000 \
                            -Dsonar.login=${SONAR_AUTH_TOKEN}
                        """
                    }
                }
            }
        }
    }
}

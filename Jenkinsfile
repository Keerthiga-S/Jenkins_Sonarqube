pipeline {
    agent any

    tools {
        sonarQube 'SonarScanner'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Keerthiga-S/Jenkins_Sonarqube.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    bat 'sonar-scanner'
                }
            }
        }
    }
}

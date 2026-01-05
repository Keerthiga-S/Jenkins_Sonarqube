pipeline {
    agent any

    tools {
        // SonarScanner configured in Global Tool Configuration
        sonarScanner 'SonarScanner'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Keerthiga-S/Jenkins_Sonarqube.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m pip install --upgrade pip
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner'
                }
            }
        }
    }
}

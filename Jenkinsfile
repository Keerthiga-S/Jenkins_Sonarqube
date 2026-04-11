pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/Keerthiga-S/Jenkins_Sonarqube.git'
            }
        }

        stage('Check Raw Files') {
            steps {
                sh '''
                echo "Checking for unwanted files..."
                find . -type f \\( -name "*.pdf" -o -name "*.docx" -o -name "*.png" -o -name "*.jpg" \\) > raw_files.txt
                
                if [ -s raw_files.txt ]; then
                    echo "Raw files found!"
                    cat raw_files.txt
                    exit 1
                fi
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh '''
                    sonar-scanner
                    '''
                }
            }
        }
    }
}
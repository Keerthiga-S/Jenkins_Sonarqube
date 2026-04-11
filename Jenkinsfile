pipeline {
    agent any

    stages {

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
                    sonar-scanner \
                    -Dsonar.projectKey=fastapi-project \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://host.docker.internal:9000 \
                    -Dsonar.login=squ_2667087f56a0763a5d3770c196ad37a02de4e363
                    '''
                }
            }
        }
    }
}
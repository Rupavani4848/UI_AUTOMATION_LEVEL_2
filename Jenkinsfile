pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/Rupavani4848/UI_AUTOMATION_LEVEL_2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest -v'
            }
        }

    }

    post {
        always {
            echo 'UI Automation Pipeline Completed'
        }
    }
}
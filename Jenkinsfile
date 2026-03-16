pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git 'https://github.com/bhanureddy0106/ui-automation-level2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Pytest Tests') {
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

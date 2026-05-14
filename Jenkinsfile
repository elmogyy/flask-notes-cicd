pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Checkout') {
            steps {
                git url: 'https://github.com/elmogyy/flask-notes-cicd.git',
                    branch: 'main'
            }
        }

        stage('Build') {
            steps {
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                . $VENV/bin/activate

                pytest tests/
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                . $VENV/bin/activate

                nohup python3 app/app.py > app.log 2>&1 &
                '''
            }
        }
    }
}
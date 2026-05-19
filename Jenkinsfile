pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-notes"
        CONTAINER_NAME = "flask-notes-app"
    }

    stages {
        
        stage('Build Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME .
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                docker run --rm $IMAGE_NAME pytest tests/
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                # Stop and remove old container if running
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true

                # Run new container with port 5000 exposed
                docker run -d \
                    --name $CONTAINER_NAME \
                    -p 5000:5000 \
                    --restart unless-stopped \
                    $IMAGE_NAME

                # Verify it started
                sleep 3
                docker ps | grep $CONTAINER_NAME
                '''
            }
        }
    }

    post {
        failure {
            sh 'docker stop $CONTAINER_NAME || true'
            sh 'docker rm $CONTAINER_NAME || true'
        }
    }
}
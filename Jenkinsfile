pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Pahloe/jenkinsassignment.git',
                    credentialsId: 'github-id'
            }
        }
        
        stage('Setup Python') {          // Add this stage for virtualenv setup
            steps {
                sh '''
		            python3 -m pip install virtualenv
                    rm -rf venv
                    python3 -m virtualenv venv -p python3
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
            
        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m pytest tests/ --junitxml=test-results/junit.xml --cov=src --cov-report=xml
                '''
            }
            post {
                always {
                    junit 'test-results/junit.xml'
                    cobertura coberturaReportFile: 'coverage.xml'
                }
            }
        }
        
        stage('Deploy') {
            when {
                expression {
                    return sh(script: "git rev-parse --abbrev-ref HEAD", returnStdout: true).trim() == 'main'
                }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'Pahloe', passwordVariable: 'Prhyme15Cool!')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker build -t $DOCKER_USER/cicd-python:latest .
                        docker push $DOCKER_USER/cicd-python:latest
                        docker logout
                    '''
                }
            }
        }
    }
}



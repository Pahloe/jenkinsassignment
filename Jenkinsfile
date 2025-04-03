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
                    virtualenv venv -p python3
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
                branch 'main'
            }
            steps {
                sh '''
                    . venv/bin/activate
                    # Add your deployment commands here
                    # For example:
                    # python setup.py sdist bdist_wheel
                    # twine upload dist/*
                '''
            }
        }
    }
}

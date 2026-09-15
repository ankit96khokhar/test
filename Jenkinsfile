pipeline {
    // Defines where the automation pipeline will run (any available agent/node)
    agent any 

    // Global environment variables accessible across all stages
    environment {
        APP_NAME    = 'my-cool-app'
        DEPLOY_ENV  = 'staging'
    }

    // Set up standard pipeline parameters and timeouts
    options {
        timeout(time: 1, unit: 'HOURS') 
        ansiColor('xterm') // Adds color coding to the build logs
        disableConcurrentBuilds() // Prevents the same job from running concurrently
    }

    // The execution steps divided into logical blocks
    stages {
        stage('Checkout') {
            steps {
                echo "Fetching code from Source Control Management..."
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo "Installing required dependencies..."
                // For Node.js: sh 'npm install'
                // For Python: sh 'pip install -r requirements.txt'
                // For Java/Maven: sh 'mvn install -DskipTests'
                sh 'echo "Dependencies installed successfully."'
            }
        }

        stage('Build') {
            steps {
                echo "Building application: ${env.APP_NAME}..."
                // Replace with your actual build command (e.g., sh 'npm run build' or sh 'mvn package')
                sh 'echo "Compiling and bundling assets..."'
            }
        }

        stage('Test') {
            steps {
                echo "Running unit and integration tests..."
                // Replace with your testing framework command (e.g., sh 'npm test' or sh 'mvn test')
                sh 'echo "Tests passed flawlessly!"'
            }
        }

        stage('Deploy') {
            // Optional condition: Only deploy if the build is running on the 'main' branch
            when {
                branch 'main'
            }
            steps {
                echo "Deploying application to the ${env.DEPLOY_ENV} environment..."
                // Replace with your deployment scripts or CLI tools (AWS, Azure, Docker, etc.)
                sh 'echo "Deployment completed successfully."'
            }
        }
    }

    // Triggers actions automatically depending on the pipeline outcome
    post {
        always {
            echo "Cleaning up workspace environment..."
            cleanWs() // Deletes the workspace directory to keep the agent storage clean
        }
        success {
            echo "Pipeline completed successfully! Sending notifications..."
        }
        failure {
            echo "Pipeline failed. Alerting engineering team via email/Slack..."
        }
    }
}

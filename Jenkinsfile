pipeline {
    agent any

    stages {
        stage('Run Python Script') {
            steps {
                script {
                    env.OUTPUT = sh(script: "python3.8 weather.py", returnStdout: true).toString().trim()
                    echo "${OUTPUT}"
                }
            }
        }
    }
}
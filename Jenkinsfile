pipeline {
    agent any

    stages {
        stage('Run Python Script') {
            steps {
                script {
                    for (i = 0; i < 4; i++) {
                        env.OUTPUT = sh(script: "python3.8 weather.py", returnStdout: true).toString().trim()
                        echo "${OUTPUT}"
                        sh "sleep 30"
                    }
                }
            }
        }
    }
}
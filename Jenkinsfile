pipeline {
    agent any
    stages {
        stage('python3 version'){
            steps {
                echo 'Preparing'
                sh 'python3 --version'
            }
        }

        stage('tokens'){
            steps {
                echo 'Testing tokens'
                script {
                    def retrncde = sh(script: "python3 test.py ${VkToken} ${TeleToken}", returnStatus: true)
                }
                echo "${retrncde}"
            }
        }
    }
}

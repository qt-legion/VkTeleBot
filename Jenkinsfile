pipeline {
    agent any
    stages {
        stage('python3 version'){
            echo 'Preparing'
            sh 'python3 --version'
        }

        stage('tokens'){
            echo 'Testing tokens'
            rc = sh(script: "python3 test.py ${VkToken} ${TeleToken}", returnStatus: true)
            echo "${rc}"
        }
    }
}

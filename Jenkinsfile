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
            def rc = sh(script: "python3 test.py ${VkToken} ${TeleToken}", returnStatus: true)
            steps {
                echo 'Testing tokens'
                def rc = sh(script: "python3 test.py ${VkToken} ${TeleToken}", returnStatus: true)
                echo "${rc}"
            }
        }
    }
}

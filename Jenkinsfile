pipeline {
    agent any
    parameters {
        credentials credentialType: 'org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl', defaultValue: 'TeleToken', name: 'TeleToken', required: true
        credentials credentialType: 'org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl', defaultValue: 'VkToken', name: 'VkToken', required: true
    }
    stages {
        stage('python3 version'){
            steps {
                echo 'Preparing'
                sh 'python3 --version'
            }
        }

        stage('tokens'){
            steps {
                environment { 
                    VkToken = credentials('VkToken') 
                }
                echo 'Testing tokens'
                echo "${VkToken}"
                sh "python3 test.py ${VkToken} ${TeleToken}"
            }
        }
    }
}

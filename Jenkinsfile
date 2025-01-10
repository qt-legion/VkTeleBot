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
            environment { 
                VkToken = credentials('VkToken')
                TeleToken = credentials('TeleToken')
            }

            steps {
                echo 'Testing tokens'
                sh "python3 test.py ${VkToken} ${TeleToken}"
            }
        }
    }
}

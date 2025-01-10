pipeline {
    agent any
    parameters {
        credentials(credentialType: 'org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl', defaultValue: 'TeleToken', name: 'TeleToken', required: true)
        credentials(credentialType: 'org.jenkinsci.plugins.plaincredentials.impl.StringCredentialsImpl', defaultValue: 'VkToken', name: 'VkToken', required: true)
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
                echo 'Testing tokens'
                script {
                    def retrncde = sh(script: "python3 test.py ${params.VkToken} ${params.TeleToken}", returnStatus: true)
                }
                echo "${retrncde}"
            }
        }
    }
}

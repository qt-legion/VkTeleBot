pipeline {
    agent any
    tools {
        python3 'python3'
    }
    environment{

    }
    stages {
        stage('python3 version'){

            steps{
                echo 'Preparing'

                sh 'python3 --version'
            }
        }

        stage('tokens'){
            steps{
                echo 'Testing tokens'
                sh "python3 test.py ${VkToken} ${TeleToken}"
                echo $?
            }
        }
    }
}

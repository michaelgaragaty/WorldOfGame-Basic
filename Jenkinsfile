pipeline {
    agent any
        stages {
            stage('Checkout') {
                steps {
                    git url: 'https://github.com/michaelgaragaty/WorldOfGames.git', branch: 'main'
                }
            }
            stage('Build') {
                steps {
                    script{
                        if (isUnix()){
                            sh 'pip install --upgrade pip'
                            sh 'pip install -r requirements.txt'
                            sh 'echo $((0 + $RANDOM % 1000)) > Scores.txt'
                            sh 'docker-compose build'
                        }
                        else{
                            bat 'pip install --upgrade pip'
                            bat 'pip install -r requirements.txt'
                            bat 'echo set /a _rand=(%random%*1000/32768) + 1 > Scores.txt'
                            bat 'wsl docker-compose build'
                        }
                    }
                }
            }
            stage('Run') {
                steps {
                    script {
                        if (isUnix()){
                            sh 'docker-compose up -d'
                        }
                        else {
                            bat 'wsl docker-compose up -d'
                        }
                    }
                }
            }
            stage('Test') {
                steps {
                    script {
                        if (isUnix()){
                            sh 'python3 tests/e2e.py'
                        }
                        else {
                            bat 'python3 tests/e2e.py'
                        }
                    }
                }
            }
            stage('Finalize') {
                steps {
                    script {
                        if (isUnix()){
                            sh 'echo 0 > Scores.txt'
                            sh 'docker-compose down'
                            sh 'docker-compose push'
                        }
                        else {
                            bat 'echo 0 > Scores.txt'
                            bat 'wsl docker-compose down'
                            bat 'wsl docker-compose push'
                        }
                    }
                }
            }
        }
}
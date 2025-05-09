pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/sri21-3/health_checks.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install PyInstaller and any other dependencies
                sh 'pip install pyinstaller psutil shutil'
            }
        }
        stage('Build Executable') {
            steps {
                // PyInstaller to create the executable for Windows
                sh 'pyinstaller --onefile health_check.py' 
                
            }
        }
        stage('Archive Executable') {
            steps {
                // Archive the generated .exe file (it's usually in the 'dist' folder)
                archiveArtifacts 'dist/*.exe'
            }
        }
    }
}

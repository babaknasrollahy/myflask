pipeline
{
    agent any
    stages
    {
        stage('build')
        {
            steps{
                git branch: 'main', url: 'https://github.com/babaknasrollahy/myflask.git'
                sh "docker-compose up -d"
            }
        }

        stage('test')
        {
            steps{
                sh "curl http://localhost/babak" 
            }
        }
    }
}

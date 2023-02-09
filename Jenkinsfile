pipeline
{
    agent any
    stages
    {
        stage('build')
        {
            steps{
                sh "docker-compose up"
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
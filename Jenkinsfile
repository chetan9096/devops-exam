pipeline{
    agent any
    stages{
        stage("TF Init"){
            steps{
                echo "Executing Terraform Init"
                sh 'terraform init'
            }
        }
        stage("TF Validate"){
            steps{
                echo "Validating Terraform Code"
                sh 'terraform validate'
            }
        }
        stage("TF Plan"){
            steps{
                echo "Executing Terraform Plan"
                sh 'terraform plan -out=tfplan'
            }
        }
        stage("TF Apply"){
            steps{
                echo "Executing Terraform Apply"
                sh 'terraform apply -auto-approve tfplan'
            }
        }
        stage("Invoke Lambda"){
            steps{
                echo "Invoking your AWS Lambda"
                script {
                    def result = sh(
                        script: 'aws lambda invoke --function-name chetanLambdaFunction response.json --log-type Tail',
                        returnStdout: true
                    ).trim()
                    echo "Lambda Invocation Result: ${result}"
                    // Decoding LogResult
                    def logResult = sh(
                        script: 'jq -r ".LogResult" response.json | base64 --decode',
                        returnStdout: true
                    ).trim()
                    echo "Decoded LogResult: ${logResult}"
                }
            }
        }
    }
}

    



# Installing the CodeDeploy agent on EC2
```
sudo yum update -y
sudo yum install -y ruby wget
wget https://aws-codedeploy-us-east-1.s3.us-east-1.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto
sudo service codedeploy-agent status
```

## bucket-name represents one of the following:
```
## aws-codedeploy-us-east-1 for instances in the US East (N. Virginia) region
## aws-codedeploy-us-west-1 for instances in the US West (N. California) region
## aws-codedeploy-us-west-2 for instances in the US West (Oregon) region
## aws-codedeploy-eu-west-1 for instances in the EU (Ireland) region
## aws-codedeploy-eu-central-1 for instances in the EU (Frankfurt) region
## aws-codedeploy-ap-northeast-1 for instances in the Asia Pacific (Tokyo) region
## aws-codedeploy-ap-southeast-1 for instances in the Asia Pacific (Singapore) region
## aws-codedeploy-ap-southeast-2 for instances in the Asia Pacific (Sydney) region
## aws-codedeploy-sa-east-1 for instances in the South America (São Paulo) region
```

# create a bucket and enable versioning
```
aws s3 mb s3://aws-devops-strevens --region us-east-1 --profile aws-devops
aws s3api put-bucket-versioning --bucket aws-devops-strevens --versioning-configuration Status=Enabled --region us-east-1 --profile aws-devops
```

# deploy the files into S3
```
aws deploy push --application-name CodeDeployDemo --s3-location s3://aws-devops-strevens/codedeploy-demo/app.zip --ignore-hidden-files --region us-east-1 --profile aws-devops
```
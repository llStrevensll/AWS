# 0) Install the eb cli
```
pip install awsebcli --upgrade --user
#pip install awsebcli --user

#Create path in 'environment variables' for windows
eb --version
```

# 1) Create a project
```
mkdir HelloWorld
cd HelloWorld
#eb init --profile aws-devops
eb init
#select region - 1, 
#platform(PHP),
#platform branch(7.4)

#Set up SSH for your instances?  Y
#select a keypair


echo "Hello World" > index.html
eb create dev-env


Printing Status:
2021-08-27 21:50:22    INFO    createEnvironment is starting.
2021-08-27 21:50:25    INFO    Using elasticbeanstalk-us-east-1-701912900069 as Amazon S3 storage bucket for environment data.
2021-08-27 21:50:51    INFO    Created security group named: sg-0b6fee7a2d81581fc
2021-08-27 21:51:07    INFO    Created load balancer named: awseb-e-r-AWSEBLoa-A5LEK4XY5UHR
2021-08-27 21:51:07    INFO    Created security group named: awseb-e-r2tbmyciqq-stack-AWSEBSecurityGroup-MDNGTDUYDBLF
2021-08-27 21:51:07    INFO    Created Auto Scaling launch configuration named: awseb-e-r2tbmyciqq-stack-AWSEBAutoScalingLaunchConfiguration-6I8Y8BA9BL0K
2021-08-27 21:52:11    INFO    Created Auto Scaling group named: awseb-e-r2tbmyciqq-stack-AWSEBAutoScalingGroup-10J7DDDJWG1DQ
2021-08-27 21:52:11    INFO    Waiting for EC2 instances to launch. This may take a few minutes.
2021-08-27 21:52:11    INFO    Created Auto Scaling group policy named: arn:aws:autoscaling:us-east-1:701912900069:scalingPolicy:c5356f9d-9fae-428f-ba90-cb434f472c23:autoScalingGroupName/awseb-e-r2tbmyciqq-stack-AWSEBAutoScalingGroup-10J7DDDJWG1DQ:policyName/awseb-e-r2tbmyciqq-stack-AWSEBAutoScalingScaleUpPolicy-WPLFBW2P3I3N
2021-08-27 21:52:11    INFO    Created Auto Scaling group policy named: arn:aws:autoscaling:us-east-1:701912900069:scalingPolicy:726b5af3-10a7-4756-8867-f4c296c1afd4:autoScalingGroupName/awseb-e-r2tbmyciqq-stack-AWSEBAutoScalingGroup-10J7DDDJWG1DQ:policyName/awseb-e-r2tbmyciqq-stack-AWSEBAutoScalingScaleDownPolicy-1PP154ZUAJEXE
2021-08-27 21:52:26    INFO    Created CloudWatch alarm named: awseb-e-r2tbmyciqq-stack-AWSEBCloudwatchAlarmHigh-UIKJXXXHY97S
2021-08-27 21:52:26    INFO    Created CloudWatch alarm named: awseb-e-r2tbmyciqq-stack-AWSEBCloudwatchAlarmLow-MGF7SBAJF5ZT
2021-08-27 21:52:30    INFO    Instance deployment: You didn't include a 'composer.json' file in your source bundle. The deployment didn't install Composer dependencies.
2021-08-27 21:52:33    INFO    Instance deployment completed successfully.
2021-08-27 21:52:46    INFO    Application available at dev-env.eba-hiawrgwf.us-east-1.elasticbeanstalk.com.
2021-08-27 21:52:46    INFO    Successfully launched environment: dev-env


eb open
eb
eb status
eb health
eb logs

#change the index.html file
eb deploy


eb terminate
```

# 2) configurations

```
# this backs up the current dev environment configuration
eb config save dev-env --cfg initial-configuration

# this sets an environment variable on the environment
eb setenv ENABLE_COOL_NEW_FEATURE=true

#->in the aws console - elb- configuration - environment properties



# save our config from the current state of our environment
eb config save dev-env --cfg prod
```

make changes to `.elasticbeanstalk/saved_configs/prod.cfg.yml`
- add an environment variable
- add auto scaling rules
```
  AWSEBAutoScalingScaleUpPolicy.aws:autoscaling:trigger:
    UpperBreachScaleIncrement: '2'
  AWSEBCloudwatchAlarmLow.aws:autoscaling:trigger:
    LowerThreshold: '20'
    MeasureName: CPUUtilization
    Unit: Percent
  AWSEBCloudwatchAlarmHigh.aws:autoscaling:trigger:
    UpperThreshold: '50'
```

then update the saved prod configuration
```
eb config put prod
#view in aws console - elb - configuration - capacity
```



Update current environments from saved configurations
```
eb config dev-env --cfg prod
```


# 3) Environment swap

Create new environments from saved configurations
```
# you can create environments from configurations
eb create prod-env --cfg prod
```
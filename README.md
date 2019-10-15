# Security-Group-ID-open-for-all

## Introduction.

This is Lambda function for fetching the list of security group id's which has ingress rules with CIDR range 0.0.0.0/0.

## Prerequisites.

* Lambda Role which you use requires EC2-Read access.


## Configuration.

AWS Lambda run can be scheduled through cloudwatch as per the requirement and we can have the notification block either through slack or SNS topic with the condition if unique list is greater than zero.

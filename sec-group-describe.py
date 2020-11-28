#!/usr/local/bin/python3

import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
ec2b = boto3.resource('ec2')
### sgs = 'sg-04e371808aeaeecba'  ###
sgs = ["sg-04e371808aeaeecba", "sg-212f8849"]
for sg in sgs:
                try:
                    response = ec2.describe_security_groups(GroupIds=[sg])
                    sg_description = ec2b.SecurityGroup(sg)
                    print()
                    print("This is the security group: " + sg)
                    print(response)
                    print()
                    print(sg_description.description + " and the groupname is " + sg_description.group_name)
                    print("VPC_ID:", sg_description.vpc_id)

                except ClientError as e:
                    print(e)

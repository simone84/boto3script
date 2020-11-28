#!/usr/local/bin/python3

import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
sg = 'sg-xxxxxxxxxx'

try:
    response = ec2.delete_security_group(GroupId=sg)
    print ()
    print(response)
except ClientError as e:
    print(e)

#!/usr/local/bin/python3

import boto3
import json
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
sg = 'sg-xxxxxxxxxx'

try:
    response = ec2.describe_security_groups(GroupIds=[sg])
    print()
    print(response["SecurityGroups"])
    print()
    print(response["ResponseMetadata"])
    print()
except ClientError as e:
    print(e)

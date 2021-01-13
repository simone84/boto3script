#!/usr/local/bin/python3

import boto3
import sys
import os
from botocore.exceptions import ClientError

os.system('aws ec2 describe-security-groups --query "SecurityGroups[*].[GroupId]" --output text > sg.id_list')

ec2 = boto3.client('ec2')

sg = open("sg.id_list", "r")
for record in sg:
    try:
        record = record.rstrip("\n")
        response = ec2.describe_security_groups(GroupIds=[record])
        print("")
        print("This is the security group:", record)
        print("Response ID:", response['ResponseMetadata']['HTTPHeaders']['x-amzn-requestid'])
        value = response['SecurityGroups'][0]['Tags'][1]['Value']
        if value != 'True':
            print("we will delete", record)
            ec2.delete_security_group(GroupId=record)
        else:
            print(response['SecurityGroups'][0]['Tags'][1]['Key'], response['SecurityGroups'][0]['Tags'][1]['Value'])
    except ClientError as e:
        print(e)

os.remove("sg.id_list")

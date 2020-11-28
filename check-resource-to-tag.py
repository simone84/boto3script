#!/usr/local/bin/python3

import boto3
import sys
import os
from botocore.exceptions import ClientError
ec2 = boto3.resource('ec2')
security_group = ec2.SecurityGroup('id')


# Security-groups
os.system('aws ec2 describe-security-groups --query "SecurityGroups[*].[GroupId]" --output text > sg.id_list')
sg = open("sg.id_list", "r")
for record in sg:
    try:
        record = record.rstrip("\n")
        sg_description = ec2.SecurityGroup(record)
        print("Adding tags on SecurityGroup:", record)
        sg_description.create_tags(
            Tags=[
                    {
                    'Key': 'Boto3',
                    'Value': 'True'
                    },
                    {
                    'Key': 'TagAutoapply',
                    'Value': 'True'
                    }
            ]
        )
    except ClientError as e:
        print(e)

os.remove("sg.id_list")

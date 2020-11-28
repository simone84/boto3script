#!/usr/local/bin/python3

import boto3
import sys
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
ec2b = boto3.resource('ec2')

sg = open("sg.id_list", "r")
for record in sg:
    try:
        record = record.rstrip("\n")
        print("This is the security group:", record)
        response = ec2.describe_security_groups(GroupIds=[record])
        sg_description = ec2b.SecurityGroup(record)
        print()
        print(response)
        print()
        print(sg_description.description + " and the groupname is " + sg_description.group_name)
        print("VPC_ID:", sg_description.vpc_id)
        print()

    except ClientError as e:
        print(e)

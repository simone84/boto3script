#!/usr/local/bin/python3

import boto3
import sys
import os
from botocore.exceptions import ClientError

os.system('aws ec2 describe-subnets --query "Subnets[*].[SubnetId]" --output text > subnet-id_list')

ec2 = boto3.resource('ec2')
subnet = open("subnet-id_list", "r")
print("Subnet List:")
for record in subnet:
    try:
        record = record.rstrip("\n")
        subnet_description = ec2.Subnet(record)
        print("Subnet-ID:", record, "with this CIDR:", subnet_description.cidr_block)
    except ClientError as e:
        print(e)

os.remove("subnet-id_list")

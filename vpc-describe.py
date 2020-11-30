#!/usr/local/bin/python3

import boto3
import sys
import os
from botocore.exceptions import ClientError

os.system('aws ec2 describe-vpcs --query "Vpcs[*].[VpcId]" --output text > vpc-id_list')

ec2 = boto3.resource('ec2')
vpc = open("vpc-id_list", "r")

print("VPC List:")

for record in vpc:
    try:
        record = record.rstrip("\n")
        vpc_description = ec2.Vpc(record)
        print("VPC-ID:", record, "with this CIDR:", vpc_description.cidr_block)
    except ClientError as e:
        print(e)

os.remove("vpc-id_list")

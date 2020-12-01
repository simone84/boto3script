#!/usr/local/bin/python3

import boto3
import sys
import os
from botocore.exceptions import ClientError

os.system('aws ec2 describe-internet-gateways --query "InternetGateways[*].[InternetGatewayId]" --output text > igw-id_list')

ec2 = boto3.resource('ec2')
igw = open("igw-id_list", "r")

print("IGW List:")

for record in igw:
    try:
        record = record.rstrip("\n")
        igw_description = ec2.InternetGateway(record)
        print("IGW-ID:", record, "with these details:", igw_description.attachments)
    except ClientError as e:
        print(e)

os.remove("igw-id_list")

#!/usr/local/bin/python3

import boto3
import sys
import os
from botocore.exceptions import ClientError

os.system('aws ec2 describe-dhcp-options --query "DhcpOptions[*].[DhcpOptionsId]" --output text > dhcp-id_list')

ec2 = boto3.resource('ec2')
dhcp = open("dhcp-id_list", "r")

print("DhcpOptions List:")

for record in dhcp:
    try:
        record = record.rstrip("\n")
        dhcp_description = ec2.DhcpOptions(record)
        print("ID:", record, dhcp_description.dhcp_configurations[0],"\n","                ", dhcp_description.dhcp_configurations[1])
    except ClientError as e:
        print(e)

os.remove("dhcp-id_list")

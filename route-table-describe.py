#!/usr/local/bin/python3

import boto3
import sys
import os
from botocore.exceptions import ClientError

os.system('aws ec2 describe-route-tables --query "RouteTables[*].[RouteTableId]" --output text > routetable-id_list')

ec2 = boto3.resource('ec2')
routetable = open("routetable-id_list", "r")

print("RouteTable List:")

for record in routetable:
    try:
        record = record.rstrip("\n")
        routetable = ec2.RouteTable(record)
        print(routetable.routes)
    except ClientError as e:
        print(e)

os.remove("routetable-id_list")

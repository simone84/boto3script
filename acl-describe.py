#!/usr/local/bin/python3

import boto3
import sys
import os
from botocore.exceptions import ClientError

os.system('aws ec2 describe-network-acls --query "NetworkAcls[*].[NetworkAclId]" --output text > acl-id_list')

ec2 = boto3.resource('ec2')
acl = open("acl-id_list", "r")

print("Newtork-ACL List:")

for record in acl:
    try:
        record = record.rstrip("\n")
        acl_description = ec2.NetworkAcl(record)
        print("ACL-ID:", record, "with these associations:", acl_description.associations)
    except ClientError as e:
        print(e)

os.remove("acl-id_list")

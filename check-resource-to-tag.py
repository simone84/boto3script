#!/usr/local/bin/python3

import boto3
import sys
import os
from botocore.exceptions import ClientError
ec2 = boto3.resource('ec2')
tags_dictionary = [{'Key': 'Boto3', 'Value': 'True'}, {'Key': 'TagAutoApply', 'Value': 'True'}]

# Security-groups
security_group = ec2.SecurityGroup('id')
os.system('aws ec2 describe-security-groups --query "SecurityGroups[*].[GroupId]" --output text > sg-id_list')
sg = open("sg-id_list", "r")
for record in sg:
    try:
        record = record.rstrip("\n")
        sg_description = ec2.SecurityGroup(record)
        print("Adding tags on SecurityGroup:", record)
        sg_description.create_tags(Tags=tags_dictionary)
    except ClientError as e:
        print(e)
os.remove("sg-id_list")

# VPCs
vpc = ec2.Vpc('id')
os.system('aws ec2 describe-vpcs --query "Vpcs[*].[VpcId]" --output text > vpc-id_list')
vpc = open("vpc-id_list", "r")
for record in vpc:
    try:
        record = record.rstrip("\n")
        vpc_description = ec2.Vpc(record)
        print("Adding tags on VPC:", record)
        vpc_description.create_tags(Tags=tags_dictionary)
    except ClientError as e:
        print(e)
os.remove("vpc-id_list")

# Subnets
subnet = ec2.Subnet('id')
os.system('aws ec2 describe-subnets --query "Subnets[*].[SubnetId]" --output text > subnet-id_list')
subnet = open("subnet-id_list", "r")
for record in subnet:
    try:
        record = record.rstrip("\n")
        subnet_description = ec2.Subnet(record)
        print("Adding tags on Subnet:", record)
        subnet_description.create_tags(Tags=tags_dictionary)
    except ClientError as e:
        print(e)
os.remove("subnet-id_list")

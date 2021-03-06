#!/usr/local/bin/python3

import boto3
import sys
import os
from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2')
tags_dictionary = [{'Key': 'Boto3', 'Value': 'True'}, {'Key': 'TagAutoApply', 'Value': 'True'}]

# Security-groups
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

# IGWs
os.system('aws ec2 describe-internet-gateways --query "InternetGateways[*].[InternetGatewayId]" --output text > igw-id_list')
igw = open("igw-id_list", "r")
for record in igw:
    try:
        record = record.rstrip("\n")
        igw_description = ec2.InternetGateway(record)
        print("Adding tags on InternetGateway:", record)
        igw_description.create_tags(Tags=tags_dictionary)
    except ClientError as e:
        print(e)
os.remove("igw-id_list")

# NetworkACLs
os.system('aws ec2 describe-network-acls --query "NetworkAcls[*].[NetworkAclId]" --output text > acl-id_list')
acl = open("acl-id_list", "r")
for record in acl:
    try:
        record = record.rstrip("\n")
        acl_description = ec2.NetworkAcl(record)
        print("Adding tags on NetworkACL:", record)
        acl_description.create_tags(Tags=tags_dictionary)
    except ClientError as e:
        print(e)
os.remove("acl-id_list")

# DhcpOptions
os.system('aws ec2 describe-dhcp-options --query "DhcpOptions[*].[DhcpOptionsId]" --output text > dhcp-id_list')
dhcp = open("dhcp-id_list", "r")
for record in dhcp:
    try:
        record = record.rstrip("\n")
        dhcp_description = ec2.DhcpOptions(record)
        print("Adding tags on DhcpOptions:", record)
        dhcp_description.create_tags(Tags=tags_dictionary)
    except ClientError as e:
        print(e)
os.remove("dhcp-id_list")

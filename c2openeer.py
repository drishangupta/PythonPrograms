# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 18:58:22 2023

@author: drish
"""

import boto3
ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="ami-0ded8326293d3201b",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro"
          )
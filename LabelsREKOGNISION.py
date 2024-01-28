# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 17:36:00 2023

@author: drish
"""

import boto3

def detect_labels(image_path):
    aws_access_key = 'AKIAQIUH7ASYGEB'
    aws_secret_key = 'd7KNbbWTAba2J+ZJ6RNF0ATu+1lwJYoawR4h'

    client = boto3.client('rekognition', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name='ap-south-1')

    
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    response = client.detect_labels(Image={'Bytes': image_bytes})

    return response['Labels']

def main():
    image_path = 'test2.jpeg'
    labels = detect_labels(image_path)
    
    print("Labels in the image:")
    for label in labels:
        print(f"- {label['Name']} (Confidence: {label['Confidence']:.2f}%)")

if __name__ == "__main__":
    main()
"""
this script is used to back up from local to AWS S3 bucket.
boto3 is used to interact with AWS S3.
"""

import boto3

s3 = boto3.resource("s3")
def show_buckets(s3):
    print(s3.buckets.all())  # List all buckets

for bucket in s3.buckets.all():
    print(bucket.name)  # Print each bucket's name



import boto3
import logging
import os

# Read the list of existing buckets
def list_bucket():
    # Create bucket
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        if response:
            print('Bucket exists....')
            for bucket in response['Buckets']:
                print(f' {bucket["Name"]}')
    except Exception as e:
        logging.error(e)
        return False
    return True

# Create bucket
def create_bucket(bucket_name, region):
    try:
        if region == None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration = location)

    except Exception as e:
        logging.error(e)
        return False
    return True

# Upload a file from local system.

def upload_file(file_name, bucket, object_name=None):
    # If object name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except Exception as e:
        logging.error(e)
        return False
    return True

# Read list of buckets
'''
list_bucket()
'''

# Calling create bucket
'''
result_create = create_bucket("jide-2024-test", 'eu-west-2')
if result_create:
    print("Bucket successfully created!")
else:
    print("Bucket FAILED to be created...")
'''

# Upload a file to bucket
result_upload = upload_file("/Users/jide/Desktop/python3cheatsheet.pdf", "jide-2024-test")
if result_upload:
    print("Bucket file uploaded successfully!")
else:
    print("Bucket file upload has failed!")

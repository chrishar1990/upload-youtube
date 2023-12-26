#!/usr/bin/python
import boto3
import os
import subprocess
import argparse


awsID = input('Enter the aws_access_key_id: ')
awsSecret = input('Enter the aws_secret_access_key: ')

s3 = boto3.client('s3', awsID, awsSecret)

# Replace 'your_bucket_name' and 'your_object_key' with the actual bucket name and object key

bucket_name = input('Enter the AWS bucket: ')
object_key = input('Enter the object_key: ') #example: 'Stunning Sunset Seen From The Sea _ Time lapse _ 10 Seconds Video _ Nature Blogs.mp4'
local_file_path = input('Enter the local_file_path: ')  # Path where you want to save the downloaded file locally. example: '/home/treeboy/upload-youtube/ocean.mp4'

#code below uses argparses for input
parser = argparse.ArgumentParser(description='Used for path of file and video path.')
parser.add_argument('--input', required=True, help='Input file path')
args = parser.parse_args()
input_file_path = args.input


# Download the file from S3
#s3.download_file(bucket_name, object_key, local_file_path)
s3.download_file(bucket_name, object_key, input_file_path)

print(f"File downloaded to: {local_file_path}")


#Code below runs the upload_video.py file
file_path = input('Enter the file path (e.g., "example.mov"): ')
title = input('Enter the title: ')
description = input('Enter the description: ')
keywords = input('Enter the keywords (comma-separated): ')
category = input('Enter the category (e.g., 22): ')
privacy_status = input('Enter the privacy status (e.g., private): ')
 # Build the command to run
command = [
    'python3',
    'upload_video.py',
    f'--file={file_path}',
    f'--title="{title}"',
    f'--description="{description}"',
    f'--keywords="{keywords}"',
    f'--category={category}',
    f'--privacyStatus={privacy_status}'
]

try:
    # Run the command using subprocess
    subprocess.run(command, check=True)
except subprocess.CalledProcessError as e:
    print(f'Error: The subprocess exited with code {e.returncode}')

os.remove(local_file_path)
print(f"File now removed ")


import boto3
import os
from botocore.exceptions import ClientError

# Assume role to get temporary credentials
def assume_role(role_arn, session_name):
    sts_client = boto3.client('sts')
    try:
        assumed_role = sts_client.assume_role(
            RoleArn=role_arn,
            RoleSessionName=session_name
        )
        return assumed_role['Credentials']
    except ClientError as e:
        print(f"Error assuming role: {e}")
        return None

# Use the temporary credentials from the assumed role
def get_s3_client_with_role(credentials):
    return boto3.client(
        's3',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken'],
        region_name=os.environ.get('S3_REGION')
    )

def generate_presigned_url(filename, role_arn, session_name='test'):
    # Assume the role to get temporary credentials
    credentials = assume_role(role_arn, session_name)
    if credentials is None:
        return {'msg': 'Error', 'Error': 'Error assuming role'}

    # Use the temporary credentials to create an S3 client
    s3_client = get_s3_client_with_role(credentials)
    
    try:
        # Set parameters for the presigned URL
        response = s3_client.generate_presigned_post(
            Bucket='tempo-traces-bharat',  # Your S3 bucket name
            Key=filename,
            ExpiresIn=10000000,  # Expiration time in seconds
            Conditions=[
                {'success_action_status': '201'},
                ['starts-with', '$key', ''],
                ['content-length-range', 0, 36862720],  # File size between 0 and 35 MB (36,862,720 bytes)
                {'x-amz-algorithm': 'AWS4-HMAC-SHA256'}
            ]
        )
        return response
    except ClientError as e:
        print(f"Error: {e}")
        return {'msg': 'Error', 'Error': 'Error creating presigned URL'}

# Example usage
role_arn = 'arn:aws:iam::011528295974:role/s3-pod'  # The IAM role ARN you provided
filename = 'test.txt'  # You can set this dynamically
result = generate_presigned_url(filename, role_arn, session_name='test')
print(result)

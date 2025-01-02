import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def generate_presigned_url_with_role_assumption(bucket_name, object_name, role_arn, expiration=3600):
    """
    Generate a presigned URL to upload a file to an S3 bucket after assuming a role.
    
    :param bucket_name: string
    :param object_name: string
    :param role_arn: string, the ARN of the IAM role to assume
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string if valid, else None
    """
    # Create an STS client to assume the role
    sts_client = boto3.client('sts')
    
    try:
        # Assume the role
        assumed_role = sts_client.assume_role(
            RoleArn=role_arn,
            RoleSessionName='GeneratePresignedURLSession'
        )
        
        # Retrieve temporary credentials
        credentials = assumed_role['Credentials']
        
        # Use temporary credentials to create an S3 client
        s3_client = boto3.client(
            's3',
            aws_access_key_id=credentials['AccessKeyId'],
            aws_secret_access_key=credentials['SecretAccessKey'],
            aws_session_token=credentials['SessionToken']
        )
        
        # Generate a presigned URL to upload a file
        response = s3_client.generate_presigned_url('put_object',
                                                    Params={'Bucket': bucket_name, 'Key': object_name},
                                                    ExpiresIn=expiration)
        
    except (NoCredentialsError, ClientError) as e:
        print(f"Error: {str(e)}")
        return None
    
    return response

# Example Usage
bucket_name = 'tempo-traces-bharat'
object_name = 'test.txt'  # The object you want to upload
role_arn = 'arn:aws:iam::11113456789:role/test'  # Replace with your role ARN
presigned_url = generate_presigned_url_with_role_assumption(bucket_name, object_name, role_arn)

if presigned_url:
    print(f"Presigned URL for uploading: {presigned_url}")

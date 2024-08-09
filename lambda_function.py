import boto3


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'randomlife-bucket'
    key = 'TODO.txt'

    response = s3.get_object(Bucket=bucket_name, Key=key)
    content = response['Body'].read().decode('utf-8')

    return {
        'statusCode': 200,
        'body': content
    }
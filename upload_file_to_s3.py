import boto3

s3_client = boto3.client('s3')
butcket_name = 'datalake-barbara'
folder_name = 'raw-data'
file_name = 'Data/DADOS'
s3_client.upload_file(file_name, butcket_name, f'{folder_name}/{file_name}')

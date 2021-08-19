import boto3

s3_client = boto3.client('s3')
butcket_name = 'datalake-barbara'
s3_folder_name = 'raw-data/censo'
local_folder_name = 'Data/DADOS'
files_to_upload = [
    # 'matricula_co.csv',
    # 'matricula_nordeste.csv',
    # 'matricula_norte.csv',
    # 'matricula_sudeste.csv',
    # 'matricula_sul.csv'
]

for file_name in files_to_upload:
    s3_client.upload_file(f'{local_folder_name}/{file_name}',
                          butcket_name,
                          f'{s3_folder_name}/{file_name}')

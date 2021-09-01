import boto3
import os
import json
import base64


#kmsclient = boto3.client('kms', region_name='us-east-1')

DB_URL = os.environ['DB_URL']
ENCRYPTED = os.environ['DB_PASSWORD']
# Decrypt code should run once and variables stored outside of the function
# handler so that these are decrypted once per coontainer
#DB_PASSWORD = boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED))['Plaintext']

DECRYPTED = boto3.client('kms').decrypt(
    CiphertextBlob=b64decode(ENCRYPTED),
    EncryptionContext={'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME']}
)['Plaintext'].decode('utf-8')



def lambda_handler(event, context):
    print(DB_URL)
    print(DECRYPTED)
    #print(ENCRYPTED)
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


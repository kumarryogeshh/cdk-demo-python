import json
import os

def handler(event, context):
    print('request:', json.dumps(event))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': f'Hello, CDK! Printing ENV_VAR1 { os.environ.get('ENV_VAR1', 'Unknown')}\n'
    }
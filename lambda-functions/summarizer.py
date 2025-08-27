import json
import os
import boto3
import logging
import textwrap
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

BEDROCK_MODEL_ID = os.environ.get('BEDROCK_MODEL_ID', 'anthropic.claude-2')
MAX_PROMPT_LENGTH = 3000  # Adjust based on model limits

bedrock = boto3.client('bedrock')


def lambda_handler(event, context):
    # event is the JSON we sent from GitHub Action

    title = event.get('title', 'No Title Provided')
    body = event.get('body', 'No Body Provided')
    commits = event.get('commits', []) or []
    diff = event.get('diff', '')

    print(f"Received event: {json.dumps(event)}")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

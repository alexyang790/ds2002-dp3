import boto3
from botocore.exceptions import ClientError
import requests
import json

# Set up your SQS queue URL and boto3 client
url = "https://sqs.us-east-1.amazonaws.com/440848399208/zy7ts"
sqs = boto3.client('sqs')

def get_message():
    try:
        sorted_messages = []
        list_messages = []
        for i in range(10): 
            response = sqs.receive_message(
                QueueUrl=url,
                AttributeNames=[
                    'All'
                ],
                MaxNumberOfMessages=1,
                MessageAttributeNames=[
                    'All'
                ]
            )
            if "Messages" in response:
                stored_messages = {}
                order = response['Messages'][0]['MessageAttributes']['order']['StringValue']
                word = response['Messages'][0]['MessageAttributes']['word']['StringValue']
                handle = response['Messages'][0]['ReceiptHandle']

                stored_messages['order'] = order
                stored_messages['word'] = word
                list_messages.append(stored_messages)

        sorted_messages = sorted(list_messages, key=lambda x: x["order"])
        return sorted_messages

    except ClientError as e:
        print(e.response['Error']['Message'])

def get_phrase(sorted_messages):
    phrase = ''
    for i in range(10):
        phrase = phrase + (sorted_messages[i]['word']) + ' '
    print(phrase)

if __name__ == "__main__":
    sorted_messages = get_message()
    get_phrase(sorted_messages)

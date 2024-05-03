import boto3
from botocore.exceptions import ClientError
import requests
import json

# Set up your SQS queue URL and boto3 client
url = "https://sqs.us-east-1.amazonaws.com/440848399208/zy7ts"
sqs = boto3.client('sqs')

'''
def delete_message(handle):
    try:
        # Delete message from SQS queue
        sqs.delete_message(
            QueueUrl=url,
            ReceiptHandle=handle
        )
        print("Message deleted")
    except ClientError as e:
        print(e.response['Error']['Message'])
'''

def get_message():
    try:
        sorted_messages = []
        list_messages = []
        # Receive message from SQS queue. Each message has two MessageAttributes: order and word
        # You want to extract these two attributes to reassemble the message
        for i in range(10): #looping the get message 10 times
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
            # Check if there is a message in the queue or not
            if "Messages" in response:
                stored_messages = {}
                # extract the two message attributes you want to use as variables
                # extract the handle for deletion later
                order = response['Messages'][0]['MessageAttributes']['order']['StringValue']
                word = response['Messages'][0]['MessageAttributes']['word']['StringValue']
                handle = response['Messages'][0]['ReceiptHandle']

                #store messages in a dictionary then pass on to a list
                stored_messages['order'] = order
                stored_messages['word'] = word
                list_messages.append(stored_messages)
                #reassemble message logic
                sorted_messages = sorted(list_messages, key=lambda x: x["order"])
                print('sorted messages', sorted_messages)
                if i == 9:
                    print('yay')
                    phrase = ''
                    for x in range (10):
                        phrase = phrase + (sorted_messages[x]['word'] + ' ')
                    print(phrase)
            else:
                print("No message in the queue")
                exit(1)

            
        
    # Handle any errors that may occur connecting to SQS
    except ClientError as e:
        print(e.response['Error']['Message'])

# Trigger the function
if __name__ == "__main__":
    get_message()
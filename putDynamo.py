import boto3
import os

def insert(items):
    # initDB
    session = boto3.session.Session(
                                    region_name=os.environ['REGION'],
                                    aws_access_key_id=os.environ['A_KEY'],
                                    aws_secret_access_key=os.environ['S_KEY']
                                    )
    dynamodb = session.resource('dynamodb')


    # connect to Table
    table_name = os.environ['TABLE_NAME']
    table = dynamodb.Table(table_name)

    for item in items:
        # add
        response = table.put_item(
            TableName=table_name,
            Item=item
        )
        if response['ResponseMetadata']['HTTPStatusCode'] != 200:
            # Failed
            print(response)
        else:
            # Succeeded
            print('Succeeded :', item['device'])
    return
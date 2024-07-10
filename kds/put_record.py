import boto3


def main():
    client = boto3.client('kinesis')

    response = client.put_record(
        StreamName='samplestream',
        Data='bytes',
        PartitionKey='PartitionKey',
    )

    print(response)


if __name__=="__main__":
    main()
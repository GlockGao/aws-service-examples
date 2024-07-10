import boto3


def main():
    client = boto3.client('kinesis')

    response = client.list_streams(
        Limit=100,
        ExclusiveStartStreamName='exclusive',
    )

    print(response)


if __name__=="__main__":
    main()
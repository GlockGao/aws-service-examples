import boto3


def main():
    client = boto3.client('kinesis')

    # 1. List shards
    response = client.list_shards(
        StreamName='samplestream',
        MaxResults=100,
    )
    shards = response['Shards']
    for idx, shard in enumerate(shards):
        print('#' * 50)
        print(f"shard id      : {shard['ShardId']}")

        # 2. Get shard iterator
        response = client.get_shard_iterator(
            StreamName='samplestream',
            ShardId=shard['ShardId'],
            ShardIteratorType='TRIM_HORIZON',
        )
        shard_iterator = response['ShardIterator']

        # 3. Get records
        response = client.get_records(
            ShardIterator=shard_iterator,
            Limit=100,
            StreamARN='arn:aws-cn:kinesis:cn-northwest-1:300360861228:stream/samplestream'
        )

        records = response['Records']
        print(f"Record count  : {len(records)}")
        for record in records:
            print(f"SequenceNumber: {record['SequenceNumber']}")
            print(f"PartitionKey  : {record['PartitionKey']}")
            print(f"Data          : {record['Data']}")


if __name__=="__main__":
    main()
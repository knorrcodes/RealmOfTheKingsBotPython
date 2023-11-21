import boto3
import json

def getsecrets():
    client = boto3.client("secretsmanager", "us-east-1")
    out = json.loads(client.get_secret_value(
        SecretId="discord-bot"
    )["SecretString"])
    return (out["DISCORD-TOKEN"], out["PREFIX"])

def getS3Object(type):
    keyName = f"CURRENT_{type.upper()}"
    client = boto3.client("s3")
    resp = client.get_object(
        Bucket="rotk-bot",
        Key=keyName
    )
    return json.loads(resp["Body"].read().decode('utf-8'))

def putS3Object(new_json, old_json, type):
    client = boto3.client("s3")
    first = client.put_object(
        Bucket="rotk-bot",
        Key=f"CURRENT_{type.upper()}",
        Body=json.dumps(new_json).encode("utf-8")
        )
    second = client.put_object(
        Bucket="rotk-bot",
        Key=f"PREVIOUS_{type.upper()}",
        Body=json.dumps(old_json).encode("utf-8")
        )
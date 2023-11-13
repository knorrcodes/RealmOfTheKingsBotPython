import boto3
import json

def getsecrets():
    client = boto3.client("secretsmanager", "us-east-1")
    out = json.loads(client.get_secret_value(
        SecretId="discord-bot"
    )["SecretString"])
    return (out["DISCORD-TOKEN"], out["PREFIX"])

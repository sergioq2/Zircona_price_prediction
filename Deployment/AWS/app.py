import json
from prediction import predict
from preprocess import FeatureEngineering

def handler(event, context):
    body = event['body']
    df = FeatureEngineering(body)
    result = predict(df)
    return result
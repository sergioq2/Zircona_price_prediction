import joblib
import pandas as pd
import json

#path to the encoder and scaler
encoder_url = 'files/encoder.pkl'
scaler_url = 'files/scaler.pkl'

#the encoder and scaler are loaded
encoder = joblib.load(encoder_url)
scaler = joblib.load(scaler_url)
categorical = encoder.feature_names_in_

#this function preprocess the data using the encoder and scaler previously loaded
def feature_preprocess(df):
    encoded_df = pd.DataFrame(
        encoder.transform(df[categorical]),
        columns=encoder.get_feature_names_out(categorical)
    )
    df = pd.concat([df.drop(categorical, axis=1), encoded_df], axis=1)

    scaled_df = pd.DataFrame(
        scaler.transform(df),
        columns=df.columns
    )
    return scaled_df

#the funcion read the json data and return a dataframe with the data preprocessed
def FeatureEngineering(json_data):
    data = json.loads(json_data)
    df = pd.DataFrame(data, index=[0])
    df = feature_preprocess(df)
    return df

if __name__ == '__main__':
    FeatureEngineering()
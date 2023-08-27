import joblib

#the model is loaded from the files folder
model = joblib.load('files/model.pkl')

#the prediction function is defined
def predict(df):
    prediction_result = model.predict(df)[0]
    return prediction_result

if __name__ == '__main__':
    predict()
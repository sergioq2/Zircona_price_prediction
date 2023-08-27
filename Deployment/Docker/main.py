import joblib
from preprocessing import FeatureEngineering

#the model is loaded from the files folder
model = joblib.load('files/model.pkl')

#the prediction function is defined
def prediction(value):
    #the value is passed to the FeatureEngineering function
    df = FeatureEngineering(value)
    #the prediction is made with the model
    prediction_result = model.predict(df)[0]
    return prediction_result

if __name__ == '__main__':
    prediction()
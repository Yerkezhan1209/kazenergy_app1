import joblib
def predict(data):
	prediction_model = joblib.load('finalized_model.sav')
	return prediction_model.predict(data)
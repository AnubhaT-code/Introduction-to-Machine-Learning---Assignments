import numpy as np
import pickle as pkl
from  sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import RandomForestRegressor

# Define your prediction method here
# df is a dataframe containing timestamps, weather data and potentials
def my_predict(df):
    
	# something to do to data
	X_test = df[["temp","humidity","no2op1","no2op2","o3op1","o3op2"]]
	

	# Load your model file
	model = pkl.load(open('model.pkl', 'rb'))
	
	y_pred = model.predict(X_test)
	pred_o3 = y_pred[:,0]
	pred_no2 = y_pred[:,1]
	

	# Return both sets of predictions
	return (pred_o3, pred_no2)
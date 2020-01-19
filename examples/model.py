# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import json
from Homomorphic.Encryption import EncryptorBits
from sklearn.linear_model import LinearRegression

##############################################################################
#READING THE DATA FROM THE API, GETS THE DATA IN BASE64 OF THE ENCRYPTED DATA#
##############################################################################
my_data_file = open('dataset.json', 'w')
Dataset_ = requests.get("http://127.0.0.1:6062/getdata")
Dataset_= Dataset_.text
Dataset_= Dataset_.strip("'<>() ").replace('\'', '\"').replace('b', '')
my_data_file.write(Dataset_)

#####################################################
#STORING THE ENTIRE CSV IN A JSON OF ENCRYPTED VALES#
#####################################################
data_dict= dict()
with open('dataset.json') as json_file:
    data_dict = json.load(json_file)

##############################################
#CREATING THE HOMOMORPHIC ENCRYPTION INSTANCE#
##############################################

"""
dataset = pd.read_csv('Dataset/diabetes.csv')
dataset = dataset[dataset.Insulin != 0]
dataset=dataset[dataset.SkinThickness!=0]
X=dataset.drop(columns='Outcome')

Y=dataset.iloc[:,-1]
Y=np.array(Y)

regressor = LinearRegression()
regressor.fit(X, Y)
regressor.predict(np.array([4,120,70,20,100,23,1,30]).reshape(1,-1))
pickle.dump(regressor, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
""" 
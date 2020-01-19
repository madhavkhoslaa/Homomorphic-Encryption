# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('Dataset\diabetes.csv')
print(dataset)

dataset = dataset[dataset.Insulin != 0]
dataset=dataset[dataset.SkinThickness!=0]
X=dataset.drop(columns='Outcome')

Y=dataset.iloc[:,-1]
Y=np.array(Y)
print(X)
print(Y)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, Y)
regressor.predict(np.array([4,120,70,20,100,23,1,30]).reshape(1,-1))

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
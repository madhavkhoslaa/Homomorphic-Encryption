import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Pregnancies':2, 'Glucose':100, 'BloodPressure':70 ,'SkinThickness':20 ,'Insulin':250,'BMI':25,'DiabetesPedigreeFunction':0.5,'Age':20})

print(r.json())
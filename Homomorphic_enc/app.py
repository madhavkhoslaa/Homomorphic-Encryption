import numpy as np
from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = np.array(int_features).reshape(1,-1)
    print('int wala: ', int_features)
    print('final : ', final_features)
    
    prediction = model.predict(final_features)
    
   
    print('pred ', prediction)
        
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='The outcome of diabetes prediction is {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
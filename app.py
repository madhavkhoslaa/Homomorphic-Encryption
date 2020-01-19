from flask import Flask 
from Homomorphic.Encryption import EncryptorBits
from utils.SerDe import SerDe
from flask import jsonify
from flask import request
import flask
import pandas

DATASET= "Dataset/diabetes.csv"
A= EncryptorBits()
app = Flask(__name__) 
PRIVATE, PUBLIC= A.private_key, A.public_key
x= SerDe()
@app.route('/Encrypt') 
def Encrypt(): 
    data = flask.request.json["Vector"]
    return str(x.Serialise(A.encryptArray(data)))

@app.route('/Deserialise', methods= ['GET'])
def Deserialise():
    data = flask.request.json
    y= A.decryptArray(x.Deserialise(data))
    return str(y)
    
@app.route('/Decrypt')
def Decrypt():
    data = flask.request.json
    ss= x.Deserialise(data)
    """
    A.private_key= data["private"]
    A.public_key= data["public"]"""
    return str(ss)
@app.route('/getdata')
def getdataset():
    ds= pandas.read_csv(DATASET)
    data_dict= {}
    for _ in ds[0:0]:
        print(_)
        data_dict[_] = x.Serialise(A.encryptArray(ds[_]))
    print(data_dict)
    return str(data_dict)


if __name__ == '__main__':
    app.run(debug=True, port= 3234) 

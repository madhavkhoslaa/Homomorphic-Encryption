from flask import Flask, request
from flask_restful import Resource, Api
import pandas


app = Flask(__name__)
api = Api(app)
todos = {}
dataset= pandas.read_csv("Dataset/diabetes.csv")
class GetData(Resource):
    def get(self, start_stop):
        start, stop= start_stop.split("-")
        print(dataset.iloc[start: stop])

    def put(self):
        pass

api.add_resource(GetData, '/<string:start_stop>')

if __name__ == '__main__':
    app.run(debug=True, port=6969)
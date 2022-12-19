import os

from flask import Flask, request
from flask_restful import Resource, Api
from main import *
app = Flask(__name__)
api = Api(app)


class PredictJson(Resource):
    def post(self):
        file = request.files['file']
        file.save(file.filename)
        img_array = prep_img(file.filename)
        predicted = predict(img_array)[1]
        os.remove(file.filename)
        return predicted


class PredictHtml(Resource):
    def post(self):
        file = request.files['file']
        file.save(file.filename)
        img_array = prep_img(file.filename)
        predicted = predict(img_array)[0]
        os.remove(file.filename)
        return predicted


api.add_resource(PredictJson, '/json')
api.add_resource(PredictHtml, '/html')

if __name__ == '__main__':
    app.run(debug=True)
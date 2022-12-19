import os

from flask import Flask, render_template, request, send_from_directory
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template("index.html")


@app.route('/data', methods=['POST'])
def handle_data():
    file = request.files['file']
    file.save(file.filename)
    files = {'file': open(file.filename, 'rb')}
    response = requests.post("http://host.docker.internal:5000/html", files=files)
    os.remove(file.filename)
    return response.text


app.run('0.0.0.0', port=80)
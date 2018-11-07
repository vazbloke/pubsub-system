from flask import Flask, render_template, redirect, url_for, request, jsonify
# from pymongo import MongoClient
from subprocess import Popen, PIPE
import requests, json, socket

app = Flask(__name__)

# Making connection to locally hosted MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client.roadtrip_buddy
# weather_c = db.weather_c
# map_c = db.map_c

hostname=socket.gethostname()

@app.route('/')
def home():
    return render_template('frontend/index.html', hostname = hostname)

@app.route('/runcode', methods=['POST'])
# API to handle POST request for Maps sent by client
def runcode():
    data =json.loads(request.data)

    # Code below
    print(data['code'])

    # Subprocess run code
    f = open("test.py", "w")
    f.write(data['code'])
    f.close()
    process = Popen(['python', 'test.py'], stdout=PIPE, stderr=PIPE)

    stdout, stderr = process.communicate()

    print(type(stdout))
    
    returnval = '{"key":"'+stdout[:-1]+'"}'
    print(returnval)
    return jsonify(stdout)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)

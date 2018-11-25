from flask import Flask, render_template, redirect, url_for, request, jsonify
from subprocess import Popen, PIPE
import requests, json, socket, os, sys

from publish import Publish
from db import DB
from subscribe import Subscribe

app = Flask(__name__)

hostname=socket.gethostname()

@app.route('/')
def index():
    return render_template('frontend/index.html', hostname = hostname)

@app.route('/publisher')
def publisher():
    return render_template('frontend/publisher.html', hostname = hostname)

@app.route('/subscriber')
def subscriber():
    return render_template('frontend/subscriber.html', hostname = hostname)

@app.route('/addsub', methods=['POST'])
def addsub():
    data =json.loads(request.data)
    print(data)
    Subscribe().subscribe(data['subemail'], data['events'])
    return jsonify("nothing")

@app.route('/addpublish', methods=['POST'])
def addpublish():
    data =json.loads(request.data)
    print(data)
    Publish().publish_event(data['events'], data['eventmessage'])
    return jsonify("nothing")

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port=80)

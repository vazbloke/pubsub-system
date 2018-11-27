from flask import Flask, render_template, redirect, url_for, request, jsonify
from subprocess import Popen, PIPE
import requests, json, socket, sys

app = Flask(__name__)

hostname=socket.gethostname()

@app.route('/')
def home():
    return render_template('frontend/index.html', hostname = hostname)

@app.route('/runcode', methods=['POST'])
def runcode():
    data =json.loads(request.data)

    # Subprocess run code
    f = open("test.py", "w")
    f.write(data['code'])
    f.close()
    process = Popen(['python', 'test.py'], stdout=PIPE, stderr=PIPE)

    stdout, stderr = process.communicate()
    if stderr:
        # print("Error.", file=sys.stderr)
        return jsonify("ERROR!")
    else:
        # print("Executed.", file=sys.stderr)
        return jsonify(stdout)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)

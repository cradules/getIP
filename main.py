import socket
import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config['DEBUG'] = True


def getData():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return hostname, ip_address


@app.route('/', methods=['GET'])
def index():
    try:
        return jsonify(getData())
    except Exception as e:
        return jsonify(e)


app.run(host='0.0.0.0', port=5000)

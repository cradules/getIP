import socket
from flask import Flask
from flask import jsonify
import time

app = Flask(__name__)
app.config['DEBUG'] = True


def get_data():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return hostname, ip_address


@app.route('/', methods=['GET'])
def index():
    try:
        time.sleep(5)
        return jsonify(get_data())
    except Exception as e:
        return jsonify(e)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

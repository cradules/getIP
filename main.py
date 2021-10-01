import socket
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True


def get_data():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return hostname, ip_address


if __name__ == "__main__":
    app.run(host='0.0.0.0')

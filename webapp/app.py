import os
import socket
import subprocess

from flask import Flask
from requests import get

app = Flask(__name__)


@app.route('/')
def hello():
    hostname = socket.gethostname()
    ip = get('https://api.ipify.org').text
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.log")) as f:
        message = f.readlines()[-20:]
    return f"Hello from: {ip} on: {hostname}." + '<br>' + '<p><a href="https://peer2profit.io/r/164181619061dc207e974f9" rel="noopener noreferrer" target="_blank">Check it</a></p>' + '<br>'.join(message)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

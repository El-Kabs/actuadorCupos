import requests
import time
from flask import Flask
from flask_cors import CORS, cross_origin
import threading

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def ingresar():
    while True:
        print('Comienzo')
        requests.get('https://cupouniandes.herokuapp.com/escribir')
        print('Fin R')
        print('Fin')
        
@app.route("/")
@cross_origin()
def comenzar():
    threads = list()
    t = threading.Thread(target=ingresar)
    threads.append(t)
    t.start()
    return ("OK")

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')

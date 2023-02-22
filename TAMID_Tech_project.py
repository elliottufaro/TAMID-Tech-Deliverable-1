#from flask import Flask, request, jsonify
import flask

app = flask.Flask(_name_)

from waitress import serve
import logging 
logger = logging.getLogger('waitress')

logger.setLevel(logging.INFO)

@app.route('/get', methods = ['GET'])
def testGet():
    return flask.jsonify ('message', 'test works')

@app.route('/post', methods =['POST'])
def testPost():
    data = flask.request.json
    print(data)
    return 'POST works'

@app.route('/')
def is_up():
        return 'Server is up'

if __name__=='__main__':
    serve(app, host = '0.0.0.0', port=8080)
    
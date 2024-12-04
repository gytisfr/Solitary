import flask, requests, dbint
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def main():
    return flask.render_template('index.html')

@app.route('/db')
def db():
    db = {}
    currin = dbint.currin.fetch()
    print(currin)
    db["users"] = {el[0]: el[1] for el in currin}
    payload = dbint.payload.fetch()
    db["payload"] = [el for el in payload]
    return db

app.run('127.0.0.1', port=8117, debug=True)
#0.0.0.0
#http://51.222.117.190:8117/db
from AccountManager import *
from flask import Flask, request, jsonify
import json

am = AccountManager()

app = Flask(__name__)

@app.route('/api/accounts', methods=['GET'])
def getAccounts():
    return jsonify(am.listAccounts())

@app.route('/api/accounts/<name>', methods=['POST'])
def addAccount(name):
    return { "message": am.addAccount(name) }

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
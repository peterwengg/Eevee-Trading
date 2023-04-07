#!/usr/bin/env python3
# The above shebang (#!) operator tells Unix-like environments
# to run this file as a python3 script

from flask import Flask
import json
import os
import requests
import pyrebase
import helpers


app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')

firebase_config = {
    "apiKey": "AIzaSyAUfijsgUQsPpdx5A21wO0wCS1qRkwh5o0",
    "authDomain": "cryptobuds-ba428.firebaseapp.com",
    "databaseURL": "https://cryptobuds-ba428-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "cryptobuds-ba428",
    "storageBucket": "cryptobuds-ba428.appspot.com",
    "messagingSenderId": "72206190161",
    "appId": "1:72206190161:web:bc8dbb3bf116fcc69fda70",
    "measurementId": "G-BVXDMYJR2K"
}

fb = pyrebase.initialize_app(firebase_config)
database = fb.database()

@app.route('/transactions')
def checkTransactionLog():
    print("--- Transaction Log invoked, retrieving transactions details.. ---")
    id = helpers.retrieveHelperVal('uID', 'helpers.txt')
    retrieved_info = database.child("users").child(id).child('transactions').get()
    key = (next(iter(retrieved_info.val())))
    retrieved_info = retrieved_info.val()[key]
    print(retrieved_info)
    return retrieved_info

if __name__ == "__main__":
    print("\nThis is " + os.path.basename(__file__) + " microservice", end='')
    app.run(host='0.0.0.0', port=5006, debug=True)
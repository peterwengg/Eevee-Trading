from invokes import invoke_http
from flask import Flask, request, jsonify, redirect
import os, json
import requests
from flask_cors import CORS
import helpers
# import amqp_setup
# import pika

import pyrebase

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

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

@app.route("/swap", methods = ['GET'])
def swap():
    from_amount = request.args.get('from_amount')
    from_currency = request.args.get("from_currency")
    to_currency = request.args.get("to_currency")

    from_price_URL = f"http://127.0.0.1:5001/coin/{from_currency}"
    to_price_URL = f"http://127.0.0.1:5001/coin/{to_currency}"

    conversion_ratio = getRatio(from_price_URL, to_price_URL)
    gas_fee = 0.01
    if from_currency == to_currency:
        gas_fee = 0 

    conversion_amount = float(from_amount) * float(conversion_ratio) * float(1 - gas_fee)
    to_amount = request.args.get("to_amount")

    #Status of successful swap
    if conversion_amount:
        #AMQP activity

        return {
            "code": 200,
            'conversion_amount': conversion_amount
        }

    #Status of failed swap
    else:
        #AMQP activity

        return {
            "code": 400,
            "message": "Swap failure sent for error handling."
        }
    
def getPrice(response):
    price = response['data']['price']
    return price

# Obtain rates from price.py and calculates ratio of swap (to rate / from rate)
def getRatio(from_url, to_url):
    
    to_price_data = requests.get(to_url)
    from_price_data = requests.get(from_url)
    from_price = None
    to_price = None
    
    if to_price_data:
        to_price_data = to_price_data.json()
        to_price = getPrice(to_price_data)
    if from_price_data:
        from_price_data = from_price_data.json() 
        from_price = getPrice(from_price_data) 
    return (from_price / to_price)


# Calls wallet to update balance and retrieve . 
'''
Takes in four arguments - type (retrieve / update), from_currency, to_currency and user_email 
Returns json in format of "updated <coin>" : updated balance 
'''

@app.route("/update", methods = ['GET'])
def updateWallet():
    wallet_URL = "http://host.docker.internal:5100/wallet/"
    id = helpers.retrieveHelperVal('uID','helpers.txt')
    from_currency = request.args.get('from_currency')
    from_amount = request.args.get('from_amount')
    to_currency = request.args.get('to_currency')
    to_amount = request.args.get('to_amount')

    old_from_balance = None
    old_to_balance = None
    updated_from_balance = None
    updated_to_balance = None

    # Calls access_wallet to update from_amount and get new balance
    coin = from_currency
    url1 = wallet_URL+coin
    old_from_balance = requests.get(url1)
    if old_from_balance:
        ownedcoin = old_from_balance.json()
        ownedcoin = getNumber(ownedcoin)
        old_from_balance = ownedcoin
        print(old_from_balance)
        changed_amt = ownedcoin - float(from_amount)
        updated_from_balance = changed_amt
        print(changed_amt)
        database.child("users").child(id).child('wallet_coins').child(from_currency).update({"qty":changed_amt})
        
        # Retrieves updated balance from firebase 
        updated_from_data = database.child("users").child(id).child('wallet_coins').child(from_currency).get()

    # transaction, transaction_log, amqp, docker
    # Calls access_wallet to update to_amount and get new balance
        coin = to_currency
        url2 = wallet_URL + coin
        old_to_balance = requests.get(url2)
        if old_to_balance:
            ownedcoin = old_to_balance.json()
            ownedcoin = getNumber(ownedcoin)
            old_to_balance = ownedcoin
            print(old_to_balance)
            changed_amt2 = ownedcoin + float(to_amount)
            updated_to_balance = changed_amt2
            database.child("users").child(id).child('wallet_coins').child(to_currency).update({"qty":changed_amt2})

            # Retrieves updated balance from firebase 
            updated_to_data = database.child("users").child(id).child('wallet_coins').child(to_currency).get()

        # Checks db update status and publishes message to rabbitmq
            # if updated_from_data != None and updated_to_data != None:
            #     if updated_to_data.val()['qty'] == updated_to_balance and updated_from_balance.val()['qty'] == updated_from_balance:
            #         message = jsonify({"success": True, "message": "New to balance updated successfully!"})
            #         # amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="*", body=message, properties=pika.BasicProperties(delivery_mode = 2))
            #     else:   
            #         message = jsonify({"success": False, "message": "Failed to update new to balance!"})
            #         # amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="swap.error", body=message, properties=pika.BasicProperties(delivery_mode = 2))

            # Returns new and old wallet balance for to and from currency
            input1 = "old " + from_currency
            input2 = "old " + to_currency
            input3 = "updated " + from_currency
            input4 = "updated " + to_currency

            code = '200'
            message = 'successfully updated swap transaction in wallet!'
            reply = {
                    'code' : code,
                    'message' : message,
                    'data':{
                    input1 : old_from_balance,
                    input2 : old_to_balance,
                    input3 : updated_from_balance,
                    input4 : updated_to_balance,
                    }   
                }
            
            if not updated_to_data.val()['qty']:
                code = '404'
                message = 'unsuccessful update of swap transaction in wallet.'
                reply = {
                        'code' : code,
                        'message' : message
                    }
            
            if updated_to_data.val()['qty']:
                return redirect('http://127.0.0.1:5000/swapsuccess')
            else:
                return redirect('http://127.0.0.1:5000/swapfail')

def getNumber(amount_owned):
    return amount_owned

if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__))
    app.run(host="0.0.0.0", port=5004, debug=True)

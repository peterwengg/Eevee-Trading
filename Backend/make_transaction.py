# make_transaction complex Microservice
# have to invoke wallet.py to check wheter got enough $$ to eg buy cc defined

from flask import Flask, redirect, render_template, url_for, request, jsonify
from flask_cors import CORS
import time
import pyrebase
import os, sys
from os import environ
import helpers
import requests
from invokes import invoke_http
from datetime import datetime
import pika
import json

app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static', static_url_path='')
CORS(app)

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


#set up RabbitMQ Connec tion
# connection = pika.BlockingConnection(pika.ConnectionParameters('host.docker.internal'))
# channel = connection.channel()
# channel.queue_declare(queue='buy_order_queue')
marketplace_URL = "http://host.docker.internal:5000/marketplace"
price_URL = "http://host.docker.internal:5001" 
# buy_transaction_URL = "http://host.docker.internal:5004/" 
# sell_transaction_URL = "http://host.docker.internal:5004/" 



def dummy(qty):
    return float(qty)

def getPrice(response):
    price = response['data']['price']
    price = str(price)
    return price

def getNumber(number):
    return number

# #BINANCE
@app.route("/BNB")
def binance():
    return render_template('coins/bnb.html')

#BITCOIN
@app.route("/BTC")
def bitcoin():
    return render_template('coins/btc.html')

#CARDANO
@app.route("/ADA")
def cardano():
    return render_template('coins/ada.html')

#DOGE
@app.route("/DOGE")
def doge():
    return render_template('coins/doge.html')

#ETHEREUM
@app.route("/ETH")
def ethereum():
    return render_template('coins/eth.html')

# SOLANA
@app.route("/SOL")
def solana():
    return render_template('coins/sol.html')


@app.route("/<string:coin>/buy")
def buycc(coin):
    qty = request.args.get('buyqty')
    qty = dummy(qty)
    price_URL = "http://host.docker.internal:5001" 
    price_URL = price_URL + "/coin/" + coin
    wallet_USD = "http://host.docker.internal:5100/wallet/USD"
    wallet_URL = "http://host.docker.internal:5100/wallet/" + coin
    #get price
    response = requests.get(price_URL, timeout=10)
    #get USD owned
    amount_owned = requests.get(wallet_USD, timeout=10)
    
    if response:
        #get total price needed to pay with current price + quantity
        response = response.json()
        price = getPrice(response)
        print(price)
        total_amount = round(float(qty) * float(price),2)
        print(total_amount)

    if amount_owned:
        amount_owned = amount_owned.json()
        qty_usd_owned = getNumber(amount_owned)
        print(qty_usd_owned)

    if qty_usd_owned >= total_amount:
        qty_coin_owned = requests.get(wallet_URL)
        if qty_coin_owned:
            id = helpers.retrieveHelperVal('uID','helpers.txt')
            ownedcoin = qty_coin_owned.json()
            ownedcoin = getNumber(ownedcoin)
            print(ownedcoin)
            decrease = qty_usd_owned - total_amount
            print(decrease)
            increase = float(ownedcoin) + float(qty)
            print(increase)
            database.child("users").child(id).child('wallet_coins').child("USD").update({"qty":decrease})
            database.child("users").child(id).child('wallet_coins').child(coin).update({"qty": increase})
            transaction_type = 'buy'
            time = datetime.now()
            data = {"userid": id, "date": str(time), "transaction_type": transaction_type, "purchase_quantity": qty, "purchase_price": price, "total_spent": total_amount, 'coin': coin }
            print(data)
            database.child("users").child(id).child('transactions').push(data)
            code = 200
        else:
            code = 400
    else:
        code = 400

    if code == 200:
        return redirect(f'http://host.docker.internal:5000/thanksbuy')
    else:
        return redirect(f'http://host.docker.internal:5000/errorbuy')
    

@app.route("/<string:coin>/sell")
def sellcc(coin):
    qty = request.args.get('sellqty')
    qty = dummy(qty)
    price_URL = "http://host.docker.internal:5001" 
    price_URL = price_URL + "/coin/" + coin
    wallet_USD = "http://host.docker.internal:5100/wallet/USD"
    wallet_URL = "http://host.docker.internal:5100/wallet/" + coin
    #get price
    response = requests.get(price_URL, timeout=10)
    coin_owned = requests.get(wallet_URL)

    if coin_owned:
        coin_owned = coin_owned.json()
        qty_coin_owned = getNumber(coin_owned)
        print(qty_coin_owned)

    if response:
        #get total price needed to pay with current price + quantity
        response = response.json()
        price = getPrice(response)
        print(price)
        total_amount = round(float(qty) * float(price),2)
        print(total_amount)

    if qty_coin_owned >= float(qty):
        amount_owned = requests.get(wallet_USD)
        if amount_owned:
            id = helpers.retrieveHelperVal('uID','helpers.txt')
            qty_usd_owned = amount_owned.json()
            qty_usd_owned = getNumber(qty_usd_owned)
            print(qty_usd_owned)
            decrease = float(qty_coin_owned) - float(qty)
            increase = qty_usd_owned + total_amount
            print(decrease)
            print(increase)
            database.child("users").child(id).child('wallet_coins').child("USD").update({"qty":increase})
            database.child("users").child(id).child('wallet_coins').child(coin).update({"qty": decrease})
            transaction_type = 'sell'
            time = datetime.now()
            data = {"userid": id, "date": str(time), "transaction_type": transaction_type, "sell_quantity": qty, "sell_price": price, "total_earned": total_amount, 'coin': coin }
            print(data)
            database.child("users").child(id).child('transactions').push(data)          
            code = 200
        else:
            code = 400
    else:
        code = 400
    
    if code == 200:
        return redirect(f'http://host.docker.internal:5000/thankssell')
    else:
        return redirect(f'http://host.docker.internal:5000/errorsell')


@app.route("/<string:coin>/buyorder")
def buyordercc(coin):
    boqty = request.args.get('buyorderqty')
    boqty = dummy(boqty)
    boprice = request.args.get('buyorderprice')
    boprice = dummy(boprice)
    wallet_USD = "http://host.docker.internal:5100/wallet/USD"
    wallet_URL = "http://host.docker.internal:5100/wallet/" + coin

    price_URL = "http://host.docker.internal:5001" 
    price_URL = price_URL + "/coin/" + coin
    response = requests.get(price_URL, timeout=10)

    #1. get total amount needed
    total_amount_needed = float(boqty) * float(boprice)
    #2. get wallet balance in USD
    total_usd_owned = requests.get(wallet_USD, timeout=10)
    #3. compare --> if wallet balance >= total amount --> place in order/ create order details
    if total_usd_owned:
        total_usd_owned = total_usd_owned.json()
        total_usd_owned = getNumber(total_usd_owned)

        if total_usd_owned >= total_amount_needed:
            #place order
            id = helpers.retrieveHelperVal('uID','helpers.txt')
            database.child('users').child(id).child('buyorders').child(coin).update({"ordercoin":coin})
            database.child('users').child(id).child('buyorders').child(coin).update({"buy_price":boprice})
            database.child('users').child(id).child('buyorders').child(coin).update({"buy_quantity":boqty})
            database.child('users').child(id).child('buyorders').child(coin).update({"total_amount_required":total_amount_needed})
            code = 200
        else:
            code = 400
    else:
            code = 400

    if code == 200:
        return redirect(f'http://host.docker.internal:5000/thanksbuyorder')
    else:
        return redirect(f'http://host.docker.internal:5000/errorbuyorder')

@app.route("/<string:coin>/sellorder")
def sellordercc(coin):
    soqty = request.args.get('sellorderqty')
    soqty = dummy(soqty)
    soprice = request.args.get('sellorderprice')
    soprice = dummy(soprice)
    wallet_USD = "http://host.docker.internal:5100/wallet/USD"
    wallet_URL = "http://host.docker.internal:5100/wallet/" + coin
    price_URL = "http://host.docker.internal:5001" 
    price_URL = price_URL + "/coin/" + coin
    response = requests.get(price_URL, timeout=10)
    #get USD owned
    total_usd_owned = requests.get(wallet_USD, timeout=10)
    #2. get qty owned
    total_coin_owned = requests.get(wallet_URL, timeout=10)
    #3. compare --> if qty owned >= qty sold --> place in order/ create order details
    if total_coin_owned:
        total_coin_owned = total_coin_owned.json()
        total_coin_owned = getNumber(total_coin_owned)
        if total_coin_owned >= soqty:
            total_amount_gained = soqty * soprice
            id = helpers.retrieveHelperVal('uID','helpers.txt')
            database.child('users').child(id).child('sellorders').child(coin).update({"ordercoin":coin})
            database.child('users').child(id).child('sellorders').child(coin).update({"sell_price":soprice})
            database.child('users').child(id).child('sellorders').child(coin).update({"sell_quantity":soqty})
            database.child('users').child(id).child('sellorders').child(coin).update({"total_amount_earned":total_amount_gained})
            code = 200
        else:
            code = 400
    else:
        code = 400

    if code == 200:
        return redirect(f'http://host.docker.internal:5000/thankssellorder')
    else:
        return redirect(f'http://host.docker.internal:5000/errorsellorder')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5010, debug=True)










# Price Microservice to show different CC prices on diff cc pages
from flask import Flask, redirect, render_template, url_for, jsonify
import requests
from flask_cors import CORS
import os

app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')
CORS(app)

# invoke Crytocompare API to get different pricing according to specific CC
@app.route("/coin/SOL")
def getSOLSinglePrice():
    print("\n--- Checking pricing for SOL ---")
    singlePriceUrl = 'https://min-api.cryptocompare.com/data/price?fsym=SOL&tsyms=USD&api_key=b6d25f96f139bef5f924e987f529a010daf1b3f4faf934b6a02d671becf8ac3d'
    response = requests.get(singlePriceUrl) 
    price = response.json()["USD"]
    print(f"--- Status Code: {response.status_code}: {response.reason} ---")
    print(f"Price retrieved for SOL: {price}USD")

    if requests.get(singlePriceUrl) != "":
        price = response.json()["USD"]
        return jsonify(
            {
                "code": 200,
                "data": {
                    "price": price
                }
            }
        )
    return jsonify ( 
        {
            'code': 404,
            'message': "Error in retrieving SOL price"
        }
    ), 404
    

@app.route("/coin/BNB")
def getBNBSinglePrice():
    print("\n--- Checking pricing for BNB ---")
    singlePriceUrl = 'https://min-api.cryptocompare.com/data/price?fsym=BNB&tsyms=USD&api_key=b6d25f96f139bef5f924e987f529a010daf1b3f4faf934b6a02d671becf8ac3d'
    response = requests.get(singlePriceUrl) 
    price = response.json()["USD"]
    print(f"--- Status Code: {response.status_code}: {response.reason} ---")
    print(f"Price retrieved for BNB: {price}USD")

    if price:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "price": price
                }
            }
        )
    return jsonify ( 
        {
            'code': 404,
            'message': "Error in retrieving BNB price"
        }
    ), 404

@app.route("/coin/BTC")
def getBTCSinglePrice():
    print("\n--- Checking pricing for BTC ---")
    singlePriceUrl = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD&api_key=b6d25f96f139bef5f924e987f529a010daf1b3f4faf934b6a02d671becf8ac3d'
    response = requests.get(singlePriceUrl) 
    price = response.json()["USD"]
    print(f"--- Status Code: {response.status_code}: {response.reason} ---")
    print(f"Price retrieved for BTC: {price}USD")

    if price:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "price": price
                }
            }
        )
    return jsonify ( 
        {
            'code': 404,
            'message': "Error in retrieving BTC price"
        }
    ), 404


@app.route("/coin/ADA")
def getADASinglePrice():
    print("\n--- Checking pricing for ADA ---")
    singlePriceUrl = 'https://min-api.cryptocompare.com/data/price?fsym=ADA&tsyms=USD&api_key=b6d25f96f139bef5f924e987f529a010daf1b3f4faf934b6a02d671becf8ac3d'
    response = requests.get(singlePriceUrl) 
    price = response.json()["USD"]
    print(f"--- Status Code: {response.status_code}: {response.reason} ---")
    print(f"Price retrieved for ADA: {price}USD")

    if price:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "price": price
                }
            }
        )
    return jsonify ( 
        {
            'code': 404,
            'message': "Error in retrieving ADA price"
        }
    ), 404


@app.route("/coin/DOGE")
def getDOGESinglePrice():
    print("\n--- Checking pricing for DOGE ---")
    singlePriceUrl = 'https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD&api_key=b6d25f96f139bef5f924e987f529a010daf1b3f4faf934b6a02d671becf8ac3d'
    response = requests.get(singlePriceUrl) 
    price = response.json()["USD"]
    print(f"--- Status Code: {response.status_code}: {response.reason} ---")
    print(f"Price retrieved for DOGE: {price}USD")

    if price:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "price": price
                }
            }
        )
    return jsonify ( 
        {
            'code': 404,
            'message': "Error in retrieving DOGE price"
        }
    ), 404

@app.route("/coin/ETH")
def getETHSinglePrice():
    print("\n--- Checking pricing for ETH ---")
    singlePriceUrl = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD&api_key=b6d25f96f139bef5f924e987f529a010daf1b3f4faf934b6a02d671becf8ac3d'
    response = requests.get(singlePriceUrl) 
    price = response.json()["USD"]
    print(f"--- Status Code: {response.status_code}: {response.reason} ---")
    print(f"Price retrieved for ETH: {price}USD")

    if price:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "price": price
                }
            }
        )
    return jsonify ( 
        {
            'code': 404,
            'message': "Error in retrieving ETH price"
        }
    ), 404
    
# with app.app_context():
#      print(getSOLSinglePrice())
#      print(getETHSinglePrice())
#      print(getADASinglePrice())
#      print(getDOGESinglePrice())
#      print(getBTCSinglePrice())
#      print(getBNBSinglePrice())

if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host='0.0.0.0', port=5001, debug=True)

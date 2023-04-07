from flask import Flask
from flask_cors import CORS
import pika
import json
import pyrebase
import os
import helpers
import requests
import threading
# import amqp_setup

app = Flask(__name__)
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

def dummy(lel):
    price = lel.json()['data']['price']
    return float(price)

def checkBuyOrderStatus():
    threading.Timer(5.0, checkBuyOrderStatus).start()
    if os.path.exists('helpers.txt')==True:
        id = helpers.retrieveHelperVal('uID','helpers.txt')
        orderlist = database.child('users').child(id).child('buyorders').get()
        print(orderlist.val())
        if orderlist.val() == None:
            pass
        else:
            for order in orderlist:
                order = order.val()
                coin_of_interest = order['ordercoin']
                current_coin_pricing = requests.get('http://host.docker.internal:5001/coin/' + coin_of_interest)
                if current_coin_pricing:
                    current_coin_pricing = dummy(current_coin_pricing)
                    if current_coin_pricing <= order['buy_price']:
                        buy=requests.get('http://host.docker.internal:5010/'+ coin_of_interest + '/buy?buyqty=' + str(order['buy_quantity']))
                        if buy:
                            total_amount_spent = float(order['buy_quantity']) * current_coin_pricing
                            database.child('users').child(id).child('buyorders').remove(coin_of_interest)

                            order = {'buy_price': current_coin_pricing, 'buy_quantity': buy['buy_quantity'], 'ordercoin': buy['ordercoin'], 'total_amount_spent': total_amount_spent}
                            # amqp_setup.channel.basic_publish(exchange=amqp_setup.RABBITMQ_BUY_EXCHANGE, routing_key='', body=json.dumps(order))
                            # # Close RabbitMQ connection
                            # amqp_setup.connection.close()

                    else:
                        pass
                else:
                    pass



def checkSellOrderStatus():
    threading.Timer(5.0, checkSellOrderStatus).start()
    if os.path.exists('helpers.txt')==True:
        id = helpers.retrieveHelperVal('uID','helpers.txt')
        orderlist = database.child('users').child(id).child('sellorders').get()
        print(orderlist.val())
        if orderlist.val() == None:
            pass
        else:
            for order in orderlist:
                order = order.val()
                coin_of_interest = order['ordercoin']
                current_coin_pricing = requests.get('http://host.docker.internal:5001/coin/' + coin_of_interest)
                if current_coin_pricing:
                    current_coin_pricing = dummy(current_coin_pricing)
                    if current_coin_pricing >= order['sell_price']:
                        sell=requests.get('http://host.docker.internal:5010/'+ coin_of_interest + '/sell?sellqty='+str(order['sell_quantity']))
                        if sell:
                            total_amount_gain = float(order['sell_quantity']) * current_coin_pricing
                            database.child('users').child(id).child('sellorders').remove(coin_of_interest)

                            order = {'sell_price': current_coin_pricing, 'sell_quantity': sell['sell_quantity'], 'ordercoin': sell['ordercoin'], 'total_amount_earned': total_amount_gain}
                            # amqp_setup.channel.basic_publish(exchange=amqp_setup.RABBITMQ_BUY_EXCHANGE, routing_key='', body=json.dumps(order))
                            # # Close RabbitMQ connection
                            # amqp_setup.connection.close()


                    else:
                        pass
                else:
                    pass
checkBuyOrderStatus()
checkSellOrderStatus()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5200, debug=True)

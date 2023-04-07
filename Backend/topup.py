from flask import redirect, request, url_for, render_template, Flask, jsonify
import stripe
import pyrebase
import helpers
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')
CORS(app)

app.config['STRIPE_PUBLIC_KEY'] = 'pk_test_51Mqv3mL81p6Fg6ebcfrJYprowuiyEYky8iILawOUGwdd7WEjxkQk6hJRfSXm02XdbgzBU0qGmhJxoA737LI0mDcm004m87jVGX'
app.config['STRIPE_SECRET_KEY'] = 'sk_test_51Mqv3mL81p6Fg6ebxNqIERpNmaW1FIyE0Ps6EH6A3UHKI9pMVIlUR6ExCmOwlrrBXArZPTLu0GnF8wOppX16g2qq00hB17R6OX'

stripe.api_key = app.config['STRIPE_SECRET_KEY']

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

@app.route("/processtopup", methods = ['GET', 'POST'])
def topUpWallet():
    
    status = '\n --- Bringing you to top-up page ---'
    try: 
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                    'price': 'price_1MqvPOL81p6Fg6ebILbmwrSq',
                    'quantity': 1,
                }],
            mode='payment',
            success_url=url_for('processTopUp', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=url_for('profile', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
        )
    except Exception as e:
        return str(e)
    # render_template( 
    #         'coins/profilepage.html',
    #         checkout_session_id=session['id'],
    #         checkout_public_key=['STRIPE_PUBLIC_KEY']
    #         )

    return redirect(session.url, code=303)
    # return redirect("https://buy.stripe.com/test_00g5nJ2nW3GC1zO288")
    # result = invoke_http("http:host.docker.internal:5000/transaction", method='POST')
    # print(result)

@app.route('/thanks')
def processTopUp():
    session_id = request.args.get("session_id")
    print(session_id)
    line_items = stripe.checkout.Session.list_line_items(session_id)
    print(line_items)
    transaction_id = line_items['data'][0].id
    top_up_amt = line_items['data'][0].amount_total/100
    id = helpers.retrieveHelperVal('uID', 'helpers.txt')
    # top_up_amt is preset to 1 and stripe ensure no -ve numbers can be entered, so there wont be any human errors
    if top_up_amt != 0:
        status = jsonify (
            {
                'code': 200,
                'message': 'Top up sucessful!'
            }
            
        )
  # Update Wallet amount
        retrieved_bal = database.child("users").child(id).child('wallet_coins').get()
        print(retrieved_bal)
        final_topup_amt = retrieved_bal.val()['USD']['qty'] + top_up_amt
        database.child("users").child(id).child('wallet_coins').child('USD').update({"qty":final_topup_amt})
        
    # Update Transaction in logs
        transaction_type = 'topup'
        time = datetime.now()
        data = {"userid": id, "transactionid": transaction_id, "date": str(time), "transaction_type": transaction_type, "amount": top_up_amt, }
        database.child("users").child(id).child('transactions').push(data)

        
        print('Top Up Amount: ', top_up_amt)
        return redirect(f'http://host.docker.internal:5000/thanks?status={status}&transaction_id={transaction_id}&top_up_amt={top_up_amt}')
    else:
        status = 'Error! Try topping up again!'
        profile_page_URL = "http://host.docker.internal:5000/profile"
        return redirect(profile_page_URL)


@app.route("/profile")
def profile():
    profile_page_URL = "http://host.docker.internal:5000/profile"
    return redirect(profile_page_URL)

@app.route("/swap")
def swap():
    swap_URL = "http://host.docker.internal:5000/swap"
    return redirect(swap_URL)

@app.route("/marketplace")
def marketplace():
    marketplace_URL = "http://host.docker.internal:5000/marketplace"
    return redirect(marketplace_URL)

if __name__ == '__main__':
    # processTopUp()
    app.run(host="0.0.0.0", port=5005, debug=True)
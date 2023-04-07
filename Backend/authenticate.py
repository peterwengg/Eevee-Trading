import pyrebase

# Price Microservice to show different CC prices on diff cc pages
from flask import Flask, request, redirect
from flask_cors import CORS
import os

app = Flask(__name__, template_folder='../Frontend/templates', static_folder='../Frontend/static')
CORS(app)


firebaseConfig = {
    'apiKey': "AIzaSyAUfijsgUQsPpdx5A21wO0wCS1qRkwh5o0",
    'authDomain': "cryptobuds-ba428.firebaseapp.com",
    'databaseURL': "https://cryptobuds-ba428-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "cryptobuds-ba428",
    'storageBucket': "cryptobuds-ba428.appspot.com",
    'messagingSenderId': "72206190161",
    'appId': "1:72206190161:web:bc8dbb3bf116fcc69fda70",
    'measurementId': "G-BVXDMYJR2K"
  }

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()

@app.route("/authenticate")
def authenticateUser():
    print("\n--- Checking credentials ---")
    
    email= request.args.get("un")
    password=request.args.get("pw")

    try:
        print("Successfully logged in!1")
        login = auth.sign_in_with_email_and_password(email, password)
        idToken = auth.get_account_info(login['idToken'])
        uID = auth.current_user['localId']

        writeToText('helpers.txt','uID:'+uID)

        return redirect('http://host.docker.internal:5000/home')
    except:
        print("Invalid email or password")
        return redirect('http://host.docker.internal:5000/login')

def writeToText(filename, text):
    with open(filename, 'w') as f:
        f.write(text)
# with app.app_context():

if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__))
    app.run(host="0.0.0.0", port=5050, debug=True)
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-app.js";
import { getDatabase, ref, update, onValue } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-database.js";
import { getAuth, signInWithEmailAndPassword, onAuthStateChanged, signOut, setPersistence, browserSessionPersistence } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-auth.js";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAUfijsgUQsPpdx5A21wO0wCS1qRkwh5o0",
  authDomain: "cryptobuds-ba428.firebaseapp.com",
  databaseURL: "https://cryptobuds-ba428-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "cryptobuds-ba428",
  storageBucket: "cryptobuds-ba428.appspot.com",
  messagingSenderId: "72206190161",
  appId: "1:72206190161:web:bc8dbb3bf116fcc69fda70",
  measurementId: "G-BVXDMYJR2K"
};

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);
const coinRef = ref(db, 'users');
const auth = getAuth();
onAuthStateChanged(auth, (user) => {
  if (user) {
    const uid = user.uid;
    onValue(coinRef, (snapshot) => {
      const data = snapshot.val();
      getValues(data, uid)
      getTransaction(data,uid)
    });
  }
});

function getValues(data, uid) {
  wallet_coins = data[uid].wallet_coins
  var username = data[uid].username
  var datecreated = data[uid].date_created
  var wallet_coins = data[uid].wallet_coins

  var ada = wallet_coins.ADA
  var usd = wallet_coins.USD
  var bnb = wallet_coins.BNB
  var btc = wallet_coins.BTC
  var doge = wallet_coins.DOGE
  var eth = wallet_coins.ETH
  var sol = wallet_coins.SOL

  document.getElementById('email').innerHTML = username
  document.getElementById('registered').innerHTML = datecreated
  document.getElementById('ADAquantity').innerHTML = ada.qty
  document.getElementById('BNBquantity').innerHTML = bnb.qty
  document.getElementById('BTCquantity').innerHTML = btc.qty
  document.getElementById('DOGEquantity').innerHTML = doge.qty
  document.getElementById('ETHquantity').innerHTML = eth.qty
  document.getElementById('SOLquantity').innerHTML = sol.qty
  document.getElementById('USDquantity').innerHTML = usd.qty
}

function getTransaction(data, uid){
  var result1 = `<tr><th>TransactionId</th><th>Amount Received</th></tr>`
  var result2 = `<tr><th>Date</th><th>Transaction Type</th><th>Purchase Quantity</th><th>Purchase Price</th><th>Total Spent</th><th>Coin</th></tr>`
    var transactions = data[uid].transactions
    for (var transaction in transactions){
      if (transactions[transaction].transaction_type == 'topup'){

        var amount = transactions[transaction]['amount']

        var transaction_id = transactions[transaction]['transactionid']

        result1 += `</tr><td>${transaction_id}</td><td>${amount}</td></tr>`
      }
      else if (transactions[transaction].transaction_type == 'buy'){
        var date = transactions[transaction]['date']
        date = date.substring(0, date.length - 7)
        var purchase_price = transactions[transaction]['purchase_price']
        var purchase_quantity = transactions[transaction]['purchase_quantity']
        var total_spent = transactions[transaction]['total_spent']
        var transaction_type = transactions[transaction]['transaction_type']
        var coin = transactions[transaction]['coin']

        result2 += `<tr><td>${date}</td><td>${transaction_type}</td><td>${purchase_quantity}</td><td>${purchase_price}</td><td>${total_spent}</td><td>${coin}</td></tr>`
      }
      else{
        var date = transactions[transaction]['date']
        date = date.substring(0, date.length - 7)
        var sell_price = transactions[transaction]['sell_price']
        var sell_quantity = transactions[transaction]['sell_quantity']
        var total_earned = transactions[transaction]['total_earned']
        var transaction_type = transactions[transaction]['transaction_type']
        var coin = transactions[transaction]['coin']
        result2 += `<tr><td>${date}</td><td>${transaction_type}</td><td>${sell_quantity}</td><td>${sell_price}</td><td>${total_earned}</td><td>${coin}</td></tr>`
      }
    }

    document.getElementById('topupdata').innerHTML = result1
    document.getElementById('transactiondata').innerHTML = result2
  }



setTimeout(() => {
  addListener()
}, 1000);

function addListener(){
  logout.addEventListener('click', (f) => {
    onAuthStateChanged(auth, (user) => {
      if (user) {
        update(ref(db, 'Users in the system/' + user.uid), {
          LoginStatus: "Logged Off",
          LoginTime: "NIL"
        })
      } 
    });
  
    signOut(auth).then(() => {
      // Sign-out successful.
      setTimeout(() => {
        alert("Signed out!")
        window.location.href = "../login";
    }, 1000);
    }).catch((error) => {
      // An error happened.
    });
  
  });
}




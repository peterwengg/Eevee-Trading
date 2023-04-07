import { initializeApp } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-app.js";
import { getDatabase, ref, update, onValue } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-database.js";
import { getAuth, signInWithEmailAndPassword, onAuthStateChanged, signOut, setPersistence, browserSessionPersistence } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-auth.js";

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
const coinRef = ref(db, 'All users in database');
const auth = getAuth();
onAuthStateChanged(auth, (user) => {
  if (user) {
    const uid = user.uid;
    onValue(coinRef, (snapshot) => {
      const data = snapshot.val();
      getValues(data, uid)
    });
  }
});

function getValues(data, uid) {
  document.getElementById('wallet').innerHTML = ' ' + data[uid].Bc
  document.getElementById('qty').innerHTML = ' ' + data[uid].Btc
}

// setTimeout(() => {
//   addBuyEvent()
// }, 1000);

// setTimeout(() => {
//   addSellEvent()
// }, 1000);

// function addBuyEvent() {
//   buy.addEventListener('click', (d) => {
//     var quantityBought = Number(document.getElementById('transactionqty').value)
//     var balance = Number(document.getElementById('qty').textContent)
//     var price = document.getElementById('price').textContent
//     var totalCost = quantityBought * Number(price)
//     var tv = Number(document.getElementById('wallet').textContent) - totalCost
//     tv = tv.toFixed(2)
//     if (tv >= 0) {
//       onAuthStateChanged(auth, (user) => {
//         if (user) {
//           var totalbtc = quantityBought + balance
//           update(ref(db, 'All users in database/' + user.uid), {
//             Btc: totalbtc,
//             Bc: tv,
//           })
//           alert('Successfully Bought!')

//         }
//       });
//     }
//     else {
//       alert("Not enough Bcs")
//     }
//   })
// }


// function addSellEvent() {
//   sell.addEventListener('click', (e) => {
//     var quantitySold = Number(document.getElementById('transactionqty').value)
//     var balance = Number(document.getElementById('qty').textContent)
//     var price = document.getElementById('price').textContent
//     var totalCost = quantitySold * Number(price)
//     var tv = Number(document.getElementById('wallet').textContent) + totalCost
//     tv = tv.toFixed(2)
//     if (balance - quantitySold >= 0) {
//       onAuthStateChanged(auth, (user) => {
//         if (user) {
//           var totalbtc = balance - quantitySold
//           update(ref(db, 'All users in database/' + user.uid), {
//             Btc: totalbtc,
//             Bc: tv,

//           })
//           alert("Successfully Sold!")
//         } else {

//         }
//       });
//     }
//     else {
//       alert("Not enough quantity")
//     }
//   })
// }



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
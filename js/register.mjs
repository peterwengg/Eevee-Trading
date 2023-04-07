import { initializeApp } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-app.js";
import { getDatabase, set, ref, update } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-database.js";
import { getAuth, createUserWithEmailAndPassword, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-auth.js";

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


// Initialize Firebase
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);
const auth = getAuth();

signUp.addEventListener('click', (e) => {

    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    var wallet_coins = {
        BTC: { name: "Bitcoin", qty: 0 },
        ETH: { name: "Ethereum", qty: 0 },
        BNB: { name: "Binance Coin", qty: 0},
        DOGE: { name: "Doge Coin", qty: 0},
        SOL: { name: "Solana", qty: 0},
        ADA: { name: "Cardano", qty: 0},
        USD: { name: "United States Dollar", qty: 0}
    };
    
    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed in 

            const user = userCredential.user;
            set(ref(database, 'users/' + user.uid), {
                username: email,
                date_created: Date(),
                wallet_coins: wallet_coins
            })

            setTimeout(() => {
                alert('user created!');
                window.location.href = "/login";
            }, 1000);
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;

            alert(errorMessage);
        });

});

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
const auth = getAuth();

const db = getDatabase(app);


setTimeout(() => {
  addListener()
}, 1000);

function addListener(){
  logout.addEventListener('click', (f) => {
    //record before signing off
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

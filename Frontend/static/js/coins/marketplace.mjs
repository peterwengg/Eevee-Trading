import { initializeApp } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-app.js";
import { getDatabase, ref, update, onValue } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-database.js";
import { getAuth, signInWithEmailAndPassword, onAuthStateChanged, signOut, setPersistence, browserSessionPersistence } from "https://www.gstatic.com/firebasejs/9.13.0/firebase-auth.js";
// import axios from 'axios'

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

function getBNBInfo(){
  axios.get(coinInfoUrl, {
  params: {
      fsym: 'BNB'
  }
  })
  .then(response => {
      var accessData = response.data.Data['BNB']
      var name = accessData.Name
      var imageurl = accessData.ImageUrl
      var assetWebsite = accessData.AssetWebsiteUrl
      var whitepaper = accessData.AssetWhitepaperUrl
      var coinName = accessData.CoinName
      var proofType = accessData.ProofType
      var symbol = accessData.Symbol
      generateRow(name, assetWebsite, whitepaper, coinName, proofType, symbol)
  })
  .catch(error => {
      console.log(error.message);
  });
}
getBNBInfo()

function getBTCInfo() {
  axios.get(coinInfoUrl, {
  params: {
      fsym: 'BTC'
  }
  })
  .then(response => {
      var accessData = response.data.Data['BTC']
      var name = accessData.Name
      var imageurl = accessData.ImageUrl
      var assetWebsite = accessData.AssetWebsiteUrl
      var whitepaper = accessData.AssetWhitepaperUrl
      var coinName = accessData.CoinName
      var proofType = accessData.ProofType
      var symbol = accessData.Symbol
      generateRow(name, assetWebsite, whitepaper, coinName, proofType, symbol)
  })
  .catch(error => {
      console.log(error.message);
  });
}
getBTCInfo()

function getADAInfo(){
  axios.get(coinInfoUrl, {
  params: {
      fsym: 'ADA'
  }
  })
  .then(response => {
      var accessData = response.data.Data['ADA']
      var name = accessData.Name
      var imageurl = accessData.ImageUrl
      var assetWebsite = accessData.AssetWebsiteUrl
      var whitepaper = accessData.AssetWhitepaperUrl
      var coinName = accessData.CoinName
      var proofType = accessData.ProofType
      var symbol = accessData.Symbol
      generateRow(name, assetWebsite, whitepaper, coinName, proofType, symbol)
  })
  .catch(error => {
      console.log(error.message);
  });
}
getADAInfo()

function getDOGEInfo() {
  axios.get(coinInfoUrl, {
  params: {
      fsym: 'DOGE'
  }
  })
  .then(response => {
      var accessData = response.data.Data['DOGE']
      var name = accessData.Name
      var imageurl = accessData.ImageUrl
      var assetWebsite = accessData.AssetWebsiteUrl
      var whitepaper = accessData.AssetWhitepaperUrl
      var coinName = accessData.CoinName
      var proofType = accessData.ProofType
      var symbol = accessData.Symbol
      generateRow(name, assetWebsite, whitepaper, coinName, proofType, symbol)
  })
  .catch(error => {
      console.log(error.message);
  });
}

getDOGEInfo()

function getETHInfo() {
  axios.get(coinInfoUrl, {
  params: {
      fsym: 'ETH'
  }
  })
  .then(response => {
      var accessData = response.data.Data['ETH']
      var name = accessData.Name
      var imageurl = accessData.ImageUrl
      var assetWebsite = accessData.AssetWebsiteUrl
      var whitepaper = accessData.AssetWhitepaperUrl
      var coinName = accessData.CoinName
      var proofType = accessData.ProofType
      var symbol = accessData.Symbol
      generateRow(name, assetWebsite, whitepaper, coinName, proofType, symbol)
  })
  .catch(error => {
      console.log(error.message);
  });
}

getETHInfo()

function getSOLInfo(){
  axios.get(coinInfoUrl, {
  params: {
      fsym: 'SOL'
  }
  })
  .then(response => {
      var accessData = response.data.Data['SOL']
      var name = accessData.Name
      var imageurl = accessData.ImageUrl
      var assetWebsite = accessData.AssetWebsiteUrl
      var whitepaper = accessData.AssetWhitepaperUrl
      var coinName = accessData.CoinName
      var proofType = accessData.ProofType
      var symbol = accessData.Symbol
      generateRow(name, assetWebsite, whitepaper, coinName, proofType, symbol)
  })
  .catch(error => {
      console.log(error.message);
  });
}

getSOLInfo()

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);
const coinRef = ref(db, 'All users in database');
const auth = getAuth();

setTimeout(() => {
  addListener()
}, 1000);

function addListener(){
  logout.addEventListener('click', (f) => {
    //record before signing off
    onAuthStateChanged(auth, (user) => {
      if (user) {
        const uid = user.uid;
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
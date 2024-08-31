import { initializeApp } from 'firebase/app'
import { getDatabase } from 'firebase/database'

const firebaseConfig = {
  apiKey: "AIzaSyBtDB_K432v81AcCv3x-jvfs-wymseFh8U",
  authDomain: "codereview-jobs.firebaseapp.com",
  databaseURL: 'https://codereview-jobs-default-rtdb.europe-west1.firebasedatabase.app',
  projectId: "codereview-jobs",
  storageBucket: "codereview-jobs.appspot.com",
  messagingSenderId: "1056554077979",
  appId: "1:1056554077979:web:dd86c5c5976c9fdc44cdbe",
  measurementId: "G-10PZV4WFCG"
}

const app = initializeApp(firebaseConfig)

export const database = getDatabase(app)

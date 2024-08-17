import { initializeApp } from 'firebase/app'
import { getDatabase } from 'firebase/database'

const firebaseConfig = {
  apiKey: 'AIzaSyCZSJyLkVUwS9VMF_0aN3iSKSAm-95ET54',
  authDomain: 'codereview-jobs-test.firebaseapp.com',
  databaseURL: 'https://codereview-jobs-test-default-rtdb.europe-west1.firebasedatabase.app',
  projectId: 'codereview-jobs-test',
  storageBucket: 'codereview-jobs-test.appspot.com',
  messagingSenderId: '525728150792',
  appId: '1:525728150792:web:f18fd9470deadf398768bd',
  measurementId: 'G-Y80K162ZC5'
}

const app = initializeApp(firebaseConfig)

export const database = getDatabase(app)

import { initializeApp } from 'firebase/app'

const firebaseConfig = {
    apiKey: import.meta.env.VITE_FIREBASE_API_KEY,
    authDomain: 'yourcodereview-35312.firebaseapp.com',
    projectId: 'yourcodereview-35312',
    storageBucket: 'yourcodereview-35312.appspot.com',
    messagingSenderId: '710177683003',
    appId: '1:710177683003:web:f6c3e6b8ebde7f46754e1e'
}

initializeApp(firebaseConfig)

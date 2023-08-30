// useFirebase.js
import { ref, onMounted } from 'vue'
import {
    getAuth,
    onAuthStateChanged,
    createUserWithEmailAndPassword,
    signInWithEmailAndPassword,
    GoogleAuthProvider,
    signInWithPopup,
    signOut
} from 'firebase/auth'

export function useFirebase() {
    const auth = getAuth()
    const currentUser = ref({})
    const isLoggedIn = ref(false)
    const errorMsg = ref('')

    const checkAuthState = () => {
        onAuthStateChanged(auth, (user) => {
            if (user) {
                isLoggedIn.value = true
                currentUser.value = user
            } else {
                isLoggedIn.value = false
                currentUser.value = {}
            }
        })
    }

    const registerUser = async (email, password) => {
        try {
            const result = await createUserWithEmailAndPassword(auth, email, password)
            currentUser.value = result.user
            isLoggedIn.value = true
        } catch (error) {
            console.log(error)
        }
    }

    const loginUser = async (email, password) => {
        try {
            const result = await signInWithEmailAndPassword(auth, email, password)
            currentUser.value = result.user
            isLoggedIn.value = true
        } catch (error) {
            console.log(error)
            switch (error.code) {
                case 'auth/invalid-email':
                case 'auth/user-not-found':
                    errorMsg.value = 'Такого человека не ждут'
                    break
                case 'auth/wrong-password':
                    errorMsg.value = 'Неверный пароль'
                    break
                default:
                    errorMsg.value = 'Неверное имя или пароль'
                    break
            }
        }
    }

    const loginWithGoogle = async () => {
        try {
            const result = await signInWithPopup(auth, new GoogleAuthProvider())
            currentUser.value = result.user
            isLoggedIn.value = true
        } catch (error) {
            console.log(error)
        }
    }

    const logoutUser = async () => {
        try {
            await signOut(auth)
            isLoggedIn.value = false
            currentUser.value = {}
        } catch (error) {
            console.log(error)
        }
    }

    onMounted(() => {
        checkAuthState()
    })

    return {
        currentUser,
        isLoggedIn,
        errorMsg,
        registerUser,
        loginUser,
        loginWithGoogle,
        logoutUser
    }
}

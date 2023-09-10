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
    const isLoading = ref(false)
    const errorMsg = ref('')

    const errorConversion = (error) => {
        switch (error.code) {
            case 'auth/invalid-email':
                return 'Некорректный email'
            case 'auth/user-not-found':
                return 'Пользователь не найден'
            case 'auth/wrong-password':
                return 'Неверный пароль'
            default:
                return 'Неверный email или пароль'
        }
    }

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
        isLoading.value = true
        try {
            const result = await createUserWithEmailAndPassword(auth, email, password)
            currentUser.value = result.user
            isLoggedIn.value = true
        } catch (error) {
            errorMsg.value = errorConversion(error)
            console.log(errorMsg.value)
        } finally {
            isLoading.value = false
        }
    }

    const loginUser = async (email, password) => {
        isLoading.value = true
        try {
            const result = await signInWithEmailAndPassword(auth, email, password)
            currentUser.value = result.user
            isLoggedIn.value = true
        } catch (error) {
            errorMsg.value = errorConversion(error)
            console.log(errorMsg.value)
        } finally {
            isLoading.value = false
        }
    }

    const loginWithGoogle = async () => {
        isLoading.value = true
        try {
            const result = await signInWithPopup(auth, new GoogleAuthProvider())
            currentUser.value = result.user
            isLoggedIn.value = true
        } catch (error) {
            console.log(error)
        } finally {
            isLoading.value = false
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
        isLoading,
        errorMsg,
        registerUser,
        loginUser,
        loginWithGoogle,
        logoutUser
    }
}

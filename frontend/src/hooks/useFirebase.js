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
                return 'Некорректный email'
            case 'auth/user-not-found':
                return 'Пользователь не найден'
            case 'auth/wrong-password':
                return 'Неверный пароль'
            default:
                return 'Неверный email или пароль'
        }
    }

    const handleAuthError = (error) => {
        isLoading.value = false
        errorMsg.value = errorConversion(error)
        console.log(errorMsg.value)
    }

    const checkAuthState = () => {
        onAuthStateChanged(auth, (user) => {
            if (user) {
                currentUser.value = user
                isLoggedIn.value = true
            } else {
                currentUser.value = {}
                isLoggedIn.value = false
            }
        })
    }

    const registerUser = async (email, password) => {
        isLoading.value = true
        try {
            const result = await createUserWithEmailAndPassword(auth, email, password)
            currentUser.value = result.user
            isLoggedIn.value = true
            clearError()
        } catch (error) {
            handleAuthError(error)
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
            clearError()
        } catch (error) {
            handleAuthError(error)
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
            clearError()
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

    const clearError = () => {
        errorMsg.value = ''
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
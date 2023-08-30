import { defineStore } from 'pinia'
import { ref } from 'vue'
import { useFirebase } from '../firebase/useFirebase'

export const useAuthStore = defineStore('auth', () => {
    const {
        currentUser,
        isLoggedIn,
        errMsg,
        registerUser,
        loginUser,
        loginWithGoogle,
        logoutUser
    } = useFirebase()

    const email = ref('')
    const password = ref('')

    const login = async () => {
        return await loginUser(email.value, password.value)
    }

    const loginGoogle = async () => {
        return await loginWithGoogle()
    }

    const register = async () => {
        return await registerUser(email.value, password.value)
    }

    const logout = async () => {
        return await logoutUser()
    }

    return {
        currentUser,
        isLoggedIn,
        errMsg,
        email,
        password,
        login,
        loginGoogle,
        register,
        logout
    }
})

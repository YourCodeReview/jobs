<script setup>
import { ref } from 'vue'
import { useStateStore } from '../stores/index'
import { useAuthStore } from '../stores/auth'

import TheNavigation from './TheNavigation.vue'
import UiButton from './ui/UiButton.vue'
import UiModal from './ui/UiModal.vue'
import UiForm from './ui/UiForm.vue'

const store = useStateStore()
const auth = useAuthStore()
const modalIsOpen = ref(false)
const formType = ref('')

const openModalType = (status) => {
    formType.value = status
    modalIsOpen.value = true
}

const register = async () => {
    await auth.register()
    modalIsOpen.value = false
}

const login = async () => {
    await auth.login()
    modalIsOpen.value = false
}

const signInWithGoogle = async () => {
    await auth.loginGoogle()
    modalIsOpen.value = false
}

const logout = () => {
    auth.logout()
}
</script>

<template>
    <header class="header">
        <div class="container header-container">
            <TheNavigation
                :links="store.headerLinks"
                :user="auth.currentUser"
                :is-logged-in="auth.isLoggedIn"
                @openModalType="openModalType"
                @logout="logout"
            />
        </div>
    </header>
    <UiModal v-if="modalIsOpen" :title="formType === 'login' ? 'Авторизация' : 'Регистрация'">
        <UiForm
            @register="register"
            @login="login"
            @logout="logout"
            :formType="formType"
            :errorMessage="auth.errMsg"
        />
        <UiButton text="Войти через Google" @click="signInWithGoogle" />
    </UiModal>
</template>

<style scoped>
.header {
    position: sticky;
    z-index: 100;
    top: 0;

    background-image: linear-gradient(
        0.092turn,
        rgba(32, 147, 254, 1) 0%,
        rgba(194, 23, 254, 1) 90%
    );
}

.header-container {
    padding: 0 40px;
}
</style>

<script setup>
import { useStateStore } from '../stores/index'
import { useAuthStore } from '../stores/auth'
import { useModalStore } from '../stores/modal'

import TheNavigation from './TheNavigation.vue'
import UiButton from './ui/UiButton.vue'
import UiModal from './ui/UiModal.vue'
import UiForm from './ui/UiForm.vue'

const store = useStateStore()
const auth = useAuthStore()
const modal = useModalStore()

const register = async () => {
    await auth.register()
    modal.close()
}

const login = async () => {
    await auth.login()
    modal.close()
}

const signInWithGoogle = async () => {
    await auth.loginGoogle()
    modal.close()
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
                @openModalType="modal.open"
                @logout="logout"
            />
        </div>
    </header>
    <UiModal v-if="modal.isOpen" :title="modal.type === 'login' ? 'Авторизация' : 'Регистрация'">
        <UiForm
            @register="register"
            @login="login"
            @logout="logout"
            :formType="modal.type"
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
</style>

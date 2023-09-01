<script setup>
import UiButton from './UiButton.vue'
import UiInput from './UiInput.vue'

import { useAuthStore } from '../../stores/auth'

const props = defineProps({
    formType: String,
    errorMessage: String
})
const emits = defineEmits(['login', 'register'])

const auth = useAuthStore()
const formSubmit = () => {
    emits(props.formType)
}
</script>

<template>
    <form @submit.prevent="formSubmit" class="form">
        <UiInput type="email" v-model="auth.email" required />
        <UiInput type="password" v-model="auth.password" required />
        <p class="error">{{ errorMessage }}</p>
        <UiButton
            :text="props.formType === 'register' ? 'Регистрация' : 'Авторизация'"
            type="submit"
        />
    </form>
</template>

<style scoped>
.form {
    display: flex;
    align-items: center;
    flex-direction: column;

    gap: 10px;
}

.error {
    color: red;
}
</style>

<template>
  <v-form v-model="form" @submit.prevent="authenticate(email, password)">
    <v-text-field
      v-model="email"
      :rules="[required]"
      hide-details
      class="mb-2"
      clearable
      label="Почта"
    ></v-text-field>

    <v-text-field
      class="mb-4"
      v-model="password"
      type="password"
      :rules="[required]"
      hide-details
      clearable
      label="Пароль"
    ></v-text-field>
    <v-btn
      class="form-btn"
      :disabled="!form"
      :loading="auth.isLoading.value"
      block
      size="large"
      type="submit"
      variant="elevated"
    >
      {{ formType }}
    </v-btn>
    <ui-snackbar :is-open="!!auth.errorMsg.value" :message="auth.errorMsg.value" />
  </v-form>
</template>

<script setup>
import { ref } from 'vue'
import { computed } from 'vue'
import { useFirebase } from '@/hooks/useFirebase'

import uiSnackbar from './ui/uiSnackbar.vue'

const emits = defineEmits(['close'])

const props = defineProps({
  type: {
    type: String,
    default: 'register'
  }
})

const auth = useFirebase()
const form = ref(false)
const email = ref(null)
const password = ref(null)
const snackbar = ref(false)

const formType = computed(() => {
  if (props.type === 'login') {
    return 'Авторизация'
  } else {
    return 'Регистрация'
  }
})

const authenticate = async (email, password) => {
  if (props.type === 'register') {
    await auth.registerUser(email, password)
  } else if (props.type === 'login') {
    await auth.loginUser(email, password)
  } else {
    await auth.loginWithGoogle()
  }
  auth.errorMsg.value === '' ? emits('close') : (snackbar.value = true)
}
const required = (v) => {
  return !!v || 'Заполните поле'
}
</script>

<style scoped>
.form-btn {
  padding: 0 30px;

  color: white;
  background-image: linear-gradient(33deg, rgba(0, 87, 255, 1) 0%, rgba(0, 228, 201, 1) 91%);
}
</style>

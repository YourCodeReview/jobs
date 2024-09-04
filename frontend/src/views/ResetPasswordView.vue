<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { confirmPasswordReset } from 'firebase/auth'
import { useFirebase } from '@/hooks/useFirebase'
import svgLogo from '@/components/_icons/svgLogo.vue'
import uiSnackbar from '@/components/_ui/uiSnackbar.vue'

const password = ref('')
const confirmPassword = ref('')
const isFormValid = ref(false)
const visiblePasswordEnter = ref(false)
const visiblePasswordConfirm = ref(false)
const form = ref(null)
const isSubmitSuccess = ref(false)
const snackbarMessage = ref('')
const snackbar = ref(false)

const passwordRules = [
  (v) => !!v || 'Поле для ввода пароля обязательно',
  (v) => v.length >= 6 || 'Пароль должен содержать не менее 6 символов'
]
const confirmPasswordRules = [
  (v) => !!v || 'Подтверждение пароля обязательно',
  (v) => v === password.value || 'Пароли должны совпадать'
]

// Получаем код восстановления пароля из URL
const route = useRoute()
const oobCode = route.query.oobCode

const router = useRouter()

const resetPassword = async () => {
  if (form.value.validate()) {
    try {
      if (password.value !== confirmPassword.value) {
        throw new Error('Passwords do not match')
      }

      const { auth } = useFirebase()
      await confirmPasswordReset(auth, oobCode, password.value)
      isSubmitSuccess.value = true
      snackbarMessage.value = 'Пароль успешно изменен'
      snackbar.value = true
      router.replace({ name: 'Login' })
    } catch (error) {
      isSubmitSuccess.value = false
      snackbarMessage.value = 'Не удалось сменить пароль. Повторите попытку.'
      snackbar.value = true
    }
  } else {
    console.log('Форма заполнена неверно')
  }
}
</script>

<template>
  <div class="background pa-8 h-screen d-flex flex-column justify-center align-center">
    <svg-logo />
    <v-card
      class="mx-auto pa-8 mt-8 w-100"
      elevation="8"
      min-width="260"
      max-width="600"
      rounded="lg"
    >
      <v-card-title>
        <span class="text-subtitle-1 text-medium-emphasis text-wrap">Введите новый пароль</span>
      </v-card-title>
      <v-card-text>
        <v-form ref="form" v-model="isFormValid" @submit.prevent="resetPassword">
          <v-text-field
            class="mb-4"
            v-model="password"
            placeholder="Введите пароль"
            prepend-inner-icon="mdi-lock-outline"
            :rules="passwordRules"
            variant="outlined"
            required
            :append-inner-icon="visiblePasswordEnter ? 'mdi-eye-off' : 'mdi-eye'"
            :type="visiblePasswordEnter ? 'text' : 'password'"
            @click:append-inner="visiblePasswordEnter = !visiblePasswordEnter"
          />
          <v-text-field
            v-model="confirmPassword"
            placeholder="Подтвердите пароль"
            prepend-inner-icon="mdi-lock-outline"
            :rules="confirmPasswordRules"
            variant="outlined"
            required
            :append-inner-icon="visiblePasswordConfirm ? 'mdi-eye-off' : 'mdi-eye'"
            :type="visiblePasswordConfirm ? 'text' : 'password'"
            @click:append-inner="visiblePasswordConfirm = !visiblePasswordConfirm"
          />
          <v-btn type="submit" class="w-100" variant="tonal" size="large" :disabled="!isFormValid">
            Изменить пароль
          </v-btn>
        </v-form>
      </v-card-text>
    </v-card>
    <uiSnackbar
      :color="isSubmitSuccess ? 'green' : 'red'"
      v-model="snackbar"
      :message="snackbarMessage"
    />
  </div>
</template>

<style scoped>
.background {
  position: relative;
  background-image: var(--purple-gradient);
}
</style>

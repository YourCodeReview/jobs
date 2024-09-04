<script setup>
import { ref } from 'vue'
import { sendPasswordResetEmail } from 'firebase/auth'
import svgLogo from '@/components/_icons/svgLogo.vue'
import uiSnackbar from '@/components/_ui/uiSnackbar.vue'
import { useFirebase } from '@/hooks/useFirebase'

const { auth } = useFirebase()

const snackbar = ref(false)
const snackbarMessage = ref('')

const email = ref('')
const isFormValid = ref(false)
const isSubmitSuccess = ref(false)

const emailRules = [
  (v) => !!v || 'Email обязателен для заполнения',
  (v) => /.+@.+\..+/.test(v) || 'Введите корректный email'
]

const form = ref(null)

const submitForm = async () => {
  if (form.value.validate()) {
    try {
      await sendPasswordResetEmail(auth, email.value)
      snackbarMessage.value = 'Ссылка для сброса пароля отправлена на вашу почту.'
      isSubmitSuccess.value = true
      snackbar.value = true
    } catch (error) {
      console.error('Error sending password reset email:', error)
      snackbarMessage.value = 'Ошибка при отправке ссылки для сброса пароля.'
      isSubmitSuccess.value = false
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
      min-width="323"
      max-width="600"
      rounded="lg"
    >
      <v-card-title v-if="!isSubmitSuccess">
        <span class="text-subtitle-1 text-medium-emphasis">Почта для сброса пароля</span>
      </v-card-title>
      <v-card-text v-if="!isSubmitSuccess">
        <v-form ref="form" v-model="isFormValid" @submit.prevent="submitForm">
          <v-text-field
            class="mb-4"
            v-model="email"
            :rules="emailRules"
            placeholder="Введите почту"
            prepend-inner-icon="mdi-email-outline"
            variant="outlined"
            required
          ></v-text-field>

          <v-btn type="submit" class="w-100" variant="tonal" size="large" :disabled="!isFormValid">
            Отправить ссылку
          </v-btn>
        </v-form>
      </v-card-text>
      <h3 v-else class="text-center">
        Проверьте почту <br />
        {{ email }}
      </h3>
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

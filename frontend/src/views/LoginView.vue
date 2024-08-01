<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useFirebase } from '@/hooks/useFirebase'
import { useUnisender } from '@/hooks/useUnisender'
import { useField, useForm } from 'vee-validate'
import * as yup from 'yup'

import svgLogo from '@/components/_icons/svgLogo.vue'
import uiSnackbar from '@/components/_ui/uiSnackbar.vue'

const validationSchema = yup.object({
  email: yup
    .string()
    .email('Некорректный формат email')
    .matches(/^.*@.*\..*.$/, 'Некорректный формат email')
    .max(120, 'Максимум 120 символов')
    .required('Поле для email обязательно'),
  password: yup
    .string()
    .min(6, 'Введите минимум 6 символов')
    .required('Поле для пароля обязательно'),
  phone: yup
    .string()
    .matches(/^\+?\d+$/, 'Телефон должен содержать только цифры')
    .min(10, 'Введите минимум 10 цифр')
    .required('Поле для телефона обязательно')
})

const { handleSubmit, handleReset } = useForm({
  validationSchema
})

const email = useField('email')
const password = useField('password')
const phone = useField('phone')

const router = useRouter()
const auth = useFirebase()
const { subscribe } = useUnisender()

const type = ref('login')

const visible = ref(false)
const snackbar = ref(false)
const expand = ref(false)
const showModal = ref(false)

const phoneSubmit = handleSubmit((values) => {
  showModal.value = false
  auth.isLoggedIn.value ? router.back() : (snackbar.value = true)
  console.log(values)
  handleReset()
})

const authenticate = async (email, password) => {
  if (type.value === 'register') {
    await auth.registerUser(email, password)
    phoneSubmit()
  } else if (type.value === 'login') {
    await auth.loginUser(email, password)
  }
  subscribe(auth.currentUser.value.email)
}

const googleAuth = async () => {
  await auth.loginWithGoogle()
  subscribe(auth.currentUser.value.email)
  showModal.value = true
}

onMounted(() => {
  auth.logoutUser()
  expand.value = true
})
</script>

<template>
  <div class="background pa-8 h-screen d-flex flex-column justify-center align-center">
    <svg-logo />
    <v-form @submit.prevent="authenticate(email.value.value, password.value.value)" v-show="expand">
      <v-card
        class="mx-auto pa-8 mt-8 w-100"
        elevation="8"
        min-width="323"
        max-width="600"
        rounded="lg"
      >
        <div class="text-subtitle-1 text-medium-emphasis">Почта</div>

        <v-text-field
          v-model="email.value.value"
          :error-messages="email.errorMessage.value"
          density="compact"
          placeholder="Введите почту"
          prepend-inner-icon="mdi-email-outline"
          variant="outlined"
          required
        ></v-text-field>

        <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
          Пароль
        </div>

        <v-text-field
          v-model="password.value.value"
          :error-messages="password.errorMessage.value"
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="visible ? 'text' : 'password'"
          density="compact"
          placeholder="Введите пароль"
          prepend-inner-icon="mdi-lock-outline"
          variant="outlined"
          required
          @click:append-inner="visible = !visible"
        ></v-text-field>

        <div v-if="type === 'register'">
          <div
            class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between"
          >
            Телефон
          </div>

          <v-text-field
            v-model="phone.value.value"
            :error-messages="phone.errorMessage.value"
            prepend-inner-icon="mdi-phone-outline"
            placeholder="Введите телефон"
            density="compact"
            variant="outlined"
          ></v-text-field>
        </div>

        <v-btn block type="submit" class="mb-2" size="large" variant="tonal">
          {{ type === 'register' ? 'Зарегистрироваться' : 'Войти' }}
        </v-btn>
        <v-btn class="btn__google mb-2" @click="googleAuth" size="large" block>
          Войти через Google
        </v-btn>

        <v-card-text class="text-center">
          <v-btn
            class="text-decoration-none"
            variant="text"
            size="small"
            @click="type === 'login' ? (type = 'register') : (type = 'login')"
          >
            {{ type !== 'register' ? 'Зарегистрироваться' : 'Войти' }}
            <v-icon icon="mdi-chevron-right"></v-icon>
          </v-btn>
        </v-card-text>
      </v-card>
      <ui-snackbar color="red" v-model="snackbar" :message="auth.errorMsg.value" />
    </v-form>
    <v-btn class="btn__close" icon="mdi-close" @click="router.back()"></v-btn>
    <v-dialog v-model="showModal" max-width="400" persistent transition="dialog-bottom-transition">
      <v-form>
        <v-card title="Введите номер телефона">
          <template v-slot:text>
            <v-text-field
              v-model="phone.value.value"
              :error-messages="phone.errorMessage.value"
              prepend-inner-icon="mdi-phone-outline"
              placeholder="Введите телефон"
              density="compact"
              variant="outlined"
            ></v-text-field>
          </template>
          <template v-slot:actions>
            <v-spacer></v-spacer>

            <v-btn @click="showModal = false"> Отмена </v-btn>

            <v-btn @click="phoneSubmit"> OK </v-btn>
          </template>
        </v-card>
      </v-form>
    </v-dialog>
  </div>
</template>

<style scoped>
.background {
  position: relative;

  background-image: var(--purple-gradient);
}

.btn__google {
  color: white;
  background-image: var(--blue-gradient);
}

.btn__close {
  position: absolute;
  top: 25px;
  right: 25px;
}
</style>

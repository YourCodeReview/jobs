<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'
import { useFirebase } from '@/hooks/useFirebase'
import { useUnisender } from '@/hooks/useUnisender'

import svgLogo from '@/components/_icons/svgLogo.vue'
import uiSnackbar from '@/components/_ui/uiSnackbar.vue'
import uiLanguageButton from '@/components/_ui/uiLanguageButton.vue'

const { t } = useI18n()

const router = useRouter()
const auth = useFirebase()
const { subscribe } = useUnisender()

const email = ref('')
const password = ref('')
const type = ref('login')

const visible = ref(false)
const snackbar = ref(false)
const expand = ref(false)

const authenticate = async (email, password) => {
  if (type.value === 'register') {
    await auth.registerUser(email, password)
  } else if (type.value === 'login') {
    await auth.loginUser(email, password)
  }
  subscribe(auth.currentUser.value.email)
  auth.isLoggedIn.value ? router.back() : (snackbar.value = true)
}

const googleAuth = async () => {
  await auth.loginWithGoogle()
  subscribe(auth.currentUser.value.email)
  auth.isLoggedIn.value ? router.back() : (snackbar.value = true)
}

onMounted(() => {
  auth.logoutUser()
  expand.value = true
})
</script>

<template>
  <div class="background pa-8 h-screen d-flex flex-column justify-center align-center">
    <svg-logo />
    <v-form @submit.prevent="authenticate(email, password)" v-show="expand">
      <v-card
        class="mx-auto pa-8 mt-8 w-100"
        elevation="8"
        min-width="323"
        max-width="600"
        rounded="lg"
      >
        <div class="text-subtitle-1 text-medium-emphasis">{{ t('loginPage.email') }}</div>

        <v-text-field
          v-model="email"
          density="compact"
          :placeholder="t('loginPage.emailPlaceholder')"
          prepend-inner-icon="mdi-email-outline"
          variant="outlined"
          required
        ></v-text-field>

        <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
          {{ t('loginPage.password') }}
        </div>

        <v-text-field
          v-model="password"
          :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
          :type="visible ? 'text' : 'password'"
          density="compact"
          :placeholder="t('loginPage.passwordPlaceholder')"
          prepend-inner-icon="mdi-lock-outline"
          variant="outlined"
          required
          @click:append-inner="visible = !visible"
        ></v-text-field>

        <v-btn block type="submit" class="mb-2" size="large" variant="tonal">
          {{ type === 'register' ? t('authButton.signUp') : t('authButton.logIn') }}
        </v-btn>
        <v-btn class="btn__google mb-2" @click="googleAuth" size="large" block>
          {{ t('authButton.google') }}
        </v-btn>

        <v-card-text class="text-center">
          <v-btn
            class="text-decoration-none"
            variant="text"
            size="small"
            @click="type === 'login' ? (type = 'register') : (type = 'login')"
          >
            {{ type !== 'register' ? t('authButton.signUp') : t('authButton.logIn') }}
            <v-icon icon="mdi-chevron-right"></v-icon>
          </v-btn>
        </v-card-text>
      </v-card>
      <ui-snackbar color="red" v-model="snackbar" :message="auth.errorMsg.value" />
    </v-form>
    <ui-language-button style="position: absolute; top: 0; left: 0; color: #fff" />
    <v-btn class="btn__close" icon="mdi-close" @click="router.back()"></v-btn>
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

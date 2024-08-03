<template>
  <v-btn
    class="mx-1"
    height="50"
    rounded="lg"
    :variant="variant"
    :block="block"
    @click="handleLogout"
  >
    {{ t('authButton.logOut') }}
  </v-btn>
</template>

<script setup>
import { useFirebase } from '@/hooks/useFirebase'
import { useI18n } from 'vue-i18n'

const auth = useFirebase()
const handleLogout = () => {
  auth.logoutUser()
}
defineProps({
  variant: String,
  block: Boolean
})
const { t } = useI18n()
</script>

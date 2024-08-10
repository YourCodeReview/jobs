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
import { useTranslation } from '@/hooks/useTranslation'

const auth = useFirebase()
const handleLogout = () => {
  auth.logoutUser()
}
defineProps({
  variant: String,
  block: Boolean
})
const { t } = useTranslation()
</script>

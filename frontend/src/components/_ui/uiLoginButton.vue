<template>
  <v-btn
    class="mx-1"
    height="50"
    rounded="lg"
    :variant="variant"
    :block="block"
    :to="{
      path: '/login',
      query: { type: 'login' }
    }"
  >
    {{ t('authButton.logIn') }}
  </v-btn>
</template>

<script setup>
import { useTranslation } from '@/hooks/useTranslation'
defineProps({
  variant: String,
  block: Boolean
})
const { t } = useTranslation()
</script>

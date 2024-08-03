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
import { useI18n } from 'vue-i18n'
defineProps({
  variant: String,
  block: Boolean
})
const { t } = useI18n()
</script>

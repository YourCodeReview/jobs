<template>
  <v-btn
    class="mx-1"
    height="50"
    color="lime"
    rounded="lg"
    href="https://yourcodereview.com/"
    :variant="variant"
    :block="block"
    target="_blank"
  >
    {{ t('careerButton') }}
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

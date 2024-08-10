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
import { useTranslation } from '@/hooks/useTranslation'
defineProps({
  variant: String,
  block: Boolean
})
const { t } = useTranslation()
</script>

<template>
  <v-btn
    class="mx-1"
    height="50"
    color="lime"
    rounded="lg"
    :href="'https://yourcodereview.com/' + generateTargetUrl('button_1')"
    :variant="variant"
    :block="block"
    target="_blank"
  >
    Карьерная поддержка
  </v-btn>
</template>

<script setup>
defineProps({
  variant: String,
  block: Boolean
})

import { generateTargetUrl } from '@/components/utils/utils';
</script>

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
    Карьерная поддержка
  </v-btn>
</template>

<script setup>
defineProps({
  variant: String,
  block: Boolean
})
</script>

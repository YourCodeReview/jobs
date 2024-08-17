<template>
  <v-btn
    class="mx-1"
    height="50"
    rounded="lg"
    :variant="variant"
    :block="block"
    :to="{
      path: '/login',
      query: { ...currentQueryParams, type: 'login' }
    }"
  >
    Войти
  </v-btn>
</template>

<script setup>
defineProps({
  variant: String,
  block: Boolean
})

import { useRouter } from 'vue-router'

const router = useRouter()
const currentQueryParams = router.currentRoute.value.query

</script>

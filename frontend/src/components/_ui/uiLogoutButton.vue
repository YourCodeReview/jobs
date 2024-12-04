<template>
  <v-btn
    class="mx-1"
    height="50"
    rounded="lg"
    :variant="variant"
    :block="block"
    @click="handleLogout"
  >
    Выйти
  </v-btn>
</template>

<script setup>
import { useJobsStore } from '@/store/jobs'

// const auth = useFirebase()
const store = useJobsStore()
const handleLogout = () => {
  localStorage.removeItem('token')

  store.isAuth = false
}
defineProps({
  variant: String,
  block: Boolean
})
</script>

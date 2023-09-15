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
import { useFirebase } from '@/hooks/useFirebase'

const auth = useFirebase()
const handleLogout = () => {
  auth.logoutUser()
}
defineProps({
  variant: String,
  block: Boolean
})
</script>

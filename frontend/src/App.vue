<script setup>
import { ref, onMounted } from 'vue'
import { useJobsStore } from './store/jobs'
// import uiAdvertisingDialog from '@/components/_ui/uiAdvertisingDialog.vue'

// const dialog = ref(false)
const store = useJobsStore()

// const setDialogIsOpen = () => {
//   dialog.value = true
//   localStorage.setItem('advertising-shown', 'true')
// }

onMounted(() => {
  const token = localStorage.getItem('token')
  if (!token) store.isAuth = false
  if (token) store.isAuth = true

  // const advertisingShown = localStorage.getItem('advertising-shown')
  // if (advertisingShown) return
  // document.addEventListener('mousemove', (event) => {
  //   const advertisingShown = localStorage.getItem('advertising-shown')
  //   if (advertisingShown) return
  //   console.log(event.clientY)
  //   if (event.clientY <= 12) {
  //     setDialogIsOpen()
  //   }
  // })
  // setTimeout(() => {
  //   const advertisingShown = localStorage.getItem('advertising-shown')
  //   if (advertisingShown) return
  //   setDialogIsOpen()
  // }, 45000)
})
</script>

<template>
  <v-app id="inspire" class="bg-grey-lighten-4 position-relative">
    <router-view />

    <!-- <uiAdvertisingDialog v-model="dialog" /> -->
  </v-app>
</template>

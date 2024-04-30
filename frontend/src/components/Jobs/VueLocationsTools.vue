<script setup>
import { useJobsStore } from '@/store/jobs'
import { useLocationsStore } from '@/store/locations'
import { onMounted, watch, ref } from 'vue'

const jobsStore = useJobsStore()
const locationStore = useLocationsStore()
const location = ref('')

const fetchWithLocation = (locationValue) => {
  jobsStore.changeQuery('location', locationValue)
  jobsStore.fetchJobsDataWithDebounce()
  jobsStore.page = 1
}

watch(location, () => {
  localStorage.setItem('location', JSON.stringify(location.value))
  fetchWithLocation(location.value)
})

onMounted(() => {
  const locationFromStorage = JSON.parse(localStorage.getItem('location'))
  if (locationFromStorage) {
    location.value = locationFromStorage
  }
})
</script>

<template>
  <v-autocomplete
    class="mt-2"
    label="Город"
    v-model="location"
    :items="locationStore.locationsList"
    density="compact"
    hide-details
    variant="plain"
    clearable
  ></v-autocomplete>
</template>

<style scoped></style>

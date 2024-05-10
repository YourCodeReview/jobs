<script setup>
import { onMounted, watch, ref } from 'vue'
import { useJobsStore } from '@/store/jobs'
import filterTools from '@/data/jobs-filter-tools.json'

const checked = ref([])
const jobStore = useJobsStore()

const fetchFilteredData = (e) => {
  const field = e.target.value
  const value = e.target.checked
  jobStore.changeQuery(field, value)
  jobStore.fetchJobsData()
  jobStore.page = 1
}

onMounted(() => {
  const filterFieldsFromStorage = JSON.parse(localStorage.getItem('filter'))
  if (filterFieldsFromStorage?.length) {
    checked.value = filterFieldsFromStorage
  }
})

watch(checked, () => {
  localStorage.setItem('filter', JSON.stringify(checked.value))
})
</script>

<template>
  <v-checkbox
    v-for="tool in filterTools"
    :key="tool.value"
    v-model="checked"
    @click="fetchFilteredData"
    :label="tool.label"
    :value="tool.value"
    density="compact"
    hide-details
  ></v-checkbox>
</template>

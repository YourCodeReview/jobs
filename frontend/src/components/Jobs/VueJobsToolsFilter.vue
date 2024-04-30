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
  if (filterFieldsFromStorage) {
    checked.value = filterFieldsFromStorage
  }
})

watch(checked, () => {
  localStorage.setItem('filter', JSON.stringify(checked.value))
})
</script>

<template>
  <v-card class="sticky-card-panels w-100">
    <v-card-item class="bg-blue-lighten-1">
      <v-card-title class="text-center">
        <span class="text-h6">Фильтрация</span>
      </v-card-title>
    </v-card-item>

    <v-container fluid>
      <v-checkbox
        v-for="tool in filterTools"
        :key="tool.value"
        v-model="checked"
        @click="fetchFilteredData"
        :label="tool.label"
        :value="tool.value"
        density="compact"
      ></v-checkbox>
    </v-container>
  </v-card>
</template>

<style scoped>
.sticky-card-panels {
  position: sticky;
  top: 242px;

  max-width: 600px;
  margin: 0.5rem auto 0;

  border-radius: 1.5rem;
}

@media screen and (min-width: 960px) {
  .sticky-card-panels {
    max-width: 280px;
    margin: 0;
    margin-left: auto;
  }
}
</style>

<script setup>
import { onMounted } from 'vue'

import TheList from '@/components/TheList.vue'
import TheTools from '@/components/TheTools.vue'

import { useGetJobs } from '@/api/requests'
import { ref } from 'vue'

const { data, isLoading, execute } = useGetJobs()
const jobsLength = ref(0)

onMounted(async () => {
  await execute()
  jobsLength.value = Object.keys(data.value).length
})
</script>

<template>
  <div class="container">
    <v-progress-circular
      v-if="isLoading"
      class="d-block mx-auto mt-8"
      size="74"
      width="10"
      indeterminate
    />
    <v-row v-else justify-sm="center" justify-md="start">
      <v-col cols="12" sm="10" md="3" lg="3" class="d-flex flex-column align-end">
        <the-tools />
      </v-col>
      <v-col cols="12" sm="10" md="6" lg="6" class="d-flex flex-column">
        <the-list v-if="jobsLength" :job-list="data" />
        <h1 v-else class="mx-auto text-h4">Вакансий пока нет</h1>
      </v-col>
    </v-row>
  </div>
</template>

<style scoped>
.container {
  min-height: 100vh;
}
</style>

<script setup>
import JobsList from '@/components/Jobs/VueJobsList.vue'
import JobsTools from '@/components/Jobs/VueJobsTools.vue'

import { useJobsStore } from '@/store/jobs'
import { onMounted, watch } from 'vue'

const jobsStore = useJobsStore()

onMounted(() => {
  jobsStore.fetchJobsData()
})

watch(jobsStore.fetchQuery, () => {
  jobsStore.fetchJobsDataWithDebounce()
})
</script>

<template>
  <v-row justify-sm="center" justify-md="start">
    <v-col cols="12" sm="10" md="3" lg="3" class="d-flex flex-column align-end">
      <jobs-tools />
    </v-col>
    <v-col cols="12" sm="10" md="6" lg="6" class="d-flex flex-column">
      <v-progress-circular
        v-if="jobsStore.loading"
        class="d-block mx-auto mt-8"
        size="74"
        width="10"
        indeterminate
      />
      <jobs-list v-if="!jobsStore.loading && jobsStore.list" :list="jobsStore.list" />
      <span v-else-if="!jobsStore.list && !jobsStore.loading" class="mx-auto text-h4"
        >Вакансий пока нет</span
      >
    </v-col>
  </v-row>
</template>

<script setup>
import { onMounted } from 'vue'

import JobsList from '@/components/Jobs/VueJobsList.vue'
import JobsTools from '@/components/Jobs/VueJobsTools.vue'

import { useGetJobs } from '@/api/requests'
import { ref } from 'vue'

const { data, loading, execute } = useGetJobs()
const jobsLength = ref(0)

onMounted(async () => {
  await execute()
  jobsLength.value = Object.keys(data.value).length
})
</script>

<template>
    <v-progress-circular
      v-if="loading"
      class="d-block mx-auto mt-8"
      size="74"
      width="10"
      indeterminate
    />
    <v-row v-else justify-sm="center" justify-md="start">
      <v-col cols="12" sm="10" md="3" lg="3" class="d-flex flex-column align-end">
        <jobs-tools />
      </v-col>
      <v-col cols="12" sm="10" md="6" lg="6" class="d-flex flex-column">
        <jobs-list v-if="jobsLength" :list="data" />
        <span v-else class="mx-auto text-h4">Вакансий пока нет</span>
      </v-col>
    </v-row>
</template>

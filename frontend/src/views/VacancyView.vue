<script setup>
import { useRoute } from 'vue-router'
import { ref, onMounted, watch } from 'vue'
import { useGetVacancy } from '@/api/requests'
import TheJobsDetails from '@/components/TheJobsDetails.vue'

const { data, loading, error, execute } = useGetVacancy()
const vacancyId = ref('')
const route = useRoute()

watch(
  () => route.params.id,
  async (newVacancyId) => {
    vacancyId.value = newVacancyId
  }
)

onMounted(async () => {
  vacancyId.value = route.params.id
  await execute(vacancyId.value)
})
</script>

<template>
  <div class="container">
    <v-progress-circular
      v-if="loading"
      class="d-block mx-auto mt-8"
      size="74"
      width="10"
      indeterminate
    />
    <template v-else-if="error">
      <h1 class="text-center text-h4">{{ error.status }}</h1>
      <h3 class="text-center text-h5">{{ error.data.detail }}</h3>
    </template>
    <the-jobs-details v-else :data="data" />
  </div>
</template>

<style scoped>
.container {
  min-height: 100vh;
}
</style>

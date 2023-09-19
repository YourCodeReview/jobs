<script setup>
import { useRoute } from 'vue-router'
import { onMounted } from 'vue'
import { useVacancyStore } from '@/store/vacancy'

import VacancyDetails from '@/components/Vacancy/VueVacancyDetails.vue'

const vacancyStore = useVacancyStore()
const route = useRoute()

onMounted(() => {
  const id = route.params.id
  vacancyStore.changeId(id)
})
</script>

<template>
  <div class="container">
    <v-progress-circular
      v-if="vacancyStore.loading"
      class="d-block mx-auto mt-8"
      size="74"
      width="10"
      indeterminate
    />
    <template v-else-if="vacancyStore.error">
      <h1 class="text-center text-h4">{{ vacancyStore.error.status }}</h1>
      <h3 class="text-center text-h5">{{ vacancyStore.error.data.detail }}</h3>
    </template>
    <vacancy-details v-else :data="vacancyStore.vacancy" />
  </div>
</template>

<style scoped>
.container {
  min-height: 100vh;
}
</style>

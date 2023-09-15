<template>
  <div>
    <router-link
      v-for="job in props.jobList"
      :key="job.id"
      :to="{ name: 'Vacancy', params: { id: job.id } }"
    >
      <ui-card :item="job" />
    </router-link>
  </div>
</template>

<script setup>
import UiCard from '@/components/ui/uiCard.vue'

const props = defineProps({
  jobList: {
    type: Array
  }
})
</script>

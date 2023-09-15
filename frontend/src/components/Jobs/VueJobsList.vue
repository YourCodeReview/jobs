<script setup>
import UiCard from '@/components/_ui/uiCard.vue'

const props = defineProps({
  list: {
    type: Array
  }
})
</script>

<template>
  <div>
    <router-link
      v-for="job in props.list"
      :key="job.id"
      :to="{ name: 'Vacancy', params: { id: job.id } }"
    >
      <ui-card :item="job" />
    </router-link>
  </div>
</template>

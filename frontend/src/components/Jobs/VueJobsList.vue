<script setup>
import UiCard from '@/components/_ui/uiCard.vue'

const props = defineProps({
  list: {
    type: Array,
    required: true
  }
})

import { useRouter } from 'vue-router'
const router = useRouter()
const currentQueryParams = router.currentRoute.value.query

</script>

<template>
  <div>
    <router-link
      v-for="job in props.list"
      :key="job.id"
      :to="{ name: 'Vacancy', params: { id: job.id }, query: currentQueryParams }"
    >
      <ui-card :item="job" />
    </router-link>
  </div>
</template>

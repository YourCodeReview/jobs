<script setup>
import { watch } from 'vue';
import { useJobsStore } from '@/store/jobs'

const jobsStore = useJobsStore()

watch(() => jobsStore.page, jobsStore.editCurrentPage)
</script>

<template>
    <v-pagination
      class="pagination"
      v-model="jobsStore.page"
      :size="$vuetify.display.smAndUp ? 'default' : 'x-small'"
      rounded="circle"
      :total-visible="7"
      :length="jobsStore.pages"
    ></v-pagination>
</template>

<style scoped>
.pagination {
  position: sticky;
  bottom: 0;
  background-color: #f5f5f5;
}
</style>
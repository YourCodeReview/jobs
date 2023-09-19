<script setup>
import svgTelegram from '@/components/_icons/svgTelegram.vue'
import groups from '@/data/tools-groups.json'

import { useJobsStore } from '@/store/jobs'

const jobsStore = useJobsStore()

const fetchWithQuery = (event) => {
  jobsStore.changeQuery('specialities', event.target.value)
  jobsStore.fetchJobsDataWithDebounce()
}
</script>

<template>
  <v-expansion-panels variant="accordion" class="sticky-expansion-panels">
    <v-btn
      block
      class="px-6 py-4 font-weight-bold justify-start"
      height="70"
      rounded="xl"
      size="small"
      href="https://t.me/YCRJobs"
      target="_blank"
    >
      <span>{{ $vuetify.display.md ? 'Вакансии' : 'Вакансии в Telegram' }}</span>
      <template #prepend>
        <svg-telegram />
      </template>
    </v-btn>
    <v-expansion-panel v-for="group in groups" :key="group.title" :title="group.title" rounded="xl">
      <v-expansion-panel-text>
        <!-- <template v-if="group.queriesName === 'format'">
          <v-checkbox
            v-for="item in group.list"
            v-model="format"
            density="compact"
            hide-details
            :key="item.title"
            :label="item.title"
            :value="item.type"
          ></v-checkbox>
        </template>
        <template v-if="group.queriesName === 'salary'">
          <v-radio-group v-model="salary">
            <v-radio
              v-for="item in group.list"
              :key="item.title"
              :label="item.title"
              :value="item.type"
            />
          </v-radio-group>
        </template> -->
        <template v-if="group.queriesName === 'specialities'">
          <v-radio-group
            v-model="jobsStore.fetchQuery.specialities"
            @change="fetchWithQuery"
            hide-details
          >
            <v-radio
              class="mb-2"
              v-for="item in group.list"
              :key="item.title"
              :label="item.title"
              :value="item.type"
              density="compact"
              hide-details
            />
          </v-radio-group>
        </template>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
</template>

<style scoped>
.sticky-expansion-panels {
  position: sticky;
  top: 112px;

  max-width: 600px;
  margin: 0 auto;
}

@media screen and (min-width: 960px) {
  .sticky-expansion-panels {
    max-width: 280px;
    margin: 0;
    margin-left: auto;
  }
}
</style>

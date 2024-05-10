<script setup>
import groups from '@/data/tools-groups.json'
import CheckboxTools from '@/components/Jobs/VueCheckboxTools.vue'
import LocationsTools from '@/components/Jobs/VueLocationsTools.vue'
import SourceTools from '@/components/Jobs/VueSourceTools.vue'
import { useJobsStore } from '@/store/jobs'

const jobsStore = useJobsStore()

const fetchWithQuery = (event) => {
  jobsStore.changeQuery('specialities', event.target.value)
  jobsStore.fetchJobsDataWithDebounce()
}
</script>

<template>
  <v-expansion-panels variant="accordion" class="sticky-expansion-panels mb-2">
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
        <v-img width="30" height="30" src="/images/telegram.png" />
      </template>
    </v-btn>
    <v-expansion-panel
      v-for="group in groups"
      :key="group.title"
      :title="group.title"
      rounded="xl"
      class="mb-2"
    >
      <v-expansion-panel-text>
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
    <v-expansion-panel title="Фильтрация" rounded="xl" class="mb-2">
      <v-expansion-panel-text>
        <checkbox-tools />
        <v-divider />
      </v-expansion-panel-text>

      <v-expansion-panel-text>
        <source-tools />
        <v-divider />
      </v-expansion-panel-text>

      <v-expansion-panel-text>
        <locations-tools />
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

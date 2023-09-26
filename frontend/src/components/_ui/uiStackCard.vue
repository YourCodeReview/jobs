<script setup>
import { computed } from 'vue'

const props = defineProps({
  item: Object
})

const chips = ['Удаленная работа', 'Junior вакансии', 'Стажировки']

const currentComponent = computed(() => {
  switch (props.item.type) {
    case 'data':
      return 'data-science'
    case 'c#':
      return 'c-sharp'
    case 'java':
      return 'java'
    case 'python':
      return 'python'
    case 'qa':
      return 'qa'
    default:
      return 'js'
  }
})
</script>

<template>
  <v-card
    max-width="400"
    width="100%"
    class="pa-4 mx-auto d-flex flex-column justify-end"
    rounded="xl"
    elevation="10"
  >
    <v-row>
      <v-col cols="8" class="d-flex flex-column align-start">
        <v-chip class="mb-2" v-for="chip in chips" :key="chip" rounded="lg">{{ chip }}</v-chip>
      </v-col>
      <v-col cols="4" class="d-flex justify-end">
        <v-img width="100px" height="100px" :src="`/images/${currentComponent}.png`" />
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" class="pt-0">
        <span class="text-h4 font-weight-bold" :class="`text-${item.color}`">{{
          props.item.name
        }}</span>
      </v-col>
    </v-row>
  </v-card>
</template>
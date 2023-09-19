<script setup>
import { computed } from 'vue'

import svgDataScience from '@/components/_icons/svgDataScience.vue'
import svgCSharp from '@/components/_icons/svgCSharp.vue'
import svgJavaScript from '@/components/_icons/svgJavaScript.vue'
import svgJava from '@/components/_icons/svgJava.vue'
import svgPython from '@/components/_icons/svgPython.vue'
import svgQA from '@/components/_icons/svgQA.vue'

const props = defineProps({
  item: Object
})

const chips = ['Удаленная работа', 'Junior вакансии', 'Стажировки']

const currentComponent = computed(() => {
  switch (props.item.type) {
    case 'data science':
      return svgDataScience
    case 'c#':
      return svgCSharp
    case 'java':
      return svgJava
    case 'python':
      return svgPython
    case 'qa':
      return svgQA
    default:
      return svgJavaScript
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
        <component :is="currentComponent"></component>
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

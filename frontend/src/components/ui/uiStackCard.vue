<template>
    <v-card
        max-width="400"
        class="card pa-4 mx-auto"
        rounded="xl"
        elevation="10"
    >
      <v-row>
        <v-col cols="8">
          <v-chip-group class="flex-column align-start">
            <v-chip v-for="chip in chips" :key="chip" rounded="lg">{{ chip }}</v-chip>
          </v-chip-group>
        </v-col>
        <v-col cols="4" class="d-flex justify-end">
          <component :is="currentComponent"></component>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="12" class="pt-0">
          <span class="text-h4 font-weight-black" :class="`text-${item.color}`">{{ props.item.name }}</span>
        </v-col>
      </v-row>
    </v-card>
</template>

<script setup>
import svgDataScience from '../icons/svgDataScience.vue'
import svgCSharp from '../icons/svgCSharp.vue';
import svgJavaScript from '../icons/svgJavaScript.vue';
import svgJava from '../icons/svgJava.vue';
import svgPython from '../icons/svgPython.vue';
import svgQA from '../icons/svgQA.vue';
import { computed } from 'vue';

const currentComponent = computed(() => {
  switch (props.item.type) {
    case 'data-science':
      return svgDataScience;
    case 'c-sharp':
      return svgCSharp;
    case 'java':
      return svgJava;
    case 'python':
      return svgPython;
    case 'qa':
      return svgQA;
    default:
      return svgJavaScript;
  }
});

const props = defineProps({
    item: Object,
});

const chips = ['Удаленная работа', 'Junior вакансии', 'Стажировки']

</script>

<style scoped>
.card {
    display: flex;
    flex-direction: column;
    justify-content: end;
}
</style>
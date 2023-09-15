<template>
  <v-snackbar
    v-model="snackbar"
    :activator="props.activator"
    timeout="2000"
    location="top"
    :color="props.color"
  >
    {{ props.message }}
  </v-snackbar>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  modelValue: Boolean,
  isOpen: Boolean,
  message: String,
  activator: String,
  color: {
    type: String,
    default: 'red-darken-1'
  }
})
const emits = defineEmits(['update:modelValue'])

const snackbar = computed({
  get: () => props.modelValue,
  set: (value) => {
    emits('update:modelValue', value)
  }
})
</script>

<script setup>
defineProps({
  title: String
})
</script>

<template>
  <v-card>
    <v-card-item class="py-0 bg-blue">
      <v-card-title class="card-item"> {{ title }} </v-card-title>
    </v-card-item>
    <v-card-item class="py-0">
      <slot></slot>
    </v-card-item>
  </v-card>
</template>

<style scoped>
.card-item {
  font-size: 0.8rem;
  line-height: 1.3rem;
}
</style>

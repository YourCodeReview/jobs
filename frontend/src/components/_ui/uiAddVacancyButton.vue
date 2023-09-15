<template>
  <v-btn
    class="mx-1"
    height="50"
    rounded="lg"
    :variant="variant"
    :block="block"
    :to="{
      path: '/add'
    }"
  >
    Добавить вакансию
  </v-btn>
</template>

<script setup>
defineProps({
  variant: String,
  block: Boolean
})
</script>

<style scoped>
.v-btn {
  color: white;
  background-image: var(--purple-gradient);
}
.v-btn:hover {
  opacity: 0.8;
}
</style>

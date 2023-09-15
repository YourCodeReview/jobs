<script setup>
import NewVacancy from '@/components/NewVacancy/VueNewVacancy.vue'
</script>

<template>
  <div class="background">
    <new-vacancy />
  </div>
</template>

<style scoped>
.background {
  position: relative;

  background-image: var(--purple-gradient);
}

.container {
  max-width: 900px;
}

.btn__close {
  position: absolute;
  top: 25px;
  right: 25px;
}
</style>

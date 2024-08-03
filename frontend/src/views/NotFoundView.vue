<script setup>
import { useI18n } from 'vue-i18n'
const { t } = useI18n()
</script>

<template>
  <div class="container">
    <span class="d-block mx-auto text-h4 mb-6">{{ t('notFoundPage.notFound') }}</span>
    <v-btn class="btn__purple" @click="$router.back()" size="large" rounded="lg">{{
      t('backButton')
    }}</v-btn>
  </div>
</template>

<style scoped>
.container {
  min-height: 100vh;

  text-align: center;
}

.btn__purple {
  color: white;
  background-image: var(--purple-gradient);
}
.btn__purple:hover {
  opacity: 0.8;
}
</style>

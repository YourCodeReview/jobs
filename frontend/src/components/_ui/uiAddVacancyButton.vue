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
    {{ t('addButton') }}
  </v-btn>
</template>

<script setup>
import { useI18n } from 'vue-i18n'

defineProps({
  variant: String,
  block: Boolean
})

const { t } = useI18n()
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

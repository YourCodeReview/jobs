<script setup>
import svgLogo from '@/components/_icons/svgLogo.vue'
import uiAuthDialog from '../components/_ui/uiAuthDialog.vue'
</script>

<template>
  <div class="background pa-8 h-screen d-flex flex-column justify-center align-center">
    <svg-logo @click="$router.push({ name: 'Home' })" />
    <ui-auth-dialog @success="$router.back()" />
  </div>
</template>

<style scoped>
.background {
  position: relative;

  background-image: var(--purple-gradient);

  svg {
    margin-bottom: 20px;
  }
}

.btn__google {
  color: white;
  background-image: var(--blue-gradient);
}

.btn__close {
  position: absolute;
  top: 25px;
  right: 25px;
}
</style>

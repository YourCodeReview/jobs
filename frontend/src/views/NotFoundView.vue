<template>
  <div class="container">
    <span class="d-block mx-auto text-h4 mb-6">Такой страницы неть...</span>
    <v-btn class="btn__purple" @click="$router.back()" size="large" rounded="lg">Назад</v-btn>
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

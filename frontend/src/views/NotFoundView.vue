<template>
  <div class="container">
    <h1 class="mx-auto text-h4 mb-6">Такой страницы неть...</h1>
    <v-btn @click="$router.back()" size="large" rounded="lg">Назад</v-btn>
  </div>
</template>

<style scoped>
.container {
  min-height: 100vh;

  text-align: center;
}

.v-btn {
  color: white;
  background-image: var(--purple-gradient);
}
.v-btn:hover {
  opacity: 0.8;
}
</style>

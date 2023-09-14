<template>
    <div class="container">
        <h1 class="mx-auto text-h4 mb-6">Такой страницы неть...</h1>
        <v-btn @click="$router.back()" size="large" rounded="lg">Назад</v-btn>
    </div>
</template>

<style scoped>
.container {
    text-align: center;
    min-height: 100vh;
}

.v-btn {
    color: white;
    background-image: var(--purple-gradient);
}
.v-btn:hover {
    opacity: 0.8;
}
</style>
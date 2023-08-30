<script setup>
import TheHeader from './components/TheHeader.vue'
import ThePage from './components/ThePage.vue'
import TheFooter from './components/TheFooter.vue'
</script>

<template>
    <ThePage>
        <TheHeader />
        <router-view />
        <TheFooter />
    </ThePage>
</template>

<style scoped>
.page {
    display: grid;

    min-height: 100vh;

    grid-template-rows: min-content 1fr min-content;
}
</style>

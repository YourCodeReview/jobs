<template>
    <div class="page">
        <slot />
    </div>
</template>

<style scoped>
.page {
    display: grid;

    min-height: 100vh;

    grid-template-rows: min-content 1fr;
}
</style>

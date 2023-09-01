<script setup>
const props = defineProps({
    title: String
})
</script>

<template>
    <div class="layout">
        <div class="modal">
            <h3>{{ props.title }}</h3>
            <slot name="form" />
            <slot />
        </div>
    </div>
</template>

<style scoped>
.layout {
    position: absolute;
    z-index: 1000;
    top: 0;
    left: 0;

    display: flex;
    align-items: center;
    justify-content: center;

    width: 100%;
    height: 100%;

    background: rgba(0, 0, 0, 0.3);
}

.modal {
    display: flex;
    align-items: center;
    flex-direction: column;

    margin-bottom: 16px;
    padding: 16px;

    border-radius: 16px;
    background: white;
    box-shadow:
        0px -1px 20px rgba(0, 0, 0, 0.03),
        0px 16px 28px rgba(0, 0, 0, 0.04),
        0px 2px 10px rgba(0, 0, 0, 0.02),
        0px 0px 1px rgba(0, 0, 0, 0.04);

    gap: 10px;
}
</style>

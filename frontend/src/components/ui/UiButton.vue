<script setup>
const props = defineProps({
    color: {
        type: String,
        default: 'primary'
    },
    text: String
})
</script>

<template>
    <button class="button" :class="`button__${props.color}`">
        {{ props.text }}
    </button>
</template>

<style scoped>
.button {
    padding: 10px 20px;

    cursor: pointer;

    color: white;
    border: none;
    border-radius: 5px;

    font-weight: bold;
}

.button:hover {
    opacity: 0.9;
}

.button__primary {
    background-image: linear-gradient(33deg, rgba(0, 87, 255, 1) 0%, rgba(0, 228, 201, 1) 91%);
}

.button__black {
    background: black;
}
</style>

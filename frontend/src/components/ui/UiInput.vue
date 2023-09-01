<script setup>
import { ref, watch } from 'vue'

const emits = defineEmits(['update:modelValue'])

const inputValue = ref('')

watch(inputValue, (newValue) => {
    emits('update:modelValue', newValue)
})
</script>

<template>
    <input class="input" v-model="inputValue" />
</template>

<style scoped>
.input {
    padding: 10px 20px;

    border-radius: 5px;

    font-weight: bold;
}
</style>

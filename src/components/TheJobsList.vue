<script setup>
import UiCard from './ui/UiCard.vue'

const props = defineProps({
    jobs: Array
})
</script>

<template>
    <ul class="jobs-list">
        <li class="jobs-list__item" v-for="job in props.jobs" :key="job.id">
            <UiCard :job="job" />
        </li>
    </ul>
</template>

<style scoped>
.jobs-list {
    display: grid;

    width: fit-content;
    min-width: 600px;
    margin: 0 auto;

    list-style-type: none;

    grid-gap: 20px;
}
</style>

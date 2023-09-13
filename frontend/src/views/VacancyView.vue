<script setup>
import { useRoute } from "vue-router";
import { ref, onMounted, watch } from "vue";
import TheJobsDetails from '@/components/TheJobsDetails.vue';
import { useGetVacancy } from "@/api/requests";

const { data, isLoading, execute } = useGetVacancy();
const vacancyId = ref("");
const route = useRoute();

watch(
    () => route.params.id,
    async (newVacancyId) => {
        vacancyId.value = newVacancyId;
    }
);

onMounted(async () => {
    vacancyId.value = route.params.id;
    await execute(vacancyId.value);
});
</script>

<template>
    <div class="container">
        <v-progress-circular v-if="isLoading" class="d-block mx-auto mt-8" size="74" width="10" indeterminate />
        <the-jobs-details v-else :data="data"/>
    </div>
</template>

<style scoped>
.container {
    min-height: 100vh;
}
</style>

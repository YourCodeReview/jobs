<script setup>
import { onMounted } from "vue";

import TheList from "@/components/TheList.vue";
import TheTools from "@/components/TheTools.vue";

import { useGetJobs } from "@/api/requests";

const { data, isLoading, execute } = useGetJobs();

onMounted(async () => {
    await execute();
    console.log(data.value);
});
</script>

<template>
    <div class="container">
        <v-progress-circular v-if="isLoading" class="d-block mx-auto mt-8" size="74" width="10" indeterminate />
        <v-row v-else justify-sm="center" justify-md="start">
            <v-col
                cols="12"
                sm="10"
                md="3"
                lg="3"
                class="d-flex flex-column align-end"
            >
                <the-tools />
            </v-col>
            <v-col cols="12" sm="10" md="6" lg="6" class="d-flex flex-column">

                <the-list :job-list="data"/>
            </v-col>
        </v-row>
    </div>
</template>

<style scoped>
.container {
    min-height: 100vh;
}
</style>
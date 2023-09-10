<script setup>
import { onMounted } from "vue";

import TheList from "@/components/TheList.vue";
import TheTools from "@/components/TheTools.vue";

import { useGetJobs } from "@/api/requests";

const { data, isLoading, isError, execute } = useGetJobs();

onMounted(async () => {
    await execute();
    console.log("Ответ от сервера: ", data.value);
});
</script>

<template>
    <div class="container">
        <v-row justify-sm="center" justify-md="start">
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
                <the-list />
            </v-col>
        </v-row>
    </div>
</template>

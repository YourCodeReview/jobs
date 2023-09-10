<template>
    <v-dialog v-model="popup" activator="parent" width="auto">
        <v-card class="mx-auto px-6 pt-8 pb-4" max-width="344">
            <the-form :type="props.type" @close="popup = false" />
            <v-card-actions>
                <v-btn color="primary" block @click="popup = false"
                    >Закрыть</v-btn
                >
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script setup>
import { ref } from "vue";
import TheForm from "../TheForm.vue";

const props = defineProps({
    type: String,
});

const popup = ref(false);
</script>

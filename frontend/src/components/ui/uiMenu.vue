<script setup>
import { ref, computed } from "vue";
import { useFirebase } from "@/hooks/useFirebase";

import UiLoginButton from "@/components/ui/uiLoginButton.vue"
import UiLogoutButton from "@/components/ui/uiLogoutButton.vue";
import UiCareerButton from "@/components/ui/uiCareerButton.vue";

defineProps({
    list: Array,
});

const auth = useFirebase();
const menu = ref(false);

const showLoginButton = computed(() => !auth.isLoggedIn.value);
</script>


<template>
    <div class="text-center">
        <v-menu v-model="menu" :close-on-content-click="false" location="start" transition="slide-x-reverse-transition">
            <template v-slot:activator="{ props }">
                <v-btn color="white" v-bind="props" icon>
                    <v-icon>mdi-menu</v-icon>
                </v-btn>
            </template>
            <v-card height="300" class="d-flex flex-column align-center pa-4 bg-white" rounded="lg">
                <UiCareerButton variant="flat" block/>
                <UiLoginButton v-if="showLoginButton" variant="flat" block/>
                <UiLogoutButton v-else variant="flat" block/>
                <slot />
            </v-card>
        </v-menu>
    </div>
</template>
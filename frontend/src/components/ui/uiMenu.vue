<template>
    <div class="text-center">
        <v-menu v-model="menu" :close-on-content-click="false" location="start" transition="slide-x-reverse-transition">
            <template v-slot:activator="{ props }">
                <v-btn color="white" v-bind="props" icon="mdi-menu"></v-btn>
            </template>
            <v-card height="300" class="d-flex flex-column pa-4 bg-white" rounded="lg">
                <v-btn
                    height="60"
                    class="px-4 mx-lg-2"
                    color="lime"
                    rounded="lg"
                    variant="flat"
                    href="https://yourcodereview.com/"
                >
                    <span class="text-wrap"> Карьерная поддержка </span>
                </v-btn>
                <v-btn
                    v-if="!auth.isLoggedIn.value"
                    height="50"
                    class="px-4 mx-1 mx-lg-2"
                    rounded="lg"
                    variant="flat"
                    :to="{
                        path: '/login',
                        query: { type: 'login' },
                    }"
                >
                    Войти
                </v-btn>
                <v-btn
                    v-else
                    height="50"
                    class="px-2 mx-1 mx-lg-2"
                    rounded="lg"
                    variant="flat"
                    @click="auth.logoutUser()"
                >
                    Выйти
                </v-btn>
                <slot />
            </v-card>
        </v-menu>
    </div>
</template>

<script setup>
import { ref } from "vue";
import { useFirebase } from "@/hooks/useFirebase";

defineProps({
    list: Array,
});

const auth = useFirebase();
const menu = ref(false);
</script>

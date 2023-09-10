<script setup>
import { useFirebase } from "@/hooks/useFirebase";

import svgLogo from "./icons/svgLogo.vue";
import TheNavigation from "./TheNavigation.vue";
import uiMenu from "./ui/uiMenu.vue";

const auth = useFirebase();

const links = [
    {
        title: "Комьюнити",
        url: "https://t.me/YourCodeReview",
    },
    {
        title: "Полезные материалы",
        url: "https://blog.yourcodereview.com/category/career/",
    },
    {
        title: "Блог",
        url: "https://blog.yourcodereview.com/",
    },
];

</script>

<template>
    <v-app-bar class="text-white" :elevation="3" height="80">
        <template v-slot:image>
            <v-img
                gradient="to top right, rgba(32 147 254 / 90%), rgba(230 23 254 / 90%) 90%"
            ></v-img>
        </template>
        <div class="container py-6">
            <v-row justify="space-between">
                <v-col
                    cols="6"
                    sm="4"
                    md="4"
                    lg="3"
                    class="d-flex justify-start align-center"
                >
                    <v-app-bar-title>
                        <router-link to="/" class="d-flex">
                            <svg-logo />
                        </router-link>
                    </v-app-bar-title>
                </v-col>
                <v-col
                    cols="6"
                    sm="7"
                    md="8"
                    lg="9"
                    class="d-flex justify-end align-center"
                >
                    <the-navigation
                        v-if="$vuetify.display.lgAndUp"
                        :links="links"
                    />
                    <v-btn
                        v-if="$vuetify.display.smAndUp"
                        height="50"
                        class="custom-btn mx-1 mx-lg-2"
                        color="lime"
                        variant="elevated"
                        rounded="lg"
                        href="https://yourcodereview.com/"
                    >
                        Карьерная поддержка
                    </v-btn>
                    <v-btn
                        v-if="!auth.isLoggedIn.value"
                        class="mx-1 mx-lg-2"
                        width="120"
                        height="50"
                        variant="elevated"
                        rounded="lg"
                        :to="{
                            path: '/login',
                            query: { type: 'login' },
                        }"
                    >
                        Войти
                    </v-btn>
                    <v-btn
                        width="120"
                        height="50"
                        class="mx-1 mx-lg-2"
                        v-else
                        variant="elevated"
                        rounded="lg"
                        @click="auth.logoutUser()"
                    >
                        Выйти
                    </v-btn>
                    <ui-menu v-if="$vuetify.display.mdAndDown">
                        <the-navigation :links="links" />
                    </ui-menu>
                </v-col>
            </v-row>
        </div>
    </v-app-bar>
</template>
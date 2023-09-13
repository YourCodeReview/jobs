<script setup>
import { computed } from "vue";
import { useFirebase } from "@/hooks/useFirebase";

import TheNavigation from "./TheNavigation.vue";

import UiLoginButton from "./ui/uiLoginButton.vue"
import UiLogoutButton from "./ui/uiLogoutButton.vue";
import UiCareerButton from "./ui/uiCareerButton.vue";
import UiMenu from "./ui/uiMenu.vue";

import SvgLogo from "./icons/svgLogo.vue";

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

const showLoginButton = computed(() => !auth.isLoggedIn.value);

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
          <v-col cols="6" sm="4" md="4" lg="3" class="d-flex justify-start align-center">
            <v-app-bar-title>
              <router-link to="/" class="d-flex">
                <SvgLogo />
              </router-link>
            </v-app-bar-title>
          </v-col>
          <v-col cols="6" sm="7" md="8" lg="9" class="d-flex justify-end align-center">
            <TheNavigation v-if="$vuetify.display.lgAndUp" :links="links" />
            <UiCareerButton v-if="$vuetify.display.smAndUp" variant="elevated"/>
            <UiLoginButton v-if="showLoginButton" variant="elevated"/>
            <UiLogoutButton v-else variant="elevated"/>
            <UiMenu v-if="$vuetify.display.mdAndDown">
              <TheNavigation :links="links" />
            </UiMenu>
          </v-col>
        </v-row>
      </div>
    </v-app-bar>
  </template>
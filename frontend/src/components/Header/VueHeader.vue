<script setup>
import { computed } from 'vue'
import { useFirebase } from '@/hooks/useFirebase'

import HeaderNavigation from '@/components/Header/VueHeaderNavigation.vue'

import UiLoginButton from '@/components/_ui/uiLoginButton.vue'
import UiLogoutButton from '@/components/_ui/uiLogoutButton.vue'
import UiCareerButton from '@/components/_ui/uiCareerButton.vue'
import UiMenu from '@/components/_ui/uiMenu.vue'

import SvgLogo from '@/components/_icons/svgLogo.vue'

import { useRouter } from 'vue-router'

const auth = useFirebase()

const links = [
  {
    title: 'Комьюнити',
    url: 'https://t.me/YourCodeReview'
  },
  {
    title: 'Полезные материалы',
    url: 'https://blog.yourcodereview.com/category/career/'
  },
  {
    title: 'Блог',
    url: 'https://blog.yourcodereview.com/'
  }
]

const showLoginButton = computed(() => !auth.isLoggedIn.value)

const router = useRouter()
const currentQueryParams = router.currentRoute.value.query

</script>

<template>
  <v-app-bar class="text-white" :elevation="3" height="80">
    <template v-slot:image>
      <v-img gradient="to top right, rgba(32 147 254 / 90%), rgba(230 23 254 / 90%) 90%"></v-img>
    </template>
    <div class="container py-6">
      <v-row justify="space-between">
        <v-col cols="6" sm="4" md="4" lg="3" class="d-flex justify-start align-center">
          <v-app-bar-title>
            <router-link :to="{ path: '/', query: currentQueryParams }" class="d-flex">
              <svg-logo />
            </router-link>
          </v-app-bar-title>
        </v-col>
        <v-col cols="6" sm="7" md="8" lg="9" class="d-flex justify-end align-center">
          <header-navigation v-if="$vuetify.display.lgAndUp" :links="links" />
          <ui-career-button v-if="$vuetify.display.smAndUp" variant="elevated" />
          <ui-login-button v-if="showLoginButton" variant="elevated" />
          <ui-logout-button v-else variant="elevated" />
          <ui-menu v-if="$vuetify.display.mdAndDown">
            <header-navigation :links="links" />
          </ui-menu>
        </v-col>
      </v-row>
    </div>
  </v-app-bar>
</template>

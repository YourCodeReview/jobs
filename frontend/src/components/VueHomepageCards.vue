<script setup>
import uiStackCard from '@/components/_ui/uiStackCard.vue'
import UiLanguageButton from '@/components/_ui/uiLanguageButton.vue'
import svgLogo from '@/components/_icons/svgLogo.vue'

import cards from '@/data/welcome-cards.json'
import { useJobsStore } from '@/store/jobs'

import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
const router = useRouter()
const jobsStore = useJobsStore()

const fetchWithQuery = (newValue) => {
  jobsStore.changeQuery('specialities', newValue)
  router.push({ name: 'Jobs' })
}
</script>

<template>
  <div class="welcome background">
    <header class="pt-1 pb-4">
      <div class="container px-4 py-6">
        <v-row>
          <router-link class="flex-fill" :to="{ name: 'Home' }">
            <svg-logo />
          </router-link>
          <ui-language-button />
        </v-row>
        <h1 class="text-sm-h2 text-center mt-auto font-weight-bold">
          {{ t('homePage.title') }}
        </h1>
        <p class="text-sm-h4 text-center mt-8">
          {{ t('homePage.subtitle') }}
        </p>
      </div>
    </header>
    <div class="container pt-2 justify-center">
      <div class="grid-cards">
        <ui-stack-card
          v-for="item in cards"
          :key="item.id"
          @click="fetchWithQuery(item.type)"
          :item="item"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.welcome {
  display: grid;

  min-height: 100vh;

  grid-template-rows: minmax(200px, 350px) 1fr;
}

.container {
  display: flex;
  flex-direction: column;

  height: 100%;
}
.grid-cards {
  display: grid;

  grid-template-columns: repeat(auto-fill, minmax(330px, 1fr));
  grid-auto-flow: dense;
  gap: 12px;
}

.background {
  background-image: var(--purple-gradient);
}

@media screen and (max-width: 550px) {
  .grid-cards {
    grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
  }
}
</style>

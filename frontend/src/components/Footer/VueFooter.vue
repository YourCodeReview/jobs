<script setup>
import { computed } from 'vue'
import { useTranslation } from '@/hooks/useTranslation'
import ContactSection from '@/components/Footer/VueFooterContacts.vue'
import NavigationSection from '@/components/Footer/VueFooterNavigation.vue'

import contacts from '@/data/contacts.json'
import anchorsRu from '@/data/anchors.ru.json'
import anchorsEn from '@/data/anchors.en.json'
import linksRu from '@/data/links.ru.json'
import linksEn from '@/data/links.en.json'

const { locale } = useTranslation()

const links = computed(() => {
  switch (locale.value) {
    case 'ru':
      return linksRu
    case 'en':
      return linksEn
    default:
      return linksRu
  }
})

const anchors = computed(() => {
  switch (locale.value) {
    case 'ru':
      return anchorsRu
    case 'en':
      return anchorsEn
    default:
      return anchorsRu
  }
})
</script>

<template>
  <v-footer class="footer px-0 py-6">
    <div class="container">
      <v-row>
        <contact-section :contacts="contacts" />
        <v-spacer />
        <navigation-section v-if="links.length" :anchors="anchors" :links="links" />
      </v-row>
    </div>
  </v-footer>
</template>
<style scoped>
.footer {
  color: white;
  background-color: #070012;
}
</style>

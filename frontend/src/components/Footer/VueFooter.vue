<script setup>
import ContactSection from '@/components/Footer/VueFooterContacts.vue'
import NavigationSection from '@/components/Footer/VueFooterNavigation.vue'

import contacts from '@/data/contacts.json'
import anchors from '@/data/anchors.json'
import links from '@/data/links.json'

</script>

<template>
  <v-footer class="footer px-0 py-6">
    <div class="container">
      <v-row>
        <contact-section :contacts="contacts" />
        <v-spacer />
        <navigation-section :anchors="anchors" :links="links" />
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

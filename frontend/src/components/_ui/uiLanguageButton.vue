<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()

const languages = [
  { title: 'RU', value: 'ru' },
  { title: 'EN', value: 'en' }
]

const currentLanguageLabel = computed(() => {
  return languages.filter((l) => l.value === locale.value)[0].title || 'unknown'
})

const switchLanguage = (langItem) => {
  locale.value = langItem.value
  localStorage.setItem('language', langItem.value)
}
</script>

<template>
  <div class="d-flex justify-space-around">
    <v-menu transition="scale-transition">
      <template v-slot:activator="{ props }">
        <v-btn class="text-none bg-none" prepend-icon="mdi-web" variant="text" v-bind="props">
          {{ currentLanguageLabel }}
        </v-btn>
      </template>

      <v-list base-color="white" bg-color="#C644FE">
        <v-list-item v-for="(langItem, i) in languages" :key="i">
          <v-list-item-title>
            <v-btn class="text-none bg-none" variant="text" @click="switchLanguage(langItem)">{{
              langItem.title
            }}</v-btn>
          </v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

import { createI18n } from 'vue-i18n'
import ru from './languages/ru.json'
import en from './languages/en.json'

export const i18n = createI18n({
  legacy: false,
  locale: localStorage.getItem('language') || 'ru',
  fallbackLocale: 'ru',
  messages: {
    ru,
    en
  }
})

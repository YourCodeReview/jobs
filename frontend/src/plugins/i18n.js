import { createI18n } from 'vue-i18n'

export const i18n = createI18n({
  legacy: false,
  locale: 'ru',
  fallbackLocale: 'ru',
  messages: {
    ru: {
      homePage: {
        title: 'Junior вакансии и стажировки',
        subtitle: 'Всё, что нужно, чтобы найти первую работу разработчиком'
      },
      homeCard: {
        remoteBadge: 'Удаленная работа',
        vacanciesBadge: 'Junior вакансии',
        internshipsBadge: 'Стажировки'
      }
    },
    en: {
      homePage: {
        title: 'Junior vacancies and internships',
        subtitle: 'Everything you need to find your first job as a developer'
      },
      homeCard: {
        remoteBadge: 'Remote job',
        vacanciesBadge: 'Junior vacancies',
        internshipsBadge: 'Internships'
      }
    }
  }
})

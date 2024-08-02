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
      },
      headerNavigation: {
        community: 'КОМЬЮНИТИ',
        useful: 'ПОЛЕЗНЫЕ МАТЕРИАЛЫ',
        blog: 'БЛОГ'
      },
      careerButton: 'КАРЬЕРНАЯ ПОДДЕРЖКА',
      authButton: {
        logIn: 'ВОЙТИ',
        logOut: 'ВЫЙТИ'
      },
      jobsTools: {
        vacancies: 'Вакансии',
        vacanciesTelegram: 'Вакансии в Telegram',
        specialization: 'Специализация',
        city: 'Город',
        source: 'Источник вакансии',
        additionally: 'Дополнительно'
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
      },
      headerNavigation: {
        community: 'COMMUNITY',
        useful: 'USEFUL MATERIALS',
        blog: 'BLOG'
      },
      careerButton: 'CAREER SUPPORT',
      authButton: {
        logIn: 'LOGIN',
        logOut: 'LOGOUT'
      },
      jobsTools: {
        vacancies: 'Vacancies',
        vacanciesTelegram: 'Vacancies in Telegram',
        specialization: 'Specialization',
        city: 'City',
        source: 'Source of vacancy',
        additionally: 'Additionally'
      }
    }
  }
})

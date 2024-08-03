import { createI18n } from 'vue-i18n'

export const i18n = createI18n({
  legacy: false,
  locale: localStorage.getItem('language') || 'ru',
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
      jobCard: {
        remoteBadge: 'Удаленно',
        internshipsBadge: 'Стажировка',
        noSalary: 'з/п не указана'
      },
      loginPage: {
        email: 'Почта',
        emailPlaceholder: 'Введите почту',
        password: 'Пароль',
        passwordPlaceholder: 'Введите пароль'
      },
      newVacancyPage: {
        title: 'Разместить вакансию',
        subtitle: 'Размещать вакансии здесь можно бесплатно. Просто заполните форму ниже.',
        default: {
          employment: 'Полная занятость',
          schedule: 'Офис',
          description: '<p>Описание вакансии!</p>'
        },
        errorMessage: 'Поле должно быть заполнено',
        emailErrorMessage: 'Введите действительный адрес электронной почты',
        beforeTaxes: 'До вычета налогов',
        salaryFrom: 'Зарплата от',
        salaryUpTo: 'До',
        currency: 'Валюта',
        name: 'Ваше имя',
        submit: 'Отправить'
      },
      notFoundPage: {
        notFound: 'Такой страницы нет...'
      },
      headerNavigation: {
        community: 'КОМЬЮНИТИ',
        useful: 'ПОЛЕЗНЫЕ МАТЕРИАЛЫ',
        blog: 'БЛОГ'
      },
      careerButton: 'КАРЬЕРНАЯ ПОДДЕРЖКА',
      backButton: 'Назад',
      addButton: 'Добавить вакансию',
      authButton: {
        logIn: 'ВОЙТИ',
        logOut: 'ВЫЙТИ',
        signUp: 'Зарегистрироваться',
        google: 'Войти через Google'
      },
      jobsTools: {
        vacancies: 'Вакансии',
        vacanciesTelegram: 'Вакансии в Telegram',
        specialization: 'Специализация',
        city: 'Город',
        cityPlaceholder: 'Выберете город',
        source: 'Источник вакансии',
        additionally: 'Дополнительно'
      },
      noVacancies: 'Вакансий пока нет'
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
      jobCard: {
        remoteBadge: 'Remotely',
        internshipsBadge: 'Internship',
        noSalary: 'Salary not specified'
      },
      loginPage: {
        email: 'Email',
        emailPlaceholder: 'Enter your email',
        password: 'Password',
        passwordPlaceholder: 'Enter your password'
      },
      newVacancyPage: {
        title: 'Post a vacancy',
        subtitle: 'You can post vacancies here for free. Just fill out the form below.',
        default: {
          employment: 'Full-time',
          schedule: 'Office',
          description: '<p>Vacancy description!</p>'
        },
        errorMessage: 'The field must be filled',
        emailErrorMessage: 'Please enter a valid email address',
        beforeTaxes: 'Before taxes',
        salaryFrom: 'Salary from',
        salaryUpTo: 'Up to',
        currency: 'Currency',
        name: 'Your name',
        submit: 'Submit'
      },
      notFoundPage: {
        notFound: 'There is no such page...'
      },
      headerNavigation: {
        community: 'COMMUNITY',
        useful: 'USEFUL MATERIALS',
        blog: 'BLOG'
      },
      careerButton: 'CAREER SUPPORT',
      backButton: 'Back',
      addButton: 'Add a vacancy',
      authButton: {
        logIn: 'LOGIN',
        logOut: 'LOGOUT',
        signUp: 'SIGNUP',
        google: 'Login via Google'
      },
      jobsTools: {
        vacancies: 'Vacancies',
        vacanciesTelegram: 'Vacancies in Telegram',
        specialization: 'Specialization',
        city: 'City',
        cityPlaceholder: 'Select a city',
        source: 'Source of vacancy',
        additionally: 'Additionally'
      },
      noVacancies: 'There are no vacancies yet'
    }
  }
})

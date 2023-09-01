import { defineStore } from 'pinia'
import vacancies from '../data/vacancies.json'
import vacancy from '../data/vacancy.json'

export const useStateStore = defineStore('state', () => {
    const headerLinks = [
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
    const footerAnchors = [
        {
            name: 'Программа и тестирование',
            anchor: 'programma'
        },
        {
            name: 'Вопросы и ответы',
            anchor: 'faq'
        },
        {
            name: 'Вакансии',
            anchor: 'vakansii'
        },
        {
            name: 'Тарифы',
            anchor: 'tarifi'
        },
        {
            name: 'Запись',
            anchor: 'zapis'
        },
        {
            name: 'Команда',
            anchor: 'komanda'
        },
        {
            name: 'Отзывы',
            anchor: 'otzivi'
        },
        {
            name: 'О нас',
            anchor: 'onas'
        },
    ]

    return { vacancies, vacancy, headerLinks, footerAnchors }
})

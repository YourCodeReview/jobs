<script setup>
import TheContactSection from './TheContactSection.vue';
import TheNavigationSection from './TheNavigationSection.vue';

const contacts = [
    {
        name: "+7 (499) 110-82-76",
        href: "tel:7499108276",
    },
    {
        name: "yourcodereview@gmail.com",
        href: "mailto:yourcodereview@gmail.com",
    },
];
const anchors = [
    {
        name: "Программа и тестирование",
        anchor: "programma",
    },
    {
        name: "Вакансии",
        anchor: "vakansii",
    },
    {
        name: "Тарифы",
        anchor: "tarifi",
    },
    {
        name: "Запись",
        anchor: "zapis",
    },
    {
        name: "Команда",
        anchor: "komanda",
    },
    {
        name: "Отзывы",
        anchor: "otzivi",
    },
    {
        name: "О нас",
        anchor: "onas",
    },
    {
        name: "Вопросы и ответы",
        anchor: "faq",
    },
];
const links = [
    {
        name: "Блог",
        href: "https://blog.yourcodereview.com",
    },
    {
        name: 'Тест "Возьмут ли меня в IT"',
        href: "https://mrqz.me/6400c6ab9c4e9c004d2fecfa",
    },
];
</script>

<template>
    <v-footer class="footer px-0 py-6">
        <div class="container">
            <v-row>
                <the-contact-section :contacts="contacts"/>
                <v-spacer />
                <the-navigation-section :anchors="anchors" :links="links"/>
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

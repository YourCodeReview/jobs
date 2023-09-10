<script setup>
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
                <v-col cols="12" md="4" sm="12" class="d-flex flex-column py-1">
                    <v-btn
                        class="justify-start"
                        variant="text"
                        href="https://yourcodereview.com"
                        >&#60; codereview &#47;&#62;</v-btn
                    >
                    <div class="mt-auto">
                        <v-btn
                            v-for="contact in contacts"
                            :key="contact.name"
                            class="justify-start"
                            variant="text"
                            :href="contact.href"
                            block
                            >{{ contact.name }}</v-btn
                        >
                    </div>
                </v-col>
                <v-spacer />
                <v-col cols="12" md="8" sm="12">
                    <v-row>
                        <v-col
                            class="py-1"
                            cols="12"
                            md="6"
                            sm="6"
                            v-for="(item, index) in anchors"
                            :key="index"
                        >
                            <v-btn
                                variant="text"
                                :href="`https://yourcodereview.com/#${item.anchor}`"
                            >
                                {{ item.name }}
                            </v-btn>
                        </v-col>
                        <v-col
                            v-for="(link, index) in links"
                            :key="index"
                            class="py-1"
                            cols="12"
                            md="6"
                            sm="6"
                        >
                            <v-btn
                                variant="text"
                                :href="link.href"
                                >{{ link.name }}</v-btn
                            >
                        </v-col>
                    </v-row>
                </v-col>
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

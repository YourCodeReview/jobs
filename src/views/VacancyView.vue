<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { useStateStore } from '../stores'
import { useAuthStore } from '../stores/auth'

import UiCard from '../components/ui/UiCard.vue'
import UiButton from '../components/ui/UiButton.vue'

import SvgBack from '../components/icons/SvgBack.vue'
import { useModalStore } from '../stores/modal'

const store = useStateStore()
const auth = useAuthStore()
const modal = useModalStore()

const route = useRoute()

const vacancyId = ref('')
const currentVacancy = ref({})

const responseVacancy = (url) => {
    auth.isLoggedIn ? window.open(url, '_blank') : modal.open()
}

onMounted(async () => {
    vacancyId.value = route.params.id
    currentVacancy.value = store.vacancy
})

watch(
    () => route.params.id,
    async (newVacancyId) => {
        vacancyId.value = newVacancyId
        // currentVacancy = ЗАПРОС
    }
)
</script>

<template>
    <main class="vacancy">
        <div class="container vacancy-container">
            <div class="fixed-navigation">
                <router-link class="fixed-navigation__link" to="/">
                    <SvgBack />
                </router-link>
            </div>
            <UiCard :job="currentVacancy" size="large" />
            <div class="vacancy-description">
                <div class="vacancy-description__left">
                    <div class="vacancy-description__salary">{{ currentVacancy.salary }} ₽</div>
                    <div class="vacancy-description__text">
                        <h3 class="vacancy-description__title">{{ currentVacancy.title }}</h3>
                        <ul
                            class="description-list"
                            v-for="(section, idx) in currentVacancy.description"
                            :key="idx"
                        >
                            <li class="description-list__item">
                                <p>{{ section.title }}</p>
                                <ul>
                                    <li v-for="(item, idx) in section.list" :key="idx">
                                        <span>{{ item }}</span>
                                    </li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
                <div class="vacancy-description__right">
                    <div class="button-response">
                        <p>Отклик</p>
                        <UiButton text="Откликнуться" @click="responseVacancy(currentVacancy.url)"/>
                    </div>
                </div>
            </div>
        </div>
    </main>
</template>

<style scoped>
.vacancy {
    position: relative;

    display: grid;

    height: 100%;

    grid-template-columns: 1fr;
}
.vacancy-container {
    display: flex;
    flex-direction: column;

    max-width: 960px;

    gap: 10px;
}

.vacancy-description__salary {
    margin-bottom: 16px;
    padding: 16px;

    border-radius: 16px;
    background: white;
    box-shadow:
        0px -1px 20px rgba(0, 0, 0, 0.03),
        0px 16px 28px rgba(0, 0, 0, 0.04),
        0px 2px 10px rgba(0, 0, 0, 0.02),
        0px 0px 1px rgba(0, 0, 0, 0.04);

    font-size: 20px;
    font-weight: 700;
}

.vacancy-description {
    position: relative;
    z-index: 21;

    display: flex;

    gap: 10px;
}

.vacancy-description__text {
    margin-bottom: 16px;
    padding: 16px;

    border-radius: 16px;
    background: white;
    box-shadow:
        0px -1px 20px rgba(0, 0, 0, 0.03),
        0px 16px 28px rgba(0, 0, 0, 0.04),
        0px 2px 10px rgba(0, 0, 0, 0.02),
        0px 0px 1px rgba(0, 0, 0, 0.04);
}

.vacancy-description__title {
    margin-bottom: 10px;
}

.fixed-navigation {
    position: fixed;
    top: 98px;
    left: 50%;

    width: 100%;
    max-width: 1024px;
    padding: 4px 16px;

    transform: translate(-50%);
}

.fixed-navigation__link {
    display: inline-block;

    padding: 10px 10px;

    border-radius: 50%;
    box-shadow:
        0px -1px 20px rgba(0, 0, 0, 0.1),
        0px 16px 28px rgba(0, 0, 0, 0.11),
        0px 2px 10px rgba(0, 0, 0, 0.09),
        0px 0px 1px rgba(0, 0, 0, 0.11);
}

.description-list__item {
    margin-bottom: 15px;
}
.description-list__item p {
    margin-bottom: 5px;

    font-weight: bold;
}
.description-list__item ul {
    padding-left: 20px;

    list-style: disc;
}

.button-response {
    margin-bottom: 16px;
    padding: 16px;

    border-radius: 16px;
    background: white;
    box-shadow:
        0px -1px 20px rgba(0, 0, 0, 0.03),
        0px 16px 28px rgba(0, 0, 0, 0.04),
        0px 2px 10px rgba(0, 0, 0, 0.02),
        0px 0px 1px rgba(0, 0, 0, 0.04);
}
.button-response p {
    margin-bottom: 10px;

    font-weight: bold;
}

@media screen and (max-width: 1024px) {
    .fixed-navigation {
        position: static;
        transform: translate(0);
    }
}

@media screen and (max-width: 680px) {

    .vacancy-description {
        flex-direction: column;
    }
}
</style>

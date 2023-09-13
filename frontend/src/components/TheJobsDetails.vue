<script setup>
import { ref, onMounted, watch } from "vue";
import { useRoute } from "vue-router";
import { useFirebase } from "@/hooks/useFirebase";
import { useGetVacancy } from "@/api/requests";

import UiCard from "@/components/ui/uiCard.vue";
import UiSnackbar from "@/components/ui/uiSnackbar.vue";

const { execute } = useGetVacancy();
const route = useRoute();
const auth = useFirebase();

const vacancyId = ref("");
const snackbar = ref(false);
const dialog = ref(false);

const currentVacancy = {
    hh_id: "85740036",
    name: "Junior PHP разработчик",
    title: "We are seeking a skilled Python Developer to join our dynamic team. If you have a passion for writing clean, maintainable code and a strong background in Python, we want to hear from you!",
    description: [
        {
            title: "Responsibilities",
            list: [
                "Collaborate with cross-functional teams to design and develop high-quality software",
                "Write efficient, reusable, and documented code.",
                "Participate in code reviews and provide constructive feedback.",
            ],
        },
        {
            title: "Requirements",
            list: [
                "Bachelor's degree in Computer Science or related field.",
                "Proven experience with Python and its frameworks.",
                "Strong problem-solving skills and attention to detail.",
                "Excellent teamwork and communication skills.",
            ],
        },
    ],
    salary_from: 800,
    salary_to: null,
    salary_currency: "USD",
    area: "Минск",
    employer: "Спортдата",
    url: "https://example.com/job/python-developer",
};

watch(
    () => route.params.id,
    async (newVacancyId) => {
        vacancyId.value = newVacancyId;
    }
);

onMounted(async () => {
    vacancyId.value = route.params.id;
    await execute(vacancyId.value);
});

const copyText = () => {
    navigator.clipboard
        .writeText(`${currentVacancy.url}`)
        .then(() => {
            console.log("Async: Copying to clipboard was successful!");
        })
        .catch((err) => {
            console.log("Something went wrong", err);
        });
};
</script>

<template>
    <div class="container py-4 position-relative">
        <v-row class="page-nav justify-center">
            <v-col cols="12" class="d-flex py-1">
                <v-btn icon="mdi-arrow-left" size="small" @click="$router.back()" />
                <v-btn class="ml-auto" icon size="small" @click="auth.isLoggedIn.value ? copyText() : null">
                    <v-icon>mdi-export-variant</v-icon>
                    <ui-snackbar v-model="snackbar" activator="parent"
                        :color="auth.isLoggedIn.value ? 'green' : 'red-darken-1'"
                        :message="auth.isLoggedIn.value ? 'Ссылка на вакансию скопирована' : 'Необходимо авторизоваться'" />
                </v-btn>
            </v-col>
        </v-row>
        <v-row class="justify-center">
            <v-col cols="12" lg="10" sm="12">
                <ui-card :item="currentVacancy" size="lg" />
            </v-col>
        </v-row>
        <v-row class="justify-center">
            <v-col cols="12" lg="7" sm="8" class="d-flex flex-column">
                <v-card class="pa-2" rounded="xl">
                    <v-card-title class="font-weight-bold">
                        от {{ currentVacancy.salary_from }} {{ currentVacancy.salary_to ? `- ${currentVacancy.salary_to}` :
                            '' }} {{ currentVacancy.salary_currency }}
                    </v-card-title>
                </v-card>
                <v-hover v-slot="{ isHovering, props }">
                    <v-card v-bind="props" class="blue-banner mt-2 pa-2" rounded="xl" :elevation="isHovering ? 10 : 1"
                        href="https://yourcodereview.com/">
                        <v-card-title class="d-flex align-center font-weight-bold">
                            Как зарабатывать больше?
                            <v-icon class="ml-auto" color="white" icon="mdi-arrow-right" />
                        </v-card-title>
                        <v-card-text>
                            Расскажем в наших карьерных консультациях
                        </v-card-text>
                    </v-card>
                </v-hover>
                <v-card class="mt-2 pa-2" rounded="xl">
                    <v-list v-for="item in currentVacancy.description" :key="item.title">
                        <v-list-item>
                            <v-list-item-title class="font-weight-bold">{{
                                item.title
                            }}</v-list-item-title>
                            <v-card-text v-for="item in item.list" :key="item" class="py-2">
                                - {{ item }}
                            </v-card-text>
                        </v-list-item>
                    </v-list>
                </v-card>
            </v-col>
            <v-col cols="12" lg="3" sm="4">
                <v-card class="pa-4 d-flex flex-column" rounded="xl">
                    <v-card-title class="pa-0 pb-1 font-weight-bold">Отклик</v-card-title>
                    <v-btn block size="large" class="card-btn__purple mb-2" rounded="lg">
                        Турбо отклик
                        <v-dialog v-model="dialog" activator="parent" width="auto">
                            <v-card class="pa-4" rounded="xl" max-width="600">
                                <v-img src="@/assets/images/popup.png" />
                                <h2 class="pa-2 text-h4 font-weight-bold">
                                    Поможем откликнуться и сопроводим на всех
                                    этапах
                                </h2>
                                <p class="pa-2 text-h6 mb-4">
                                    71% наших клиентов находят работу за 3
                                    месяца. Среднее время поиска - 57 дней
                                </p>
                                <v-btn height="60" href="https://yourcodereview.com" color="black" size="large" rounded="xl"
                                    block>
                                    Узнать подробнее
                                </v-btn>
                                <v-btn class="close-popup" size="small" icon="mdi-close" @click="dialog = false" />
                            </v-card>
                        </v-dialog>
                    </v-btn>
                    <v-btn v-if="auth.isLoggedIn.value" block color="black" size="large" :href="currentVacancy.url">
                        Отклик
                    </v-btn>
                    <v-btn v-else :to="{ name: 'Login' }" color="black" size="large" rounded="lg" block>
                        Отклик
                    </v-btn>
                </v-card>
            </v-col>
            <v-col cols="12" sm="10">
                <v-card class="lime-banner pa-6" rounded="xl">
                    <h2 class="pa-2 text-h4 font-weight-bold">
                        Поможем найти работу за 3 месяца
                    </h2>
                    <p class="pa-2 text-h6 mb-4">
                        71% наших клиентов находят работу за 3 месяца. Среднее
                        время поиска - 57 дней
                    </p>
                    <v-btn color="black" rounded="xl" size="x-large" href="https://yourcodereview.com/">Узнать
                        подробнее</v-btn>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>
  
<style scoped>
.close-popup {
    position: absolute;
    top: 25px;
    right: 25px;
}

.card-btn__purple {
    color: white;
    background-image: var(--purple-gradient);
}

.blue-banner {
    color: white;
    background-image: var(--blue-gradient);
    cursor: pointer;
}

.page-nav {
    border-radius: 50px;
    position: sticky;
    top: 90px;
    z-index: 1006;
}

.lime-banner {
    background-image: var(--lime-gradient);
}
</style>
  
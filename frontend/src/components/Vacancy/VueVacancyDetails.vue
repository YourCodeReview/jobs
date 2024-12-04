<script setup>
import { ref } from 'vue'
import { useFirebase } from '@/hooks/useFirebase'
import { generateTargetUrl } from '@/components/utils/utils'
import { useJobsStore } from '@/store/jobs'

import UiCard from '@/components/_ui/uiCard.vue'
import UiAuthDialog from '../_ui/uiAuthDialog.vue'

const props = defineProps({
  data: Object
})

const store = useJobsStore()
const auth = useFirebase()
const dialog = ref(false)

const authDialog = ref(false)
</script>

<template>
  <div v-if="props.data" class="position-relative">
    <v-row class="page-nav justify-center">
      <v-col cols="12" class="d-flex py-1">
        <v-btn icon="mdi-arrow-left" size="small" @click="$router.back()" />
      </v-col>
    </v-row>
    <v-row class="justify-center">
      <v-col cols="12" lg="10" sm="12">
        <ui-card :item="props.data" size="lg" />
      </v-col>
    </v-row>
    <v-row class="justify-center">
      <v-col cols="12" lg="7" sm="8" class="card-info">
        <v-card v-if="props.data.salary" class="pa-2" rounded="xl">
          <span class="text-h5 font-weight-bold px-2">{{ props.data.salary }}</span>
        </v-card>
        <v-hover v-slot="{ isHovering, props }">
          <v-card
            v-bind="props"
            class="orange-banner mt-2 pa-2"
            rounded="xl"
            :elevation="isHovering ? 10 : 1"
            :href="'https://yourcodereview.com/' + generateTargetUrl('button_2')"
          >
            <v-card-title class="d-flex align-center font-weight-bold">
              Одни отĸазы и не зовут на собеседования?
              <v-icon class="ml-auto" color="white" icon="mdi-arrow-right" />
            </v-card-title>
            <v-card-text> Поможем тебе получить оффер на нашем ĸарьерном треĸе </v-card-text>
          </v-card>
        </v-hover>
        <v-card v-if="props.data.description" class="mt-2 pa-6" rounded="xl">
          <div class="description" v-html="props.data.description" />
        </v-card>
      </v-col>
      <v-col cols="12" lg="3" sm="4">
        <v-card class="pa-4 d-flex flex-column" rounded="xl">
          <v-card-title class="pa-0 pb-1 font-weight-bold">Отклик</v-card-title>
          <v-btn block size="large" class="card-btn__purple mb-2" rounded="lg">
            Получить оффер
            <v-dialog v-model="dialog" activator="parent" width="auto">
              <v-card class="pa-4" rounded="xl" max-width="600">
                <v-img src="/images/popup_2.png" />
                <h2 class="pa-2 text-h4 font-weight-bold">
                  Поможем тебе найти работу, с оплатой за результат.
                </h2>
                <p class="pa-2 text-h6 mb-4">
                  Средняя зарплата ребят, ĸоторых мы трудоустраиваем — 109.000 руб. Средняя время
                  трудоустройства 76 дней
                </p>
                <v-btn
                  height="60"
                  :href="'https://yourcodereview.com/' + generateTargetUrl('button_3')"
                  color="black"
                  size="large"
                  rounded="xl"
                  block
                  target="_blank"
                >
                  Получить помощь с трудоустройством.
                </v-btn>
                <v-btn class="close-popup" size="small" icon="mdi-close" @click="dialog = false" />
              </v-card>
            </v-dialog>
          </v-btn>
          <v-btn
            v-if="store.isAuth"
            block
            color="black"
            size="large"
            :href="props.data.url"
            target="_blank"
          >
            Откликнуться
          </v-btn>
          <v-btn v-else color="black" size="large" rounded="lg" block>
            Откликнуться
            <v-dialog v-model="authDialog" activator="parent" width="auto">
              <UiAuthDialog @success="authDialog = false" closable @close="authDialog = false" />
            </v-dialog>
          </v-btn>
        </v-card>
      </v-col>
      <v-col cols="12" lg="10" sm="12">
        <v-card class="orange-banner pa-6" rounded="xl">
          <h2 class="pa-2 text-h4 font-weight-bold">Хочешь попасть в эту ĸомпанию?</h2>
          <p class="pa-2 text-h6 mb-4">
            Помогаем разработчиĸам найти работу за 76 дней. С Зарплатой на 30-40% выше рыночной. С
            оплатой за результат.
          </p>
          <v-btn
            color="black"
            rounded="xl"
            size="x-large"
            :href="'https://yourcodereview.com/' + generateTargetUrl('button_4')"
            >Узнать подробнее.</v-btn
          >
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<style>
.card-info {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.close-popup {
  position: absolute;
  top: 25px;
  right: 25px;
}

.card-btn__purple {
  color: white;
  background-image: var(--purple-reverse-gradient);
}

.blue-banner {
  cursor: pointer;

  color: white;
  background-image: var(--blue-gradient);
}

.orange-banner {
  cursor: pointer;

  color: white;
  background-image: var(--orange-gradient);
}

.page-nav {
  position: sticky;
  z-index: 1006;
  top: 100px;

  border-radius: 50px;
}

.lime-banner {
  background-image: var(--lime-gradient);
}

.description {
  display: flex;
  flex-direction: column;

  gap: 16px;
}

.description ul,
.description ol {
  padding-left: 16px;
}
</style>

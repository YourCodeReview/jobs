<template>
  <div class="background">
    <div class="container">
      <h1 class="w-75 mb-4 px-2 text-white text-h4">Разместить вакансию</h1>
      <h1 class="mb-4 px-2 text-white text-h6">
        Размещать вакансии здесь можно бесплатно. Просто заполните форму ниже.
      </h1>
      <form @submit.prevent="onSubmit">
        <v-card class="pa-8 mb-4" rounded="xl" elevation="8">
          <template v-for="(field, fieldName) in formFields" :key="fieldName">
            <v-text-field
              v-if="field.type === 'text'"
              :label="field.label"
              v-model="state[fieldName]"
              :rules="getValidationRules(fieldName)"
              clearable
              variant="solo"
            />
            <v-text-field
              v-else-if="field.type === 'email'"
              :label="field.label"
              v-model="state[fieldName]"
              type="email"
              :rules="getValidationRules(fieldName)"
              clearable
              variant="solo"
            />
            <v-select
              v-else-if="field.type === 'select'"
              v-model="state[fieldName]"
              :items="field.items"
              :label="field.label"
              :rules="getValidationRules(fieldName)"
              clearable
              variant="solo"
            />
            <template v-else-if="fieldName === 'salary'">
              <v-row>
                <v-col cols="12" sm="3" v-for="(item, itemName) in field" :key="itemName">
                  <v-checkbox
                    v-if="itemName === 'gross'"
                    v-model="state.salary.gross"
                    label="До вычета налогов"
                  ></v-checkbox>
                  <v-text-field
                    v-else-if="itemName === 'currency'"
                    v-model="state.salary[itemName]"
                    label="Валюта"
                    :rules="getValidationRules('salary.' + itemName)"
                    clearable
                    variant="solo"
                  />
                  <v-text-field
                    v-else-if="itemName === 'from'"
                    v-model="state.salary[itemName]"
                    label="Зарплата от"
                    :rules="getValidationRules('salary.' + itemName)"
                    clearable
                    variant="solo"
                  />
                  <v-text-field
                    v-else-if="itemName === 'to'"
                    v-model="state.salary[itemName]"
                    label="До"
                    :rules="getValidationRules('salary.' + itemName)"
                    clearable
                    variant="solo"
                  />
                </v-col>
              </v-row>
            </template>
          </template>
          <the-tiptap v-model="state.description" :rules="getValidationRules('description')" />
          <v-text-field
            v-model="state.nameFrom"
            label="Ваше имя"
            :rules="getValidationRules('nameFrom')"
            clearable
            variant="solo"
          />
          <v-text-field
            v-model="state.email"
            label="Email"
            :rules="getValidationRules('email')"
            clearable
            variant="solo"
          />
          <v-btn block color="purple" type="submit">Отправить</v-btn>
        </v-card>
      </form>
    </div>
    <v-btn class="btn__close" icon="mdi-close" @click="router.back()"></v-btn>
  </div>
</template>
<script setup>
import TheTiptap from '@/components/TheTiptap.vue'
import { reactive } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const formFields = {
  name: {
    type: 'text',
    label: 'Должность'
  },
  employer: {
    type: 'text',
    label: 'Компания'
  },
  area: {
    type: 'text',
    label: 'Город'
  },
  salary: {
    from: null,
    to: null,
    currency: null,
    gross: false
  },
  employment: {
    type: 'select',
    label: 'Занятость',
    items: ['Полная занятость', 'Частичная занятость', 'Стажировка', 'Проектная работа']
  },
  schedule: {
    type: 'select',
    label: 'Формат работы',
    items: ['Удаленный', 'Офис', 'Гибрид']
  },
  specialty: {
    type: 'select',
    label: 'Специализация',
    items: ['Python', 'Java', 'JavaScript', 'Data Science', 'QA', 'C#']
  }
}

const state = reactive({
  name: '',
  employer: '',
  area: '',
  email: '',
  nameFrom: '',
  salary: {
    from: null,
    to: null,
    currency: null,
    gross: false
  },
  specialty: '',
  employment: 'Полная занятость',
  schedule: 'Офис',
  description: '<p>Описание вакансии!</p>'
})

const validations = {
  name: [(v) => !!v || 'Поле должно быть заполнено'],
  employer: [(v) => !!v || 'Поле должно быть заполнено'],
  area: [(v) => !!v || 'Поле должно быть заполнено'],
  'salary.currency': [(v) => !!v || 'Поле должно быть заполнено'],
  'salary.from': [(v) => !!v || 'Поле должно быть заполнено'],
  'salary.to': [(v) => !!v || 'Поле должно быть заполнено'],
  description: [(v) => !!v || 'Поле должно быть заполнено'],
  nameFrom: [(v) => !!v || 'Поле должно быть заполнено'],
  email: [
    (v) => !!v || 'Поле должно быть заполнено',
    (v) => /.+@.+..+/.test(v) || 'Введите действительный адрес электронной почты'
  ]
}

const getValidationRules = (field) => {
  return validations[field] || []
}

const onSubmit = () => {
  console.log(state)
}
</script>

<style scoped>
.container {
  max-width: 900px;
}

.background {
  position: relative;

  background-image: var(--purple-gradient);
}

.btn__close {
  position: absolute;
  top: 25px;
  right: 25px;
}
</style>

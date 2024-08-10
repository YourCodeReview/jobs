<script setup>
import { useTranslation } from '@/hooks/useTranslation'
import { computed, reactive, ref, watchEffect } from 'vue'
import { useRouter } from 'vue-router'
import uiLanguageButton from '@/components/_ui/uiLanguageButton.vue'

import NewVacancyDescription from '@/components/NewVacancy/VueNewVacancyDescription.vue'

const { t, locale } = useTranslation()

const formFields = ref({})

const loadFormFields = async (locale) => {
  if (locale.value === 'en') {
    formFields.value = await import('@/data/new-vacancy-fields.en.json')
  } else {
    formFields.value = await import('@/data/new-vacancy-fields.ru.json')
  }
}

const employmentDefault = computed(() => t('newVacancyPage.default.employment'))
const scheduleDefault = computed(() => t('newVacancyPage.default.schedule'))
const descriptionDefault = computed(() => t('newVacancyPage.default.description'))

watchEffect(() => {
  loadFormFields(locale)
})

const router = useRouter()

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
  employment: employmentDefault,
  schedule: scheduleDefault,
  description: descriptionDefault
})

const validations = {
  name: [(v) => !!v || t('newVacancyPage.errorMessage')],
  employer: [(v) => !!v || t('newVacancyPage.errorMessage')],
  area: [(v) => !!v || t('newVacancyPage.errorMessage')],
  'salary.currency': [(v) => !!v || t('newVacancyPage.errorMessage')],
  'salary.from': [(v) => !!v || t('newVacancyPage.errorMessage')],
  'salary.to': [(v) => !!v || t('newVacancyPage.errorMessage')],
  description: [(v) => !!v || t('newVacancyPage.errorMessage')],
  nameFrom: [(v) => !!v || t('newVacancyPage.errorMessage')],
  email: [
    (v) => !!v || t('newVacancyPage.errorMessage'),
    (v) => /.+@.+..+/.test(v) || t('newVacancyPage.emailErrorMessage')
  ]
}

const getValidationRules = (field) => {
  return validations[field] || []
}

const onSubmit = () => {
  console.log(state)
}
</script>

<template>
  <div class="container">
    <h1 class="w-75 mb-4 px-2 text-white text-h4">{{ t('newVacancyPage.title') }}</h1>
    <h1 class="mb-4 px-2 text-white text-h6">
      {{ t('newVacancyPage.subtitle') }}
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
                  :label="t('newVacancyPage.beforeTaxes')"
                ></v-checkbox>
                <v-text-field
                  v-else-if="itemName === 'currency'"
                  v-model="state.salary[itemName]"
                  :label="t('newVacancyPage.currency')"
                  :rules="getValidationRules('salary.' + itemName)"
                  clearable
                  variant="solo"
                />
                <v-text-field
                  v-else-if="itemName === 'from'"
                  v-model="state.salary[itemName]"
                  :label="t('newVacancyPage.salaryFrom')"
                  :rules="getValidationRules('salary.' + itemName)"
                  clearable
                  variant="solo"
                />
                <v-text-field
                  v-else-if="itemName === 'to'"
                  v-model="state.salary[itemName]"
                  :label="t('newVacancyPage.salaryUpTo')"
                  :rules="getValidationRules('salary.' + itemName)"
                  clearable
                  variant="solo"
                />
              </v-col>
            </v-row>
          </template>
        </template>
        <new-vacancy-description
          v-model="state.description"
          :rules="getValidationRules('description')"
        />
        <v-text-field
          v-model="state.nameFrom"
          :label="t('newVacancyPage.name')"
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
        <v-btn block color="purple" type="submit">{{ t('newVacancyPage.submit') }}</v-btn>
      </v-card>
    </form>
    <v-btn class="btn__close" icon="mdi-close" @click="router.back()"></v-btn>
    <ui-language-button class="btn__language" />
  </div>
</template>

<style scoped>
.background {
  position: relative;

  background-image: var(--purple-gradient);
}

.container {
  max-width: 900px;
}

.btn__close {
  position: absolute;
  top: 25px;
  right: 25px;
}
.btn__language {
  position: absolute;
  top: 0;
  left: 0;
  color: #fff;
}
</style>

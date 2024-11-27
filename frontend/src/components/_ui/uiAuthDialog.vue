<script setup>
import { computed, onBeforeUnmount, onMounted } from 'vue'
import svgClose from '@/components/_icons/svgClose.vue'
import SvgTelegram from '../_icons/svgTelegram.vue'
import SvgArrow from '../_icons/svgArrow.vue'
import { useGetUuid, useCheckAuth } from '@/api/requests'

const props = defineProps({
  modelValue: Boolean
})

const dialog = computed({
  get: () => props.modelValue,
  set: (value) => emits('update:modelValue', value)
})

const emits = defineEmits(['update:modelValue'])

const { data: uuid, execute: getUuid } = useGetUuid()
const { data: authToken, execute: checkAuth } = useCheckAuth()

let authInterval = null

const onAuth = async () => {
  window.open(`https://t.me/ITjobofferbot?start=uuid_${uuid.value}`, '_blank')

  if (authInterval) return

  authInterval = setInterval(async () => {
    await checkAuth(uuid.value)
    if (authToken.value) {
      clearInterval(authInterval)
      authInterval = null
    }
  }, 1000)
}

onMounted(async () => {
  await getUuid()
})

onBeforeUnmount(() => {
  clearInterval(authInterval)
})
</script>

<template>
  <v-dialog v-model="dialog" width="320" class="dialog">
    <v-card class="banner">
      <div class="info">
        <h3>
          Авторизуйтесь <br />
          через бота в <br />
          Telegram
        </h3>
        <p>
          <span>получите доступ к вакансиям</span> и полезным материалам, которые ускорят ваше
          трудоустройство в 5 раз
        </p>
        <SvgArrow />
        <button class="close" @click="dialog = false">
          <svgClose />
        </button>
        <button class="btn" @click="onAuth">
          <div>
            <SvgTelegram />
            <span>Авторизоваться</span>
          </div>
        </button>
      </div>
    </v-card>
  </v-dialog>
</template>

<style scoped>
.dialog {
  --v-theme-on-surface: 0, 0, 0, 0.749;
}

.dialog::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.75);
  backdrop-filter: blur(4px);
}

.v-overlay__scrim {
  background-color: rgba(0, 0, 0, 0) !important;
}

.banner {
  flex-direction: row !important;
  border-radius: 16px !important;
}

.info {
  position: relative;
  padding: 48px 38px;
  width: 100%;
  height: 416px;

  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
}

.info p {
  font-size: 16px;
  font-weight: 400;
  line-height: 18.75px;
  text-align: center;
}

.info p span {
  font-weight: 600;
}

.info h3 {
  font-size: 24px;
  font-weight: 700;
  line-height: 28.13px;
  text-align: center;

  color: #0088cc;
}

.btn {
  width: 240px;
  padding: 10px 40px 10px 33px;

  border-radius: 8px;
  background-color: #0088cc;
  color: #ffffff;

  text-align: center;

  font-family: 'Wix Madefor Display';
  font-size: 16px;
  font-weight: 700;
  line-height: 18.75px;

  div {
    display: flex;
    align-items: center;
    gap: 14px;
  }
}

.close {
  position: absolute;
  top: 12px;
  right: 12px;
}
</style>

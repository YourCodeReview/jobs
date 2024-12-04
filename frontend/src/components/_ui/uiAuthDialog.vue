<script setup>
import { onBeforeUnmount, onMounted } from 'vue'
import svgClose from '@/components/_icons/svgClose.vue'
import SvgTelegram from '../_icons/svgTelegram.vue'
import SvgArrow from '../_icons/svgArrow.vue'
import { useGetUuid, useCheckAuth } from '@/api/requests'
import { useJobsStore } from '@/store/jobs'

const jobsStore = useJobsStore()

defineProps({
  closable: Boolean
})
const emits = defineEmits(['success', 'close'])

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

      localStorage.setItem('token', authToken.value.access_token)
      jobsStore.isAuth = true

      emits('success')
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
      <button v-if="closable" class="close" @click="emits('close')">
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
</template>

<style scoped>
.banner {
  width: 320px;
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

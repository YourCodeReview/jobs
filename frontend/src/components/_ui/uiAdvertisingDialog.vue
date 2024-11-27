<script setup>
import { computed } from 'vue'
import svgClose from '@/components/_icons/svgClose.vue'

const props = defineProps({
  modelValue: Boolean
})

const dialog = computed({
  get: () => props.modelValue,
  set: (value) => emits('update:modelValue', value)
})

const emits = defineEmits(['update:modelValue'])
</script>

<template>
  <v-dialog v-model="dialog" width="640" class="dialog">
    <v-card class="banner">
      <div class="img-wrapper">
        <img class="img" src="/images/popup-banner.jpeg" />
      </div>
      <div class="info">
        <p>из ЖДУНА в ДЖУНА</p>
        <h3>
          Путь от отклика <br />
          до оффера <br />
          <span>за 14 дней</span>
        </h3>
        <button class="close" @click="dialog = false">
          <svgClose />
        </button>
        <a
          class="btn"
          href="https://yourcodereview.com/ready2work?utm_source=jobs&utm_medium=popup&utm_campaign=1"
          target="_blank"
          >Узнать подробнее →</a
        >
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

.img {
  width: 280px;
  height: 100%;
  object-fit: cover;
  object-position: right;
}

.info {
  position: relative;
  padding: 40px;
  width: 100%;
}

.info p {
  margin-bottom: 38px;

  font-family: 'Wix Madefor Display';
  font-size: 14px;
  font-weight: 300;
  line-height: 16.41px;
  color: #525252;
}

.info h3 {
  margin-bottom: 52px;
}

.info h3,
.info h3 span {
  font-family: 'Wix Madefor Display';
  font-size: 32px;
  font-weight: 700;
  line-height: 37.5px;
}

.info h3 span {
  color: #c449ff;
}

.btn {
  display: block;
  width: 280px;
  padding: 15px 40px;
  border-radius: 8px;

  background-image: linear-gradient(90deg, #4490ff 0%, #be4dff 100%);
  color: #ffffff;

  text-align: center;

  font-family: 'Wix Madefor Display';
  font-size: 16px;
  font-weight: 700;
  line-height: 18.75px;
}

.close {
  position: absolute;
  top: 12px;
  right: 12px;
}

@media (width < 550px) {
  .banner {
    flex-direction: column !important;
  }

  .info {
    padding: 32px;
  }

  .info p {
    margin-bottom: 20px;
    text-align: center;
  }

  .info h3 {
    margin-bottom: 32px;
    text-align: center;
  }

  .img {
    width: 100%;
  }

  .img-wrapper {
    height: 270px;
  }

  .btn {
    width: 100%;
  }

  .close {
    top: 8px;
    right: 8px;
  }
}
</style>

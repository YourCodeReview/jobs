<script setup>
import { ref, onMounted } from 'vue'
import UiStackCard from './ui/uiStackCard.vue'
import svgLogo from '@/components/icons/svgLogo.vue'

const expand = ref(false)

const cards = [
  {
    id: 1,
    name: 'Python',
    type: 'python',
    color: 'indigo-darken-1'
  },
  {
    id: 2,
    name: 'Java',
    type: 'java',
    color: 'orange-darken-1',
    icon: 'SvgJavaScript'
  },
  {
    id: 3,
    name: 'JavaScript',
    type: 'javascript',
    color: 'yellow-darken-3'
  },
  {
    id: 4,
    name: 'Data Science',
    type: 'data-science',
    color: 'light-blue-accent-2'
  },
  {
    id: 5,
    name: 'QA',
    type: 'qa',
    color: 'deep-purple-accent-3'
  },
  {
    id: 6,
    name: 'C#',
    type: 'c-sharp',
    color: 'green-darken-1'
  }
]

onMounted(() => {
  expand.value = true
})
</script>

<template>
  <div class="welcome background">
    <header class="pt-1 pb-4">
      <div class="container px-4 py-6">
        <router-link :to="{ name: 'Home' }">
          <svg-logo />
        </router-link>
        <h1 class="text-sm-h2 text-center mt-auto font-weight-bold">
          Junior вакансии и стажировки
        </h1>
        <p class="text-sm-h4 text-center mt-8">
          Всё, что нужно, чтобы найти первую работу разработчиком
        </p>
      </div>
    </header>
    <div class="container pt-2 justify-center">
      <div class="grid-cards">
        <v-fade-transition v-for="item in cards" :key="item.id">
          <!-- <router-link :to="{ name: 'Jobs', query: { stack: item.type } }" v-show="expand"> -->
          <router-link :to="{ name: 'Jobs' }" v-show="expand">
            <ui-stack-card :item="item" />
          </router-link>
        </v-fade-transition>
      </div>
    </div>
  </div>
</template>

<style scoped>
.welcome {
  display: grid;

  min-height: 100vh;

  grid-template-rows: minmax(200px, 350px) 1fr;
}

.container {
  display: flex;
  flex-direction: column;

  height: 100%;
}
.grid-cards {
  display: grid;

  grid-template-columns: repeat(auto-fill, minmax(330px, 1fr));
  grid-auto-flow: dense;
  gap: 12px;
}

@media screen and (max-width: 550px) {
  .grid-cards {
    grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
  }
}

.background {
  background-image: var(--purple-gradient);
}
.fade-transition-enter-active {
  transition-delay: 0.5s;
}
</style>

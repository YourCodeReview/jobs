// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/DefaultLayout.vue'),
    children: [
      {
        name: 'Home',
        path: '',
        component: () => import('@/views/HomeView.vue'),
      },
      {
        name: 'Login',
        path: '/login',
        component: () => import('@/views/LoginView.vue'),
      },
    ]
  },
  {
    path: '/jobs',
    component: () => import('@/layouts/JobsLayout.vue'),
    children: [
      {
        name: 'Jobs',
        path: '',
        component: () => import('@/views/JobsView.vue'),
      },
      {
        name: 'Vacancy',
        path: ':id',
        component: () => import('@/views/VacancyView.vue'),
        props: true
      }
    ]
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return from.name !== 'Vacancy' ? { top: 0 } : savedPosition
  },
})

export default router

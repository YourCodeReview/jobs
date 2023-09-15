// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/:catchAll(.*)',
    redirect: '404'
  },
  {
    path: '/404',
    component: () => import('@/layouts/JobsLayout.vue'),
    children: [
      {
        name: 'NotFound',
        path: '',
        component: () => import('@/views/NotFoundView.vue')
      }
    ]
  },
  {
    path: '/',
    component: () => import('@/layouts/DefaultLayout.vue'),
    children: [
      {
        name: 'Home',
        path: '',
        component: () => import('@/views/HomeView.vue')
      },
      {
        name: 'Login',
        path: '/login',
        component: () => import('@/views/LoginView.vue')
      }
    ]
  },
  {
    path: '/jobs',
    component: () => import('@/layouts/JobsLayout.vue'),
    children: [
      {
        name: 'Jobs',
        path: '',
        component: () => import('@/views/JobsView.vue')
      },
      {
        name: 'Vacancy',
        path: ':id',
        component: () => import('@/views/VacancyView.vue'),
        props: true
      }
    ]
  },
  {
    path: '/add',
    component: () => import('@/layouts/DefaultLayout.vue'),
    children: [
      {
        name: 'NewVacancy',
        path: '',
        component: () => import('@/views/NewVacancyView.vue')
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return from.name !== 'Vacancy' ? { top: 0 } : savedPosition
  }
})

export default router

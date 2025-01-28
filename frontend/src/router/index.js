import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory('/MiniAppRazvivahka/'),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfileView.vue')
    },
    {
      path: '/tasks',
      name: 'tasks',
      component: () => import('../views/TasksView.vue')
    }
  ]
})

// Middleware для проверки Telegram WebApp
router.beforeEach((to, from, next) => {
  const telegram = window.Telegram?.WebApp
  if (telegram) {
    // Если приложение запущено в Telegram
    telegram.ready()
    telegram.expand()
  }
  next()
})

export default router

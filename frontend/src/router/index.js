import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/tasks',
      name: 'tasks',
      component: () => import('../views/TasksView.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfileView.vue')
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

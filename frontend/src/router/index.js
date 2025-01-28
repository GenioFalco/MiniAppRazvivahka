import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHashHistory(),
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

// Middleware для проверки окружения
router.beforeEach((to, from, next) => {
  const telegram = window.Telegram?.WebApp
  
  // Если приложение запущено в Telegram
  if (telegram) {
    telegram.ready()
    telegram.expand()
  } else {
    console.log('Running in browser mode')
  }
  
  // Всегда разрешаем навигацию
  next()
})

export default router

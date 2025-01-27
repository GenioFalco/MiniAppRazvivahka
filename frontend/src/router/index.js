import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: () => import('../views/Tasks.vue')
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/Profile.vue')
  },
  {
    path: '/category/:id',
    name: 'Category',
    component: () => import('../views/Category.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

// Middleware для проверки авторизации Telegram
router.beforeEach((to, from, next) => {
  const telegram = window.Telegram?.WebApp;
  if (telegram) {
    // Если приложение запущено в Telegram, передаем данные пользователя
    const user = telegram.initDataUnsafe?.user;
    if (user) {
      // Здесь можно добавить логику проверки пользователя
      next();
    } else {
      // Если нет данных пользователя, можно перенаправить на страницу авторизации
      next('/auth');
    }
  } else {
    // Если приложение запущено вне Telegram, разрешаем доступ (для разработки)
    next();
  }
})

export default router 
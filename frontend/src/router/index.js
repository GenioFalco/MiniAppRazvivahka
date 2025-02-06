import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ProfileView from '@/views/ProfileView.vue'
import TasksView from '@/views/TasksView.vue'
import PhotoAlbumView from '@/views/PhotoAlbumView.vue'

const router = createRouter({
  history: createWebHashHistory('/'),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/tasks/:category?',
      name: 'tasks',
      component: TasksView
    },
    {
      path: '/photoalbum',
      name: 'photoalbum',
      component: PhotoAlbumView
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

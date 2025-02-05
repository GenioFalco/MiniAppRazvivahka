import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ProfileView from '@/views/ProfileView.vue'
import TasksView from '@/views/TasksView.vue'
import PhotoAlbumView from '@/views/PhotoAlbumView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
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
    
    // Убираем использование BackButton, так как он не поддерживается
    if (to.name === 'profile' || to.name === 'photoalbum') {
      // Используем MainButton вместо BackButton
      telegram.MainButton.setText('Назад')
      telegram.MainButton.show()
      telegram.MainButton.onClick(() => {
        router.push('/')
      })
    } else {
      telegram.MainButton.hide()
    }
  } else {
    console.log('Running in browser mode')
  }
  
  // Всегда разрешаем навигацию
  next()
})

export default router

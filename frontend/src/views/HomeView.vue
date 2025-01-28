<template>
  <div class="main-menu">
    <!-- Верхняя часть меню с иконками профиля, подписки и фотоальбома -->
    <div class="top-menu">
      <div class="menu-card" @click="handleClick('profile')">
        <img src="@/assets/profile.png" alt="Профиль" class="menu-icon" />
        <span>Профиль</span>
      </div>
      <div class="menu-card" @click="handleClick('subscription')">
        <img src="@/assets/subscription.png" alt="Подписка" class="menu-icon" />
        <span>Подписка</span>
      </div>
      <div class="menu-card" @click="handleClick('photoalbum')">
        <img src="@/assets/photoalbum.png" alt="Фотоальбом" class="menu-icon" />
        <span>Фотоальбом</span>
      </div>
    </div>

    <!-- Список категорий -->
    <div class="categories">
      <div class="category-item" @click="handleClick('creativity')">
        <img src="@/assets/creativity.png" alt="Творчество" class="category-icon" />
        <span>Творчество</span>
      </div>
      <div class="category-item" @click="handleClick('daily')">
        <img src="@/assets/daily.png" alt="Задания на день" class="category-icon" />
        <span>Задания на день</span>
      </div>
      <div class="category-item" @click="handleClick('riddles')">
        <img src="@/assets/riddles.png" alt="Загадки" class="category-icon" />
        <span>Загадки</span>
      </div>
      <div class="category-item" @click="handleClick('tonguetwisters')">
        <img src="@/assets/tonguetwisters.png" alt="Скороговорки" class="category-icon" />
        <span>Скороговорки</span>
      </div>
      <div class="category-item" @click="handleClick('rebus')">
        <img src="@/assets/rebus.png" alt="Ребусы" class="category-icon" />
        <span>Ребусы</span>
      </div>
      <div class="category-item" @click="handleClick('articulation')">
        <img src="@/assets/articulation.png" alt="Артикулярная гимнастика" class="category-icon" />
        <span>Артикулярная гимнастика</span>
      </div>
      <div class="category-item" @click="handleClick('neuro')">
        <img src="@/assets/neuro.png" alt="Нейрогимнастика" class="category-icon" />
        <span>Нейрогимнастика</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const handleClick = async (category) => {
  try {
    // Прямой вызов вибрации сразу при нажатии
    if (window.Telegram?.WebApp) {
      // Используем все доступные методы вибрации Telegram
      window.Telegram.WebApp.HapticFeedback.impactOccurred('heavy')
      window.Telegram.WebApp.HapticFeedback.notificationOccurred('success')
      window.Telegram.WebApp.HapticFeedback.selectionChanged()
    }

    // Стандартная вибрация как запасной вариант
    if ('vibrate' in navigator) {
      navigator.vibrate([50, 50, 50])
    }
    
    // Эффект нажатия
    const elements = document.querySelectorAll('.category-item, .menu-card')
    elements.forEach(el => {
      if (el.contains(event.target)) {
        el.classList.add('press-down')
        setTimeout(() => el.classList.remove('press-down'), 150)
      }
    })

    setTimeout(() => {
      router.push(`/tasks?category=${category}`)
    }, 150)
  } catch (error) {
    console.error('Error in handleClick:', error)
    router.push(`/tasks?category=${category}`)
  }
}

// Функция для воспроизведения звука
const playClickSound = () => {
  const audio = new Audio('data:audio/wav;base64,UklGRl9vT19XQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YU')
  audio.volume = 0.2 // Тихий звук
  audio.play().catch(() => {
    // Игнорируем ошибку, если браузер блокирует автовоспроизведение
  })
}
</script>

<style scoped>
.main-menu {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: linear-gradient(180deg, #4a90e2, #003f7f);
  padding: 20px;
  min-height: 100vh;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
  margin: 0;
  color: white;
  font-family: 'Arial', sans-serif;
}

.top-menu {
  display: flex;
  gap: 20px;
  margin-bottom: 30px;
}

.menu-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s ease;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
}

.menu-icon {
  width: 60px;
  height: 60px;
  margin-bottom: 5px;
}

.categories {
  display: grid;
  grid-template-columns: 1fr;
  gap: 15px;
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
}

.category-item {
  display: flex;
  align-items: center;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 10px;
  gap: 10px;
  cursor: pointer;
  position: relative;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: all 0.2s ease;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
}

/* Эффект при наведении только для ПК */
@media (hover: hover) {
  .category-item:hover {
    transform: scale(1.05);
    background: rgba(255, 255, 255, 0.2);
  }
  
  .menu-card:hover {
    transform: scale(1.05);
  }
}

/* Эффект вдавливания только для мобильных */
@media (hover: none) {
  .category-item:active {
    transform: scale(0.95);
    box-shadow: 0 1px 2px rgba(0,0,0,0.15);
  }
  
  .menu-card:active {
    transform: scale(0.95);
  }
  
  .press-down {
    animation: pressDownSimple 0.15s ease-out forwards;
  }
}

.category-icon {
  width: 40px;
  height: 40px;
}

/* Анимация вдавливания для мобильных */
@keyframes pressDownSimple {
  to { 
    transform: scale(0.95);
    box-shadow: 0 1px 2px rgba(0,0,0,0.15);
  }
}

/* Отключаем анимации для устройств с отключенной анимацией */
@media (prefers-reduced-motion: reduce) {
  .category-item,
  .menu-card {
    transition: none;
  }
  .press-down {
    animation: none;
  }
}
</style>

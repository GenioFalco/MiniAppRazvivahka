<template>
  <div class="main-menu">
    <!-- Верхнее меню -->
    <div class="top-menu">
      <!-- Профиль слева -->
      <div class="profile-card" @click="handleClick('profile')">
        <img src="@/assets/profile.png" alt="Профиль" class="menu-icon" />
        <span>Профиль</span>
      </div>
      
      <!-- Сетка 2x2 справа -->
      <div class="menu-grid">
        <div class="menu-card" @click="handleClick('subscription')">
          <img src="@/assets/subscription.png" alt="Подписка" class="menu-icon" />
          <span>Подписка</span>
        </div>
        <div class="menu-card" @click="handleClick('photoalbum')">
          <img src="@/assets/photoalbum.png" alt="Фотоальбом" class="menu-icon" />
          <span>Фотоальбом</span>
        </div>
        <div class="menu-card" @click="handleClick('shop')">
          <img src="@/assets/shop.png" alt="Магазин" class="menu-icon" />
          <span>Магазин</span>
        </div>
        <div class="menu-card" @click="handleClick('link')">
          <img src="@/assets/link.png" alt="Ссылки" class="menu-icon" />
          <span>Ссылки</span>
        </div>
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
    // Простая вибрация через Web Vibration API
    if ('vibrate' in navigator) {
      navigator.vibrate(100)
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
  padding: 15px;
  min-height: 100vh;
  width: 100%;
  box-sizing: border-box;
  margin: 0;
  color: white;
  font-family: 'Arial', sans-serif;
}

.top-menu {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
  width: 100%;
  max-width: 350px;
}

/* Профиль слева */
.profile-card {
  width: 90px;
  height: 190px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 10px;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: all 0.2s ease;
}

/* Сетка 2x2 справа */
.menu-grid {
  flex: 1;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(2, 1fr);
  gap: 10px;
  height: 190px;
}

.menu-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 10px;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: all 0.2s ease;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
}

.categories {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
  width: 100%;
  max-width: 350px;
  margin: 0 auto;
}

.category-item {
  display: flex;
  align-items: center;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 10px 15px;
  gap: 15px;
  cursor: pointer;
  position: relative;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: all 0.2s ease;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
  height: 45px;
}

/* Размеры иконок */
.menu-icon {
  width: 35px;
  height: 35px;
  margin-bottom: 5px;
}

.profile-card .menu-icon {
  width: 50px;
  height: 50px;
  margin-bottom: 8px;
}

.category-icon {
  width: 35px;
  height: 35px;
  flex-shrink: 0;
}

/* Стили для текста */
span {
  font-size: 13px;
  line-height: 1.2;
  white-space: nowrap;
}

/* Медиа-запросы для адаптивности */
@media (min-width: 768px) {
  .main-menu {
    padding: 20px;
  }

  .top-menu,
  .categories {
    max-width: 400px;
  }

  .category-item {
    height: 50px;
  }

  span {
    font-size: 14px;
  }
}

/* Эффекты при наведении и нажатии */
@media (hover: hover) {
  .profile-card:hover,
  .menu-card:hover {
    transform: scale(1.05);
    background: rgba(255, 255, 255, 0.2);
  }
}

@media (hover: none) {
  .profile-card:active,
  .menu-card:active {
    transform: scale(0.95);
    box-shadow: 0 1px 2px rgba(0,0,0,0.15);
  }
}

/* Эффект при наведении только для ПК */
@media (hover: hover) {
  .category-item:hover {
    transform: scale(1.05);
    background: rgba(255, 255, 255, 0.2);
  }
}

/* Эффект вдавливания только для мобильных */
@media (hover: none) {
  .category-item:active {
    transform: scale(0.95);
    box-shadow: 0 1px 2px rgba(0,0,0,0.15);
  }
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

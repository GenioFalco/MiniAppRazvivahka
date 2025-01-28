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
    // Более сильная вибрация
    if (window.navigator && window.navigator.vibrate) {
      window.navigator.vibrate([100, 30, 100, 30, 100]) // Тройная вибрация
    }
    
    // Добавляем класс для анимации встряски
    const elements = document.querySelectorAll('.category-item, .menu-card')
    elements.forEach(el => {
      if (el.contains(event.target)) {
        el.classList.add('shake')
        setTimeout(() => el.classList.remove('shake'), 500)
      }
    })

    // Навигация с небольшой задержкой для анимации
    setTimeout(() => {
      router.push(`/tasks?category=${category}`)
    }, 300)
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
  -webkit-tap-highlight-color: transparent; /* Убираем стандартное выделение на iOS */
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
  transition: transform 0.2s ease, background 0.2s ease;
  -webkit-tap-highlight-color: transparent;
  position: relative;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transform: translateY(0);
  transition: all 0.2s ease;
}

/* Эффект при наведении (для ПК) */
@media (hover: hover) {
  .category-item:hover {
    transform: scale(1.02);
    background: rgba(255, 255, 255, 0.2);
  }
}

/* Эффект при нажатии (для всех устройств) */
.category-item:active {
  transform: scale(0.95);
  background: rgba(255, 255, 255, 0.3);
  transition: all 0.1s ease-in-out;
  box-shadow: 0 1px 2px rgba(0,0,0,0.2);
  transform: translateY(1px);
}

.menu-card:active {
  transform: scale(0.92);
  transition: all 0.1s ease-in-out;
}

.category-icon {
  width: 40px;
  height: 40px;
}

/* Улучшенная анимация нажатия */
@keyframes press {
  0% { transform: scale(1); }
  40% { transform: scale(0.94); }
  100% { transform: scale(1); }
}

.pressed {
  animation: press 0.3s cubic-bezier(.25,.46,.45,.94) both;
}

/* Анимация встряски */
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  10%, 30%, 50%, 70%, 90% { transform: translateX(-2px); }
  20%, 40%, 60%, 80% { transform: translateX(2px); }
}

.shake {
  animation: shake 0.4s cubic-bezier(.36,.07,.19,.97) both;
  transform: translate3d(0, 0, 0);
  backface-visibility: hidden;
  perspective: 1000px;
}

/* Добавляем подсветку при нажатии */
.category-item::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  border-radius: 10px;
  opacity: 0;
  transition: opacity 0.2s ease;
  background: radial-gradient(circle at center, rgba(255,255,255,0.2) 0%, transparent 70%);
  pointer-events: none;
}

.category-item:active::after {
  opacity: 1;
}
</style>

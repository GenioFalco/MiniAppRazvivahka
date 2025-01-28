<template>
  <div class="main-menu">
    <!-- Верхняя часть меню с профилем слева и сеткой 2x2 справа -->
    <div class="top-menu">
      <!-- Профиль на всю высоту слева -->
      <div class="menu-card" @click="handleClick('profile')">
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
  display: grid;
  grid-template-columns: 120px 1fr; /* Профиль слева, сетка справа */
  gap: 15px;
  margin-bottom: 30px;
  width: 100%;
  max-width: 375px; /* Уменьшаем максимальную ширину для более компактного вида */
}

.menu-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  cursor: pointer;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 10px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  transition: all 0.2s ease;
  -webkit-tap-highlight-color: transparent;
  user-select: none;
  height: 100%;
  aspect-ratio: 1; /* Делаем все карточки квадратными */
}

/* Специальный стиль для карточки профиля */
.menu-card:first-child {
  grid-row: span 2;
  height: 100%; /* Высота будет равна высоте сетки справа */
  aspect-ratio: auto; /* Отменяем квадратную форму для профиля */
}

/* Контейнер для сетки 2x2 */
.menu-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(2, 1fr);
  gap: 15px;
  height: 100%;
  aspect-ratio: 2/1; /* Соотношение сторон для сетки 2x2 */
}

.menu-icon {
  width: 40px; /* Уменьшаем размер иконок */
  height: 40px;
  margin-bottom: 5px;
}

/* Обновляем стили для профиля */
.menu-card:first-child .menu-icon {
  width: 60px; /* Немного уменьшаем иконку профиля */
  height: 60px;
  margin-bottom: 10px;
}

/* Добавляем стили для текста */
.menu-card span {
  font-size: 14px;
  line-height: 1.2;
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

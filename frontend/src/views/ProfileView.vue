<template>
  <!-- Основной контейнер профиля -->
  <div class="profile">
    <!-- Верхняя панель с именем пользователя и кнопкой настроек -->
    <header>
      <div class="header-content">
        <div class="user-info">
          <img :src="profileIcon" alt="Profile" class="profile-mini" />
          <span class="username">ТИМА#564</span>
        </div>
        <button class="settings-button">
          <img :src="gearIcon" alt="Settings" />
        </button>
      </div>
    </header>

    <!-- Верхняя панель статистики (монеты, ежедневные задания, трофеи) -->
    <div class="stats-bar">
      <div class="stat-item">
        <img :src="coinIcon" alt="Coins" />
        <span>1,555,000</span>
      </div>
      <div class="stat-item">
        <img :src="dailyIcon" alt="Daily" />
        <span>25</span>
      </div>
      <div class="stat-item">
        <img :src="trophyIcon" alt="Trophies" />
        <span>3</span>
      </div>
    </div>

    <!-- Индикатор прогресса уровня -->
    <div class="level-info">
      <span>Уровень 7</span>
      <div class="xp-bar">
        <div class="xp-progress" :style="{ width: xpProgress + '%' }"></div>
      </div>
      <span class="xp-text">XP {{ xp }}/100</span>
    </div>

    <!-- Контейнер с персонажем и кнопкой обмена -->
    <div class="character-container">
      <img :src="profileIcon" alt="Character" class="character-image" />
      <button class="exchange-button">ОБМЕНЯТЬ</button>
    </div>

    <!-- Нижняя панель с кнопками действий -->
    <div class="bottom-actions-container">
      <div class="bottom-actions">
        <button 
          v-for="(action, index) in actions" 
          :key="index" 
          class="action-button"
          :class="{ 'active': activeButtonIndex === index }"
          @click="setActiveButton(index)"
        >
          <img :src="action.icon" :alt="action.name" />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
// Импорт необходимых компонентов и изображений
import { ref } from "vue";
import gearIcon from '@/assets/gear-icon.png'
import coinIcon from '@/assets/coin-icon.png'
import dailyIcon from '@/assets/daily.png'
import trophyIcon from '@/assets/trophy-icon.png'
import profileIcon from '@/assets/profile.png'
import dailyIcon2 from '@/assets/daily.png'
import neuroIcon from '@/assets/neuro.png'
import creativityIcon from '@/assets/creativity.png'
import rebusIcon from '@/assets/rebus.png'
import riddlesIcon from '@/assets/riddles.png'
import tongueTwisterIcon from '@/assets/tonguetwisters.png'
import articulationIcon from '@/assets/articulation.png'

// Состояние для уровня и опыта
const level = ref(7);
const xp = ref(25);
const xpProgress = ref((xp.value / 100) * 100); // Вычисление процента прогресса

// Массив кнопок для нижней панели
const actions = ref([
  { name: "Ежедневные задания", icon: dailyIcon2 },
  { name: "Творчество", icon: creativityIcon },
  { name: "Ребусы", icon: rebusIcon },
  { name: "Загадки", icon: riddlesIcon },
  { name: "Скороговорки", icon: tongueTwisterIcon },
  { name: "Нейрогимнастика", icon: neuroIcon },
  { name: "Артикулярная гимнастика", icon: articulationIcon },
]);

// Состояние для активной кнопки
const activeButtonIndex = ref(0); // Первая кнопка активна по умолчанию

// Функция для изменения активной кнопки
function setActiveButton(index) {
  activeButtonIndex.value = index;
}

// Функция обмена (пока не реализована)
function exchange() {
  alert("Функция обмена не реализована!");
}
</script>

<style scoped>
/* Основной контейнер */
.profile {
  background: linear-gradient(180deg, #1e3a8a 0%, #1e40af 100%);
  min-height: 100vh;
  height: 100vh;
  color: white;
  padding: 0;
  display: flex;
  flex-direction: column;
  width: 100vw;
  max-width: 100vw;
  position: relative;
  overflow: hidden;
  margin: 0;
  left: 0;
  right: 0;
}

/* Стили для верхней панели */
header {
  background: rgba(0, 0, 0, 0.2);
  padding: clamp(0.5rem, 2vh, 1rem);
  flex-shrink: 0;
  width: 100%;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Стили для информации о пользователе */
.user-info {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.profile-mini {
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
}

.username {
  font-weight: bold;
  font-size: 1.2rem;
}

/* Стили для кнопки настроек */
.settings-button {
  background: none;
  border: none;
  padding: 0.5rem;
}

.settings-button img {
  width: 1.5rem;
  height: 1.5rem;
}

/* Стили для верхней панели статистики */
.stats-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(255, 255, 255, 0.1);
  padding: clamp(0.5rem, 2vh, 1rem);
  border-radius: 1rem;
  margin: clamp(0.5rem, 2vh, 1rem);
  flex-shrink: 0;
  width: calc(100% - clamp(2rem, 4vh, 4rem));
  margin-left: auto;
  margin-right: auto;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.stat-item img {
  width: 1.5rem;
  height: 1.5rem;
}

/* Стили для индикатора прогресса уровня */
.level-info {
  text-align: center;
  margin: clamp(0.5rem, 2vh, 1rem);
  padding: clamp(0.25rem, 1vh, 0.5rem);
  flex-shrink: 0;
  width: calc(100% - clamp(2rem, 4vh, 4rem));
  margin-left: auto;
  margin-right: auto;
}

.xp-bar {
  width: 100%;
  height: 0.5rem;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 1rem;
  margin: 0.5rem 0;
  overflow: hidden;
}

.xp-progress {
  height: 100%;
  background: #3b82f6;
  border-radius: 1rem;
  transition: width 0.3s ease;
}

/* Стили для контейнера с персонажем */
.character-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0;
  padding: 0;
  flex: 1;
  justify-content: center;
  width: 100%;
  margin: 0 auto;
  position: relative;
  z-index: 2;
  margin-top: -10vh;
}

.character-image {
  width: clamp(12rem, 40vh, 20rem);
  height: auto;
  object-fit: contain;
  position: relative;
  z-index: 2;
}

/* Стили для кнопки обмена */
.exchange-button {
  background: #3b82f6;
  color: white;
  border: none;
  padding: clamp(0.75rem, 2.5vh, 1.5rem) clamp(2rem, 5vh, 4rem);
  border-radius: 2rem;
  font-weight: bold;
  font-size: clamp(1.1rem, 2.5vh, 1.4rem);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
  position: relative;
  z-index: 2;
  margin-top: -10%;
  letter-spacing: 0.05em;
}

.exchange-button:active {
  transform: scale(0.98);
}

/* Стили для нижней панели с кнопками */
.bottom-actions-container {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: clamp(1rem, 3vh, 2rem);
  background: rgba(0, 0, 0, 0.2);
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  height: clamp(40vh, 55vh, 60vh);
  width: 100vw;
  margin: 0;
  z-index: 1;
}

/* Контейнер с кнопками внизу панели */
.bottom-actions {
  position: absolute;
  bottom: clamp(1rem, 3vh, 2rem);
  left: clamp(1rem, 3vh, 2rem);
  right: clamp(1rem, 3vh, 2rem);
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(255, 255, 255, 0.1);
  padding: clamp(0.5rem, 2vh, 1rem);
  border-radius: 1rem;
  z-index: 2;
}

/* Стили для кнопок действий */
.action-button {
  background: none;
  border: none;
  padding: clamp(0.25rem, 1vh, 0.5rem);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
  min-width: clamp(2rem, 6vh, 3rem);
  min-height: clamp(2rem, 6vh, 3rem);
  position: relative;
  z-index: 3;
  cursor: pointer;
}

/* Стили для активной кнопки */
.action-button.active {
  background: rgba(255, 255, 255, 0.2);
}

/* Индикатор активной кнопки (точка снизу) */
.action-button.active::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 50%;
  transform: translateX(-50%);
  width: 4px;
  height: 4px;
  background: #3b82f6;
  border-radius: 50%;
  z-index: 3;
}

/* Эффект при наведении на кнопку */
.action-button:hover {
  background: rgba(255, 255, 255, 0.1);
}

/* Размеры иконок в кнопках */
.action-button img {
  width: clamp(1rem, 3vh, 1.5rem);
  height: clamp(1rem, 3vh, 1.5rem);
  pointer-events: none;
}

@media (min-width: 768px) {
  .profile {
    width: 100vw;
    max-width: 100vw;
    margin: 0;
  }

  .bottom-actions-container {
    width: 100vw;
    margin: 0;
  }

  .character-container {
    margin-top: -8vh;
  }

  .character-image {
    width: clamp(16rem, 45vh, 24rem);
  }

  .exchange-button {
    padding: clamp(1rem, 3vh, 2rem) clamp(3rem, 6vh, 5rem);
    font-size: clamp(1.2rem, 3vh, 1.6rem);
  }
}

@media (min-width: 1200px) {
  .character-container {
    margin-top: -10vh;
  }

  .character-image {
    width: clamp(20rem, 50vh, 28rem);
  }

  .bottom-actions-container {
    height: clamp(45vh, 50vh, 55vh);
  }
}

@media (max-height: 600px) {
  .character-container {
    margin-top: -3vh;
  }

  .character-image {
    width: clamp(10rem, 35vh, 18rem);
  }

  .exchange-button {
    padding: clamp(0.5rem, 2vh, 1rem) clamp(1.5rem, 4vh, 3rem);
    font-size: clamp(1rem, 2vh, 1.2rem);
  }

  .bottom-actions-container {
    height: 50vh;
  }
}
</style>

<template>
  <div class="profile">
    <!-- Header -->
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

    <!-- Stats Bar -->
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

    <!-- Level Progress -->
    <div class="level-info">
      <span>Уровень 7</span>
      <div class="xp-bar">
        <div class="xp-progress" :style="{ width: xpProgress + '%' }"></div>
      </div>
      <span class="xp-text">XP {{ xp }}/100</span>
    </div>

    <!-- Character -->
    <div class="character-container">
      <img :src="profileIcon" alt="Character" class="character-image" />
      <button class="exchange-button">ОБМЕНЯТЬ</button>
    </div>

    <!-- Bottom Actions -->
    <div class="bottom-actions">
      <button v-for="(action, index) in actions" :key="index" class="action-button">
        <img :src="action.icon" :alt="action.name" />
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import { useRouter } from 'vue-router';
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

const router = useRouter();

onMounted(() => {
  if (window.Telegram?.WebApp) {
    // Инициализация WebApp
    window.Telegram.WebApp.ready();
    window.Telegram.WebApp.expand();
    
    // Показ кнопки назад
    window.Telegram.WebApp.BackButton.show();
    window.Telegram.WebApp.BackButton.onClick(() => {
      router.push('/');
    });
  }
});

onUnmounted(() => {
  if (window.Telegram?.WebApp) {
    // Скрытие кнопки назад
    window.Telegram.WebApp.BackButton.hide();
  }
});

const level = ref(7);
const xp = ref(25);
const xpProgress = ref((xp.value / 100) * 100);

const actions = ref([
  { name: "Ежедневные задания", icon: dailyIcon2 },
  { name: "Творчество", icon: creativityIcon },
  { name: "Ребусы", icon: rebusIcon },
  { name: "Загадки", icon: riddlesIcon },
  { name: "Скороговорки", icon: tongueTwisterIcon },
  { name: "Нейрогимнастика", icon: neuroIcon },
  { name: "Артикулярная гимнастика", icon: articulationIcon },
]);

function exchange() {
  alert("Функция обмена не реализована!");
}
</script>

<style scoped>
.profile {
  background: linear-gradient(180deg, #1e3a8a 0%, #1e40af 100%);
  min-height: 100vh;
  color: white;
  padding: 0;
  display: flex;
  flex-direction: column;
}

header {
  background: rgba(0, 0, 0, 0.2);
  padding: 1rem;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

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

.settings-button {
  background: none;
  border: none;
  padding: 0.5rem;
}

.settings-button img {
  width: 1.5rem;
  height: 1.5rem;
}

.stats-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(255, 255, 255, 0.1);
  padding: 0.75rem;
  border-radius: 1rem;
  margin-bottom: 1rem;
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

.level-info {
  text-align: center;
  margin-bottom: 2rem;
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

.character-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  margin: auto 0;
}

.character-image {
  width: 12rem;
  height: 12rem;
  object-fit: contain;
}

.exchange-button {
  background: #3b82f6;
  color: white;
  border: none;
  padding: 0.75rem 2rem;
  border-radius: 2rem;
  font-weight: bold;
  font-size: 1.1rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
}

.exchange-button:active {
  transform: scale(0.98);
}

.bottom-actions {
  display: flex;
  justify-content: space-around;
  padding: 1rem 0;
  margin-top: auto;
}

.action-button {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  padding: 0.75rem;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.2s ease;
}

.action-button img {
  width: 1.5rem;
  height: 1.5rem;
}

.action-button:active {
  background: rgba(255, 255, 255, 0.2);
}
</style>

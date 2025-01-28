<template>
  <div class="profile container">
    <!-- Header -->
    <header class="header">
      <button class="back-button clickable" @click="goBack">&#8592;</button>
      <h1 class="username">Тима#564</h1>
      <button class="settings-button clickable">
        <img src="@/assets/gear-icon.png" alt="Settings" class="icon" />
      </button>
    </header>

    <!-- User Stats -->
    <div class="stats">
      <div class="stat-item clickable">
        <img src="@/assets/coin-icon.png" alt="Coins" class="icon" />
        <span>1,555,000</span>
      </div>
      <div class="stat-item clickable">
        <img src="@/assets/daily.png" alt="Targets" class="icon" />
        <span>25</span>
      </div>
      <div class="stat-item clickable">
        <img src="@/assets/trophy-icon.png" alt="Trophies" class="icon" />
        <span>3</span>
      </div>
    </div>

    <!-- XP Bar -->
    <div class="xp-container">
      <div class="xp-bar">
        <div class="xp-progress" :style="{ width: xpProgress + '%' }"></div>
      </div>
      <p class="xp-text">Уровень {{ level }} ({{ xp }}/100 XP)</p>
    </div>

    <!-- Character -->
    <div class="character">
      <img src="@/assets/profile.png" alt="Character" class="character-image" />
      <button class="exchange-button clickable" @click="exchange">
        Обменять
      </button>
    </div>

    <!-- Actions -->
    <div class="actions">
      <button
        v-for="(action, index) in actions"
        :key="index"
        class="action-button clickable"
      >
        <img :src="require(`@/assets/${action.icon}`)" :alt="action.name" class="action-icon" />
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from 'vue-router';

const router = useRouter();

const level = ref(7);
const xp = ref(25);
const xpProgress = ref((xp.value / 100) * 100);

const actions = ref([
  { name: "Творчество", icon: "creativity.png" },
  { name: "Задания", icon: "daily.png" },
  { name: "Ребусы", icon: "rebus.png" },
  { name: "Загадки", icon: "riddles.png" },
  { name: "Артикулярная", icon: "articulation.png" },
  { name: "Нейрогимнастика", icon: "neuro.png" },
  { name: "Скороговорки", icon: "tonguetwisters.png" },
]);

function exchange() {
  alert("Функция обмена не реализована!");
}

function goBack() {
  router.push('/');
}
</script>

<style scoped>
.profile {
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  padding: 20px;
  background: var(--tg-theme-bg-color);
  color: var(--tg-theme-text-color);
}

.header {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.back-button, .settings-button {
  background: none;
  border: none;
  font-size: 24px;
  color: var(--tg-theme-text-color);
  padding: 10px;
  cursor: pointer;
}

.username {
  font-size: 20px;
  font-weight: bold;
}

.stats {
  width: 100%;
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  background: var(--tg-theme-secondary-bg-color, rgba(255, 255, 255, 0.1));
  border-radius: 12px;
}

.icon {
  width: 24px;
  height: 24px;
}

.xp-container {
  width: 100%;
  margin-bottom: 30px;
}

.xp-bar {
  width: 100%;
  height: 16px;
  background: var(--tg-theme-secondary-bg-color, rgba(255, 255, 255, 0.1));
  border-radius: 8px;
  overflow: hidden;
}

.xp-progress {
  height: 100%;
  background: var(--tg-theme-button-color);
  transition: width 0.3s ease;
}

.xp-text {
  text-align: center;
  margin-top: 8px;
  font-size: 14px;
  color: var(--tg-theme-hint-color);
}

.character {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 30px;
}

.character-image {
  width: 160px;
  height: 160px;
  margin-bottom: 20px;
}

.exchange-button {
  background: var(--tg-theme-button-color);
  color: var(--tg-theme-button-text-color);
  border: none;
  padding: 12px 24px;
  border-radius: 20px;
  font-size: 16px;
  font-weight: bold;
}

.actions {
  width: 100%;
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  gap: 15px;
}

.action-button {
  background: var(--tg-theme-secondary-bg-color, rgba(255, 255, 255, 0.1));
  border: none;
  padding: 12px;
  border-radius: 50%;
}

.action-icon {
  width: 24px;
  height: 24px;
}
</style>

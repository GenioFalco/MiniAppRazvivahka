<template>
  <div class="main-menu">
    <div class="menu-grid">
      <router-link to="/profile" class="menu-item">
        <img :src="profileIcon" alt="Профиль" />
        <span>Профиль</span>
      </router-link>

      <router-link to="/shop" class="menu-item">
        <img :src="shopIcon" alt="Магазин" />
        <span>Магазин</span>
      </router-link>

      <router-link to="/subscription" class="menu-item">
        <img :src="subscriptionIcon" alt="Подписка" />
        <span>Подписка</span>
      </router-link>

      <router-link to="/photoalbum" class="menu-item">
        <img :src="photoalbumIcon" alt="Фотоальбом" />
        <span>Фотоальбом</span>
      </router-link>

      <div class="menu-item" @click="toggleDailyRewards">
        <img :src="dailyAdmissionIcon" alt="Ежедневный вход" />
        <span>Ежедневный вход</span>
      </div>
    </div>

    <div class="tasks-list">
      <router-link to="/tasks/creativity" class="task-item">
        <img :src="creativityIcon" alt="Творчество" />
        <span>Творчество</span>
      </router-link>

      <router-link to="/tasks/daily" class="task-item">
        <img :src="dailyIcon" alt="Задания на день" />
        <span>Задания на день</span>
      </router-link>

      <router-link to="/tasks/riddles" class="task-item">
        <img :src="riddlesIcon" alt="Загадки" />
        <span>Загадки</span>
      </router-link>

      <router-link to="/tasks/tonguetwisters" class="task-item">
        <img :src="tongueTwistersIcon" alt="Скороговорки" />
        <span>Скороговорки</span>
      </router-link>
    </div>

    <!-- Панель ежедневных наград -->
    <DailyRewardsPanel 
      :is-visible="isDailyRewardsVisible"
      @close="toggleDailyRewards"
      @claim-reward="handleClaimReward"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import DailyRewardsPanel from './DailyRewardsPanel.vue';

// Импорт иконок
import profileIcon from '@/assets/profile.png';
import shopIcon from '@/assets/shop.png';
import subscriptionIcon from '@/assets/subscription.png';
import photoalbumIcon from '@/assets/photoalbum.png';
import dailyAdmissionIcon from '@/assets/daily_admission.png';
import creativityIcon from '@/assets/creativity.png';
import dailyIcon from '@/assets/daily.png';
import riddlesIcon from '@/assets/riddles.png';
import tongueTwistersIcon from '@/assets/tonguetwisters.png';

const router = useRouter();
const isDailyRewardsVisible = ref(false);

function toggleDailyRewards() {
  isDailyRewardsVisible.value = !isDailyRewardsVisible.value;
}

function handleClaimReward(data) {
  // Здесь будет логика обработки получения награды
  console.log('Claim reward data:', data);
}
</script>

<style scoped>
.main-menu {
  padding: 1rem;
  background: var(--tg-theme-bg-color, #ffffff);
  min-height: 100vh;
}

.menu-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-bottom: 2rem;
}

.menu-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
  color: var(--tg-theme-text-color, #000000);
  padding: 1rem;
  background: var(--tg-theme-secondary-bg-color, #f0f2f5);
  border-radius: 12px;
  transition: transform 0.2s;
}

.menu-item:hover {
  transform: translateY(-2px);
}

.menu-item img {
  width: 48px;
  height: 48px;
  object-fit: contain;
}

.menu-item span {
  font-size: 0.9rem;
  text-align: center;
}

.tasks-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.task-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: var(--tg-theme-secondary-bg-color, #f0f2f5);
  border-radius: 12px;
  text-decoration: none;
  color: var(--tg-theme-text-color, #000000);
  transition: transform 0.2s;
}

.task-item:hover {
  transform: translateX(4px);
}

.task-item img {
  width: 32px;
  height: 32px;
  object-fit: contain;
}

.task-item span {
  font-size: 1rem;
}
</style> 
<template>
  <div class="home">
    <div class="menu-list">
      <div class="menu-item" @click="navigateToCategory('creativity')">
        <div class="menu-icon">🎨</div>
        <div class="menu-text">ТВОРЧЕСТВО</div>
      </div>
      
      <div class="menu-item" @click="navigateToCategory('daily')">
        <div class="menu-icon">©️</div>
        <div class="menu-text">ЗАДАНИЯ НА ДЕНЬ</div>
      </div>
      
      <div class="menu-item" @click="navigateToCategory('riddles')">
        <div class="menu-icon">💬</div>
        <div class="menu-text">ЗАГАДКИ</div>
      </div>
      
      <div class="menu-item" @click="navigateToCategory('tonguetwisters')">
        <div class="menu-icon">⏰</div>
        <div class="menu-text">СКОРОГОВОРКИ</div>
      </div>
      
      <div class="menu-item" @click="navigateToCategory('rebus')">
        <div class="menu-icon">❓</div>
        <div class="menu-text">РЕБУСЫ</div>
      </div>
      
      <div class="menu-item" @click="navigateToCategory('articulation')">
        <div class="menu-icon">👋</div>
        <div class="menu-text">АРТИКУЛЯРНАЯ ГИМНАСТИКА</div>
      </div>
      
      <div class="menu-item" @click="navigateToCategory('neuro')">
        <div class="menu-icon">🧠</div>
        <div class="menu-text">НЕЙРОГИМНАСТИКА</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const navigateToCategory = (category) => {
  router.push(`/tasks?category=${category}`)
}
</script>

<style scoped>
.home {
  padding: 0;
  background-color: var(--tg-theme-bg-color);
  min-height: 100vh;
}

.menu-list {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.menu-item {
  display: flex;
  align-items: center;
  padding: 16px;
  background-color: var(--tg-theme-secondary-bg-color);
  cursor: pointer;
  transition: background-color 0.2s;
}

.menu-item:active {
  background-color: var(--tg-theme-button-color);
  opacity: 0.7;
}

.menu-icon {
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  margin-right: 16px;
}

.menu-text {
  color: var(--tg-theme-text-color);
  font-size: 16px;
  font-weight: 500;
}

/* Добавляем эффект при наведении только на устройствах с мышью */
@media (hover: hover) {
  .menu-item:hover {
    background-color: var(--tg-theme-button-color);
    opacity: 0.7;
  }
}
</style>

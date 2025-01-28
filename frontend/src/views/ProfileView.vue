<template>
  <div class="profile">
    <div class="profile-header">
      <div class="avatar">
        {{ userInitials }}
      </div>
      <h1>{{ userData.first_name }} {{ userData.last_name }}</h1>
      <p class="username">@{{ userData.username }}</p>
    </div>

    <div class="stats">
      <div class="stat-card">
        <h3>Решено задач</h3>
        <p class="stat-value">{{ stats.solved }}</p>
      </div>
      <div class="stat-card">
        <h3>Очки</h3>
        <p class="stat-value">{{ stats.points }}</p>
      </div>
      <div class="stat-card">
        <h3>Уровень</h3>
        <p class="stat-value">{{ stats.level }}</p>
      </div>
    </div>

    <div class="achievements">
      <h2>Достижения</h2>
      <div class="achievements-grid">
        <div 
          v-for="achievement in achievements" 
          :key="achievement.id"
          class="achievement-card"
          :class="{ 'achievement-locked': !achievement.unlocked }"
        >
          <div class="achievement-icon">{{ achievement.icon }}</div>
          <h3>{{ achievement.name }}</h3>
          <p>{{ achievement.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'

const userData = ref({
  first_name: 'Пользователь',
  last_name: 'Telegram',
  username: 'user',
})

const stats = ref({
  solved: 0,
  points: 0,
  level: 1
})

const achievements = ref([
  {
    id: 1,
    name: 'Первые шаги',
    description: 'Решите первую задачу',
    icon: '🎯',
    unlocked: true
  },
  {
    id: 2,
    name: 'Математик',
    description: 'Решите 10 задач по математике',
    icon: '🔢',
    unlocked: false
  },
  {
    id: 3,
    name: 'Логик',
    description: 'Решите 10 логических задач',
    icon: '🧩',
    unlocked: false
  }
])

const userInitials = computed(() => {
  const first = userData.value.first_name.charAt(0)
  const last = userData.value.last_name.charAt(0)
  return `${first}${last}`
})

onMounted(() => {
  // Получаем данные пользователя из Telegram WebApp
  if (window.Telegram?.WebApp) {
    const tgUser = window.Telegram.WebApp.initDataUnsafe?.user
    if (tgUser) {
      userData.value = {
        first_name: tgUser.first_name,
        last_name: tgUser.last_name || '',
        username: tgUser.username || 'user'
      }
    }
  }
})
</script>

<style scoped>
.profile {
  padding: 1rem;
  max-width: 800px;
  margin: 0 auto;
}

.profile-header {
  text-align: center;
  margin-bottom: 2rem;
}

.avatar {
  width: 80px;
  height: 80px;
  background: var(--tg-theme-button-color, #2196F3);
  color: var(--tg-theme-button-text-color, white);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: bold;
  margin: 0 auto 1rem;
}

.username {
  color: var(--tg-theme-hint-color, #666);
}

.stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: var(--tg-theme-secondary-bg-color, white);
  padding: 1rem;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.stat-value {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--tg-theme-button-color, #2196F3);
}

.achievements h2 {
  margin-bottom: 1rem;
  text-align: center;
}

.achievements-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.achievement-card {
  background: var(--tg-theme-secondary-bg-color, white);
  padding: 1rem;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.achievement-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.achievement-locked {
  opacity: 0.5;
}

.achievement-locked .achievement-icon {
  filter: grayscale(1);
}
</style> 
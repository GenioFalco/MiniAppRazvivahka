<template>
  <div class="home">
    <div class="welcome-section">
      <h1>Добро пожаловать в Развивахку!</h1>
      <p>Давайте учиться и развиваться вместе</p>
    </div>
    
    <div class="categories">
      <div 
        v-for="category in categories" 
        :key="category.id" 
        class="category-card"
        @click="selectCategory(category)"
      >
        <div class="category-icon">{{ category.emoji }}</div>
        <h3>{{ category.name }}</h3>
        <p>{{ category.description }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const categories = ref([
  {
    id: 1,
    name: 'Математика',
    description: 'Увлекательные задачи по математике',
    emoji: '🔢'
  },
  {
    id: 2,
    name: 'Логика',
    description: 'Развивающие логические задачи',
    emoji: '🧩'
  },
  {
    id: 3,
    name: 'Память',
    description: 'Упражнения для развития памяти',
    emoji: '🧠'
  }
])

const selectCategory = (category) => {
  router.push(`/tasks?category=${category.id}`)
}
</script>

<style scoped>
.home {
  padding: 1rem;
}

.welcome-section {
  text-align: center;
  margin-bottom: 2rem;
}

.welcome-section h1 {
  color: var(--tg-theme-button-color, #2196F3);
  margin-bottom: 0.5rem;
  font-size: 1.5rem;
}

.categories {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

.category-card {
  background: var(--tg-theme-secondary-bg-color, white);
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  cursor: pointer;
  transition: transform 0.2s;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.category-card:hover {
  transform: translateY(-5px);
}

.category-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.category-card h3 {
  color: var(--tg-theme-text-color, #2196F3);
  margin-bottom: 0.5rem;
}

.category-card p {
  color: var(--tg-theme-hint-color, #666);
  font-size: 0.9rem;
}
</style>

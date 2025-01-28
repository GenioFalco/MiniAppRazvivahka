<template>
  <div class="tasks">
    <h1>{{ currentCategory ? currentCategory.name : 'Все задания' }}</h1>
    
    <div class="tasks-list">
      <div v-for="task in tasks" :key="task.id" class="task-card">
        <h3>{{ task.title }}</h3>
        <p>{{ task.description }}</p>
        <div class="task-footer">
          <span class="difficulty">Сложность: {{ task.difficulty }}/5</span>
          <button 
            class="solve-button"
            @click="startTask(task)"
          >
            Решить
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const currentCategory = ref(null)
const tasks = ref([
  {
    id: 1,
    title: 'Сложение чисел',
    description: 'Решите простую задачу на сложение двух чисел',
    difficulty: 1,
    categoryId: 1
  },
  {
    id: 2,
    title: 'Логическая загадка',
    description: 'Решите интересную логическую загадку',
    difficulty: 2,
    categoryId: 2
  },
  {
    id: 3,
    title: 'Тренировка памяти',
    description: 'Запомните и воспроизведите последовательность',
    difficulty: 3,
    categoryId: 3
  }
])

onMounted(() => {
  const categoryId = parseInt(route.query.category)
  if (categoryId) {
    tasks.value = tasks.value.filter(task => task.categoryId === categoryId)
    currentCategory.value = {
      id: categoryId,
      name: getCategoryName(categoryId)
    }
  }
})

function getCategoryName(id) {
  const categories = {
    1: 'Математика',
    2: 'Логика',
    3: 'Память'
  }
  return categories[id] || 'Неизвестная категория'
}

function startTask(task) {
  // Здесь будет логика начала решения задания
  console.log('Начинаем решение задания:', task)
}
</script>

<style scoped>
.tasks {
  padding: 1rem;
}

h1 {
  color: var(--tg-theme-text-color, #2c3e50);
  margin-bottom: 2rem;
  text-align: center;
}

.tasks-list {
  display: grid;
  gap: 1rem;
  max-width: 800px;
  margin: 0 auto;
}

.task-card {
  background: var(--tg-theme-secondary-bg-color, white);
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.task-card h3 {
  color: var(--tg-theme-text-color, #2196F3);
  margin-bottom: 0.5rem;
}

.task-card p {
  color: var(--tg-theme-hint-color, #666);
  margin-bottom: 1rem;
}

.task-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.difficulty {
  color: var(--tg-theme-hint-color, #666);
  font-size: 0.9rem;
}

.solve-button {
  background: var(--tg-theme-button-color, #2196F3);
  color: var(--tg-theme-button-text-color, white);
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  transition: opacity 0.2s;
}

.solve-button:hover {
  opacity: 0.9;
}
</style> 
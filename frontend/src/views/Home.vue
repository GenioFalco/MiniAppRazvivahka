<template>
  <div class="home">
    <div class="welcome-section">
      <h1>Добро пожаловать в Развивахку!</h1>
      <p>Давайте учиться и развиваться вместе</p>
    </div>
    
    <div class="categories">
      <div class="category-card" v-for="category in categories" :key="category.id" @click="selectCategory(category)">
        <img :src="category.icon" :alt="category.name">
        <h3>{{ category.name }}</h3>
        <p>{{ category.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      categories: [
        {
          id: 1,
          name: 'Математика',
          description: 'Увлекательные задачи по математике',
          icon: '/icons/math.svg'
        },
        {
          id: 2,
          name: 'Логика',
          description: 'Развивающие логические задачи',
          icon: '/icons/logic.svg'
        },
        {
          id: 3,
          name: 'Память',
          description: 'Упражнения для развития памяти',
          icon: '/icons/memory.svg'
        }
      ]
    }
  },
  methods: {
    selectCategory(category) {
      this.$router.push(`/category/${category.id}`);
    }
  }
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
  color: #2196F3;
  margin-bottom: 0.5rem;
}

.categories {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  padding: 1rem;
}

.category-card {
  background: white;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
  cursor: pointer;
  transition: transform 0.2s;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.category-card:hover {
  transform: translateY(-5px);
}

.category-card img {
  width: 64px;
  height: 64px;
  margin-bottom: 1rem;
}

.category-card h3 {
  color: #2196F3;
  margin-bottom: 0.5rem;
}

.category-card p {
  color: #666;
  font-size: 0.9rem;
}
</style> 
<template>
  <div class="main-menu">
    <!-- Верхняя часть меню с иконками профиля, подписки и фотоальбома -->
    <div class="top-menu">
      <div class="menu-card">
        <img src="/assets/profile.png" alt="Профиль" class="menu-icon" />
        <span>Профиль</span>
      </div>
      <div class="menu-card">
        <img src="/assets/subscription.png" alt="Подписка" class="menu-icon" />
        <span>Подписка</span>
      </div>
      <div class="menu-card">
        <img src="/assets/photoalbum.png" alt="Фотоальбом" class="menu-icon" />
        <span>Фотоальбом</span>
      </div>
    </div>

    <!-- Список категорий -->
    <div class="categories">
      <div class="category-item">
        <img src="/assets/creativity.png" alt="Творчество" class="category-icon" />
        <span>Творчество</span>
      </div>
      <div class="category-item">
        <img src="/assets/daily.png" alt="Задания на день" class="category-icon" />
        <span>Задания на день</span>
      </div>
      <div class="category-item">
        <img src="/assets/riddles.png" alt="Загадки" class="category-icon" />
        <span>Загадки</span>
      </div>
      <div class="category-item">
        <img src="/assets/tonguetwisters.png" alt="Скороговорки" class="category-icon" />
        <span>Скороговорки</span>
      </div>
      <div class="category-item">
        <img src="/assets/rebus.png" alt="Ребусы" class="category-icon" />
        <span>Ребусы</span>
      </div>
      <div class="category-item">
        <img src="/assets/articulation.png" alt="Артикулярная гимнастика" class="category-icon" />
        <span>Артикулярная гимнастика</span>
      </div>
      <div class="category-item">
        <img src="/assets/neuro.png" alt="Нейрогимнастика" class="category-icon" />
        <span>Нейрогимнастика</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainMenu",
};
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
  display: flex;
  gap: 20px;
  margin-bottom: 30px;
}

.menu-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.menu-icon {
  width: 60px;
  height: 60px;
  margin-bottom: 5px;
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
  transition: transform 0.2s ease, background 0.2s ease;
}

.category-item:hover {
  transform: scale(1.05);
  background: rgba(255, 255, 255, 0.2);
}

.category-icon {
  width: 40px;
  height: 40px;
}
</style>

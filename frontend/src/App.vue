<template>
  <div id="app">
    <nav class="nav-menu" v-if="showNav">
      <router-link to="/" class="nav-link">Главная</router-link>
      <router-link to="/tasks" class="nav-link">Задания</router-link>
      <router-link to="/profile" class="nav-link">Профиль</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      showNav: true
    }
  },
  created() {
    // Проверяем, запущено ли приложение в Telegram
    if (window.Telegram?.WebApp) {
      this.showNav = false;
      // Инициализация Telegram Mini App
      window.Telegram.WebApp.ready();
      // Устанавливаем тему
      window.Telegram.WebApp.setHeaderColor('#2196F3');
    }
  }
}
</script>

<style>
#app {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
    Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.nav-menu {
  padding: 1rem;
  background: #f8f9fa;
}

.nav-link {
  margin: 0 1rem;
  color: #2196F3;
  text-decoration: none;
  font-weight: 500;
}

.nav-link.router-link-active {
  color: #1976D2;
  border-bottom: 2px solid #1976D2;
}
</style> 
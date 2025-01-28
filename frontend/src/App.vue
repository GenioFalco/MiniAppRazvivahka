<template>
  <div class="app" :class="{ 'dark': isDarkTheme }">
    <RouterView v-if="isInitialized" />
    <div v-else class="loading">Загрузка...</div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { RouterView } from 'vue-router'

const isInitialized = ref(false)
const isDarkTheme = computed(() => {
  return window.Telegram?.WebApp?.colorScheme === 'dark'
})

onMounted(() => {
  // Проверяем, запущено ли приложение в Telegram
  if (window.Telegram?.WebApp) {
    // Инициализируем Telegram WebApp
    window.Telegram.WebApp.ready()
    window.Telegram.WebApp.expand()
    
    // Получаем тему
    document.documentElement.className = window.Telegram.WebApp.colorScheme
    
    // Устанавливаем цвета из Telegram WebApp
    document.documentElement.style.setProperty('--tg-theme-bg-color', window.Telegram.WebApp.backgroundColor)
    document.documentElement.style.setProperty('--tg-theme-text-color', window.Telegram.WebApp.textColor)
    document.documentElement.style.setProperty('--tg-theme-hint-color', window.Telegram.WebApp.backgroundColor)
    document.documentElement.style.setProperty('--tg-theme-link-color', window.Telegram.WebApp.linkColor)
    document.documentElement.style.setProperty('--tg-theme-button-color', window.Telegram.WebApp.buttonColor)
    document.documentElement.style.setProperty('--tg-theme-button-text-color', window.Telegram.WebApp.buttonTextColor)
    
    // Помечаем, что инициализация завершена
    isInitialized.value = true
  } else {
    // Если запущено не в Telegram, просто показываем контент
    isInitialized.value = true
  }
})
</script>

<style>
:root {
  --tg-theme-bg-color: var(--tg-theme-bg-color, #fff);
  --tg-theme-text-color: var(--tg-theme-text-color, #000);
  --tg-theme-hint-color: var(--tg-theme-hint-color, #999);
  --tg-theme-link-color: var(--tg-theme-link-color, #2678b6);
  --tg-theme-button-color: var(--tg-theme-button-color, #2678b6);
  --tg-theme-button-text-color: var(--tg-theme-button-text-color, #fff);
  --tg-theme-secondary-bg-color: var(--tg-theme-secondary-bg-color, #f0f0f0);
}

body {
  background-color: var(--tg-theme-bg-color);
  color: var(--tg-theme-text-color);
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
    Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}

.app {
  min-height: 100vh;
  padding: 1rem;
}

.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  font-size: 1.2rem;
  color: var(--tg-theme-text-color);
}

.dark {
  --tg-theme-bg-color: #1f1f1f;
  --tg-theme-text-color: #fff;
  --tg-theme-hint-color: #aaa;
  --tg-theme-link-color: #64b5f6;
  --tg-theme-button-color: #64b5f6;
  --tg-theme-secondary-bg-color: #2f2f2f;
}
</style>

<template>
  <div class="app" :class="{ 'dark': isDarkTheme }">
    <RouterView />
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { RouterView } from 'vue-router'

const isDarkTheme = computed(() => {
  return window.Telegram?.WebApp?.colorScheme === 'dark'
})

// Инициализация Telegram WebApp
onMounted(() => {
  if (window.Telegram?.WebApp) {
    window.Telegram.WebApp.ready()
    window.Telegram.WebApp.expand()
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

.dark {
  --tg-theme-bg-color: #1f1f1f;
  --tg-theme-text-color: #fff;
  --tg-theme-hint-color: #aaa;
  --tg-theme-link-color: #64b5f6;
  --tg-theme-button-color: #64b5f6;
  --tg-theme-secondary-bg-color: #2f2f2f;
}
</style>

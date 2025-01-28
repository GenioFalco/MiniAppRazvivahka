<template>
  <div class="profile bg-gradient-to-b from-blue-900 to-blue-800 h-screen w-screen flex flex-col items-center text-white">
    <!-- Header -->
    <header class="w-full flex items-center justify-between px-4 py-3">
      <button class="text-2xl">&#8592;</button>
      <h1 class="text-xl font-bold">Тима#564</h1>
      <button>
        <img src="@/assets/settings.png" alt="Settings" class="w-6 h-6" />
      </button>
    </header>

    <!-- User Stats -->
    <div class="stats w-full px-6 flex items-center justify-between my-4">
      <div class="flex items-center">
        <img src="coin-icon.png" alt="Coins" class="w-6 h-6 mr-2" />
        <span>1,555,000</span>
      </div>
      <div class="flex items-center">
        <img src="daily.png" alt="Targets" class="w-6 h-6 mr-2" />
        <span>25</span>
      </div>
      <div class="flex items-center">
        <img src="trophy-icon.png" alt="Trophies" class="w-6 h-6 mr-2" />
        <span>3</span>
      </div>
    </div>

    <!-- XP Bar -->
    <div class="xp-bar w-3/4 bg-gray-700 h-4 rounded-full overflow-hidden">
      <div
        class="bg-blue-500 h-full"
        :style="{ width: xpProgress + '%' }"
      ></div>
    </div>
    <p class="mt-2 text-sm">Уровень {{ level }} ({{ xp }}/100 XP)</p>

    <!-- Character -->
    <div class="character my-6">
      <img src="profile.png" alt="Character" class="w-40 h-40" />
      <button
        class="mt-4 px-6 py-2 bg-blue-600 rounded-full text-lg font-bold shadow-lg hover:bg-blue-700 transition"
        @click="exchange"
      >
        Обменять
      </button>
    </div>

    <!-- Actions -->
    <div class="actions flex justify-around w-full px-6">
      <button
        v-for="(action, index) in actions"
        :key="index"
        class="p-3 bg-blue-600 rounded-full shadow-lg hover:bg-blue-700 transition"
      >
        <img :src="action.icon" :alt="action.name" class="w-6 h-6" />
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

// Параметры профиля
const level = ref(7);
const xp = ref(25);
const xpProgress = ref((xp.value / 100) * 100);

// Действия профиля
const actions = ref([
  { name: "Настройка", icon: "@/assets/neuro.png" },
  { name: "Статистика", icon: "@/assets/creativity.png" },
  { name: "Подсказки", icon: "@/assets/rebus.png" },
  { name: "Ручной режим", icon: "@/assets/riddles.png" },
  { name: "Настройки", icon: "@/assets/settings.png" },
]);

// Функция обмена
function exchange() {
  alert("Функция обмена не реализована!");
}
</script>

<style scoped>
.profile {
  font-family: "Arial", sans-serif;
}
</style>

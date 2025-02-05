<template>
  <div class="photo-album">
    <header>
      <div class="header-content">
        <h1>Фотоальбом</h1>
      </div>
    </header>

    <div class="photos-grid">
      <div v-for="photo in photos" :key="photo.id" class="photo-card">
        <div class="photo-container">
          <img :src="photo.url" :alt="photo.caption" @click="openPhoto(photo)" />
        </div>
        <div class="photo-info">
          <span class="author">{{ photo.author }}</span>
          <span class="date">{{ formatDate(photo.date) }}</span>
        </div>
      </div>
    </div>

    <!-- Модальное окно для просмотра фото -->
    <div v-if="selectedPhoto" class="photo-modal" @click="closePhoto">
      <div class="modal-content">
        <img :src="selectedPhoto.url" :alt="selectedPhoto.caption" />
        <div class="modal-info">
          <span class="author">{{ selectedPhoto.author }}</span>
          <span class="date">{{ formatDate(selectedPhoto.date) }}</span>
          <p class="caption">{{ selectedPhoto.caption }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const photos = ref([]);
const selectedPhoto = ref(null);

// Функция для форматирования даты
function formatDate(timestamp) {
  return new Date(timestamp * 1000).toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric'
  });
}

// Функция для открытия фото в модальном окне
function openPhoto(photo) {
  selectedPhoto.value = photo;
  document.body.style.overflow = 'hidden';
}

// Функция для закрытия модального окна
function closePhoto() {
  selectedPhoto.value = null;
  document.body.style.overflow = '';
}

// Загрузка фотографий из канала
onMounted(async () => {
  try {
    // Используем метод getMessages вместо getChat
    const response = await fetch('https://api.telegram.org/bot7072578872:AAHCAnoA7kgsRc9qgg0j62mNum-9dGp73Kg/getUpdates');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    
    // Временно используем тестовые данные, пока не настроим правильный доступ к API
    photos.value = [
      {
        id: 1,
        url: 'https://via.placeholder.com/300',
        author: 'Test User 1',
        date: Math.floor(Date.now() / 1000),
        caption: 'Тестовое фото 1'
      },
      {
        id: 2,
        url: 'https://via.placeholder.com/300',
        author: 'Test User 2',
        date: Math.floor(Date.now() / 1000),
        caption: 'Тестовое фото 2'
      }
    ];
    
  } catch (error) {
    console.error('Error loading photos:', error);
    // Используем простой alert вместо Telegram WebApp методов
    alert('Не удалось загрузить фотографии. Пожалуйста, попробуйте позже.');
  }
});
</script>

<style scoped>
.photo-album {
  min-height: 100vh;
  background: linear-gradient(180deg, #4a90e2, #003f7f);
  padding: 1rem;
  color: white;
}

header {
  position: sticky;
  top: 0;
  z-index: 10;
  background: rgba(0, 0, 0, 0.2);
  padding: 1rem;
  margin: -1rem -1rem 1rem -1rem;
}

.header-content {
  display: flex;
  justify-content: center;
  align-items: center;
}

h1 {
  margin: 0;
  font-size: 1.5rem;
  font-weight: bold;
}

.photos-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  gap: 1rem;
  padding: 1rem 0;
}

.photo-card {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.2s;
  cursor: pointer;
}

.photo-card:hover {
  transform: scale(1.02);
}

.photo-container {
  aspect-ratio: 1;
  overflow: hidden;
}

.photo-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.photo-info {
  padding: 0.5rem;
  font-size: 0.9rem;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.author {
  font-weight: bold;
}

.date {
  opacity: 0.8;
  font-size: 0.8rem;
}

/* Стили для модального окна */
.photo-modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  max-width: 90vw;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.modal-content img {
  max-width: 100%;
  max-height: 70vh;
  object-fit: contain;
}

.modal-info {
  padding: 1rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 12px;
}

.caption {
  margin: 0.5rem 0 0 0;
  font-size: 0.9rem;
  line-height: 1.4;
}

@media (min-width: 768px) {
  .photos-grid {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
}

@media (min-width: 1024px) {
  .photos-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  }
}
</style> 
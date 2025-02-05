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

// Загрузка фотографий из Google Drive
onMounted(() => {
  // Массив с фотографиями из Google Drive
  // Замените эти URL на реальные ссылки из вашей публичной папки Google Drive
  photos.value = [
    {
      id: 1,
      url: 'https://drive.google.com/uc?export=view&id=YOUR_PHOTO_ID_1',
      author: 'Автор 1',
      date: Math.floor(Date.now() / 1000),
      caption: 'Описание фото 1'
    },
    {
      id: 2,
      url: 'https://drive.google.com/uc?export=view&id=YOUR_PHOTO_ID_2',
      author: 'Автор 2',
      date: Math.floor(Date.now() / 1000),
      caption: 'Описание фото 2'
    },
    {
      id: 3,
      url: 'https://drive.google.com/uc?export=view&id=YOUR_PHOTO_ID_3',
      author: 'Автор 3',
      date: Math.floor(Date.now() / 1000),
      caption: 'Описание фото 3'
    }
  ];
});
</script>

<style scoped>
.photo-album {
  min-height: 100vh;
  background: linear-gradient(180deg, #4a90e2, #003f7f);
  padding: 1rem;
  color: white;
  padding-top: 4rem; /* Добавляем отступ сверху для кнопки назад */
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
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 1.5rem;
  padding: 1rem;
}

.photo-card {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.2s;
  cursor: pointer;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.photo-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

.photo-container {
  position: relative;
  padding-bottom: 100%; /* Создаем квадратный контейнер */
  overflow: hidden;
}

.photo-container img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.photo-info {
  padding: 1rem;
  background: rgba(0, 0, 0, 0.2);
}

.author {
  display: block;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.date {
  font-size: 0.9rem;
  opacity: 0.8;
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
  z-index: 1001;
}

.modal-content {
  max-width: 90vw;
  max-height: 90vh;
  position: relative;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 12px;
}

.modal-content img {
  max-width: 100%;
  max-height: 70vh;
  object-fit: contain;
  border-radius: 8px;
}

.modal-info {
  margin-top: 1rem;
  padding: 1rem;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 8px;
}

.caption {
  margin-top: 0.5rem;
  font-size: 0.9rem;
  line-height: 1.4;
}

@media (max-width: 768px) {
  .photos-grid {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 1rem;
  }
}
</style> 
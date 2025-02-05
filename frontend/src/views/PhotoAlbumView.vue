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
          <img :src="photo.url" :alt="photo.author" @click="openPhoto(photo)" />
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
        <img :src="selectedPhoto.url" :alt="selectedPhoto.author" />
        <div class="modal-info">
          <span class="author">{{ selectedPhoto.author }}</span>
          <span class="date">{{ formatDate(selectedPhoto.date) }}</span>
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

// Загрузка фотографий из Яндекс.Диска
onMounted(async () => {
  try {
    // Публичная ссылка на папку Яндекс.Диска
    const PUBLIC_FOLDER_URL = 'https://disk.yandex.ru/d/odb9rYQBjq_1Cw';
    
    // Получаем список файлов из публичной папки
    const response = await fetch(
      `https://cloud-api.yandex.net/v1/disk/public/resources?public_key=${encodeURIComponent(PUBLIC_FOLDER_URL)}&limit=100&preview_size=L`,
      {
        headers: {
          'Accept': 'application/json'
        }
      }
    );

    if (!response.ok) {
      throw new Error('Не удалось загрузить список фотографий');
    }

    const data = await response.json();
    
    // Преобразуем данные в нужный формат
    photos.value = data._embedded.items
      .filter(item => item.type === 'file' && item.mime_type.startsWith('image/'))
      .map(file => ({
        id: file.resource_id,
        url: file.file, // Прямая ссылка на файл
        author: file.name.split('.')[0], // Имя файла без расширения как автор
        date: new Date(file.created).getTime() / 1000
      }));

  } catch (error) {
    console.error('Ошибка при загрузке фотографий:', error);
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
  transition: opacity 0.3s;
}

/* Добавляем индикатор загрузки */
.photo-container::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 30px;
  height: 30px;
  border: 3px solid rgba(255, 255, 255, 0.3);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  opacity: 0;
}

.photo-container.loading::before {
  opacity: 1;
}

@keyframes spin {
  to { transform: translate(-50%, -50%) rotate(360deg); }
}

/* Улучшаем отображение информации о фото */
.photo-info {
  padding: 1rem;
  background: rgba(0, 0, 0, 0.2);
  transition: transform 0.3s;
}

.photo-card:hover .photo-info {
  transform: translateY(-5px);
}

.author {
  display: block;
  font-weight: bold;
  margin-bottom: 0.5rem;
  color: #fff;
}

.date {
  font-size: 0.9rem;
  opacity: 0.8;
  color: rgba(255, 255, 255, 0.8);
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
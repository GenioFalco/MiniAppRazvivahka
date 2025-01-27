# Развивахка - Telegram Мини-приложение

Развивающее мини-приложение для Telegram, построенное с использованием Python (FastAPI) и Vue.js.

## Структура проекта

```
├── backend/           # FastAPI backend
│   ├── app/
│   │   ├── api/      # API endpoints
│   │   ├── core/     # Конфигурация и утилиты
│   │   ├── db/       # Модели базы данных
│   │   └── services/ # Бизнес-логика
│   └── main.py       # Точка входа backend
├── frontend/         # Vue.js frontend
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   └── store/
│   └── package.json
└── docker-compose.yml
```

## Установка и запуск

### Backend

1. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Создайте файл .env в корневой директории:
```
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=sqlite:///./app.db
```

4. Запустите backend:
```bash
cd backend
uvicorn main:app --reload
```

### Frontend

1. Установите зависимости:
```bash
cd frontend
npm install
```

2. Запустите frontend в режиме разработки:
```bash
npm run serve
```

## Развертывание

1. Соберите frontend:
```bash
cd frontend
npm run build
```

2. Разверните на GitHub Pages:
- Создайте репозиторий на GitHub
- Включите GitHub Pages в настройках репозитория
- Настройте деплой через GitHub Actions

## Интеграция с Telegram

1. Создайте бота через @BotFather
2. Получите токен бота
3. Добавьте токен в .env файл
4. Настройте веб-хуки для бота

## Использование

1. Откройте бота в Telegram
2. Следуйте инструкциям бота для доступа к мини-приложению
3. Наслаждайтесь функционалом! 
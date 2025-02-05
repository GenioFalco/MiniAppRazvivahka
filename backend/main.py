from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import WebAppInfo, MenuButtonWebApp
from sqlalchemy.orm import Session
import asyncio
import logging
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from typing import List

from app.db.database import get_db, engine
from app.db.models import Base, Category, Task, User, UserProgress

# Создаем таблицы
Base.metadata.create_all(bind=engine)

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация FastAPI
app = FastAPI(
    title="Развивахка API",
    description="API для Telegram мини-приложения Развивахка",
    version="1.0.0"
)

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В продакшене заменить на конкретные домены
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Инициализация бота
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

WEBAPP_URL = "https://geniofalco.github.io/MiniAppRazvivahka"  # URL без #

@app.on_event("startup")
async def startup_event():
    """Действия при запуске приложения"""
    logger.info("Запуск приложения...")
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_webhook(url=f"{WEBAPP_URL}/webhook")
    
    # Настраиваем кнопку меню для мини-приложения
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="Открыть приложение",
            web_app=WebAppInfo(url=f"{WEBAPP_URL}")
        )
    )

@app.on_event("shutdown")
async def shutdown_event():
    """Действия при остановке приложения"""
    logger.info("Остановка приложения...")
    await bot.session.close()

@app.get("/")
async def root():
    """Корневой эндпоинт для проверки работоспособности API"""
    return {"message": "Развивахка API работает!"}

@app.get("/api/categories")
async def get_categories(db: Session = Depends(get_db)):
    """Получение списка категорий"""
    categories = db.query(Category).all()
    return categories

@app.get("/api/categories/{category_id}/tasks")
async def get_category_tasks(category_id: int, db: Session = Depends(get_db)):
    """Получение заданий для категории"""
    tasks = db.query(Task).filter(Task.category_id == category_id).all()
    if not tasks:
        raise HTTPException(status_code=404, detail="Задания не найдены")
    return tasks

@app.post("/api/tasks/{task_id}/submit")
async def submit_task(task_id: int, answer: str, user_id: int, db: Session = Depends(get_db)):
    """Отправка ответа на задание"""
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Задание не найдено")
    
    user = db.query(User).filter(User.telegram_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    
    progress = db.query(UserProgress).filter(
        UserProgress.user_id == user.id,
        UserProgress.task_id == task_id
    ).first()
    
    if not progress:
        progress = UserProgress(user_id=user.id, task_id=task_id)
        db.add(progress)
    
    progress.attempts += 1
    is_correct = answer.lower().strip() == task.correct_answer.lower().strip()
    
    if is_correct and not progress.completed:
        progress.completed = True
        progress.completed_at = datetime.utcnow()
    
    db.commit()
    
    return {
        "correct": is_correct,
        "attempts": progress.attempts,
        "completed": progress.completed
    }

@app.post("/webhook")
async def webhook(request: Request):
    """Обработчик веб-хука от Telegram"""
    update = await request.json()
    telegram_update = types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)
    return {"ok": True}

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    user_id = message.from_user.id
    db = next(get_db())
    
    # Создаем или получаем пользователя
    user = db.query(User).filter(User.telegram_id == user_id).first()
    if not user:
        user = User(
            telegram_id=user_id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name
        )
        db.add(user)
        db.commit()
    
    await message.answer(
        "Привет! Я бот Развивахка. Я помогу тебе учиться и развиваться!\n"
        "Нажми на кнопку меню внизу, чтобы открыть мини-приложение.",
        parse_mode=ParseMode.HTML,
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        text="Открыть приложение",
                        web_app=WebAppInfo(url=WEBAPP_URL)
                    )
                ]
            ]
        )
    )

@app.get("/api/photos")
async def get_photos():
    """Получение фотографий из Telegram канала"""
    try:
        # Получаем последние сообщения из канала
        channel_username = "doskadlavsex"  # Имя канала без @
        messages = []
        
        async with bot:
            async for message in bot.get_chat_history(channel_username, limit=50):
                if message.photo:
                    # Получаем информацию о фото
                    photo = message.photo[-1]  # Берем самое большое разрешение
                    photo_url = await bot.get_file_url(photo.file_id)
                    
                    messages.append({
                        "id": message.message_id,
                        "url": photo_url,
                        "author": message.from_user.username or message.from_user.first_name,
                        "date": int(message.date.timestamp()),
                        "caption": message.caption or ""
                    })
        
        return messages
    except Exception as e:
        logger.error(f"Error getting photos: {e}")
        raise HTTPException(status_code=500, detail="Error getting photos from channel")

# Запуск бота и FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 
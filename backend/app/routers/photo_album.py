from fastapi import APIRouter, HTTPException
import aiohttp
import logging
from typing import List

# Настройка логирования
logger = logging.getLogger(__name__)

router = APIRouter(
    prefix="/api/photos",
    tags=["photos"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_photos():
    """Получение фотографий из публичной папки Яндекс.Диска"""
    try:
        # Публичная ссылка на папку
        PUBLIC_FOLDER_URL = 'https://disk.yandex.ru/d/odb9rYQBjq_1Cw'
        
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://cloud-api.yandex.net/v1/disk/public/resources",
                params={
                    "public_key": PUBLIC_FOLDER_URL,
                    "limit": 100,
                    "preview_size": "L"
                },
                headers={
                    "Accept": "application/json"
                }
            ) as response:
                if response.status != 200:
                    raise HTTPException(status_code=500, detail="Ошибка при получении списка фотографий")
                
                data = await response.json()
                
                # Фильтруем и преобразуем данные
                photos = [
                    {
                        "id": item["resource_id"],
                        "url": item["file"],
                        "author": item["name"].split('.')[0],
                        "date": item["created"]
                    }
                    for item in data["_embedded"]["items"]
                    if item["type"] == "file" and item["mime_type"].startswith("image/")
                ]
                
                return photos

    except Exception as e:
        logger.error(f"Error getting photos: {e}")
        raise HTTPException(status_code=500, detail="Ошибка при получении фотографий") 
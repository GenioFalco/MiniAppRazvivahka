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
                    "preview_size": "XL",
                    "preview_crop": False
                },
                headers={
                    "Accept": "application/json"
                }
            ) as response:
                if response.status != 200:
                    logger.error(f"Yandex.Disk API error: {response.status}")
                    raise HTTPException(status_code=500, detail="Ошибка при получении списка фотографий")
                
                data = await response.json()
                
                # Проверяем корректность структуры данных
                if "_embedded" not in data or "items" not in data["_embedded"]:
                    logger.error("Некорректный формат данных от Yandex.Диск API")
                    raise HTTPException(status_code=500, detail="Некорректный формат данных от Yandex.Диск API")

                # Фильтруем и преобразуем данные
                photos = [
                    {
                        "id": item.get("resource_id"),
                        "url": item.get("preview"),  # Используем preview вместо file
                        "author": item.get("name", "").split('.')[0],
                        "date": item.get("created")
                    }
                    for item in data["_embedded"]["items"]
                    if item.get("type") == "file" and 
                       item.get("mime_type", "").startswith("image/") and
                       "preview" in item
                ]
                
                return photos

    except Exception as e:
        logger.error(f"Error getting photos: {e}")
        raise HTTPException(status_code=500, detail="Ошибка при получении фотографий") 
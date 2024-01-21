"""
Пример добавления и скачивания видео
"""
from utils.manager import AuthenticationManager
from config import USER, PASSWORD, HOST, PORT, DATABASE

connection_url = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

auth_manager = AuthenticationManager(connection_url)

mail = "user_test@example.com"
password = "password123"

auth_manager.authenticate_user(mail, password)

# Добавление видео
source_video_path = "../videos/Тренировка.mp4"

try:
    video_id = auth_manager.add_video("Пример Видео", source_video_path, 40)
    print(f"Видео с ID {video_id} добавлено.")
except Exception as e:
    print(f"Ошибка: {e}")
else:
    # Получение пути к видео
    try:
        video_path = auth_manager.get_video_path(video_id)
        print(f"Путь к видео: {video_path}")
    except Exception as e:
        print(f"Ошибка: {e}")

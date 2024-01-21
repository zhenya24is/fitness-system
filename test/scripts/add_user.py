"""
Пример добавления пользователя
"""
from utils.manager import AuthenticationManager
from config import USER, PASSWORD, HOST, PORT, DATABASE

from utils.models import User

connection_url = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

auth_manager = AuthenticationManager(connection_url)
mail = "user_test@example.com"
password = "password123"

# Добавление пользователя
try:
    new_user = auth_manager.register_user(mail, password)
    print(f"Пользователь с ID {new_user} добавлен.")
except Exception as e:
    print(f"Ошибка: {e}")


# Поиск и вывод пользователя
session = auth_manager.session_factory()
user = session.query(User).filter_by(email=mail).first()
if user:
    print(f"Найден: {user.email}")
else:
    print("Не найден.")

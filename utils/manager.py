#manager.py
import datetime

from PyQt5.QtCore import QDate
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.models import User, TrainingVideo, TrainingSession
from config import VIDEOS_FOLDER, USER, PASSWORD, HOST, PORT, DATABASE


class AuthenticationManager:
    """
    Класс для управления аутентификацией и авторизацией пользователей,
    а также для управления видео в системе.
    """

    connection_url = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

    def __init__(self, db_url: str = connection_url):
        self.engine = self._create_engine(db_url)
        self.session_factory = sessionmaker(bind=self.engine)
        self.current_user = None

    def _create_engine(self, db_url):
        return create_engine(db_url)

    def register_user(self, email, password):
        """
        Регистрирует нового пользователя с заданным email и паролем.

        :param email: Email пользователя.
        :param password: Пароль пользователя.
        :return: ID зарегистрированного пользователя.
        :raises: Exception, если регистрация не удалась.
        """
        session = self.session_factory()
        new_user = User(email=email)
        new_user.set_password(password)
        session.add(new_user)
        try:
            session.commit()
            return new_user.id
        except Exception as e:
            session.rollback()
            raise e

    def authenticate_user(self, email, password):
        """
        Аутентифицирует пользователя по email и паролю.

        :param email: Email пользователя.
        :param password: Пароль пользователя.
        :return: True, если аутентификация успешна, иначе False.
        """
        session = self.session_factory()
        user = session.query(User).filter_by(email=email).first()
        if user and user.check_password(password):
            self.current_user = user
            return True
        return False

    def change_password(self, old_password, new_password):
        """
        Изменяет пароль текущего аутентифицированного пользователя.

        :param old_password: Старый пароль.
        :param new_password: Новый пароль.
        :return: True, если изменение пароля успешно, иначе False.
        :raises: Exception, если пользователь не аутентифицирован.
        """

        # Если пользователь аутентифицирован, и пароль верный
        if self.current_user and self.current_user.check_password(old_password):
            # Устанавливаем новый пароль
            self.current_user.set_password(new_password)
            session = self.session_factory()
            session.add(self.current_user)
            session.commit()
            return True
        return False

    def add_video(self, title, source_path, duration):
        """
        Добавляет видео в систему, копируя его файл в указанную папку и создавая запись в базе данных.

        :param title:       Название видео.
        :param source_path: Путь к исходному файлу видео.
        :param duration:    Длительность видео

        :return: ID добавленного видео.
        :raises: Exception, если пользователь не аутентифицирован или произошла ошибка при копировании файла.
        """

        # Добавление информации о видео в БД
        session = self.session_factory()
        new_video = TrainingVideo(title=title, video_url=source_path, duration=duration)
        session.add(new_video)
        session.commit()
        return new_video.id

    def get_video_path(self, day):
        """
        Возвращает путь к видео по его идентификатору.

        :param video_id: ID видео.
        :return: Путь к файлу видео.
        :raises: Exception, если видео не найдено.
        """
        """Возвращает путь к видео по его ID."""
        session = self.session_factory()
        videos = session.query(TrainingVideo)
        result_list = []
        for video in videos:
            if video.title == day:
                result_list.append(video.video_url)
        return result_list

    def add_train(self, id, date, train_id):
        """
        Добавляет тренировку в систему.
        :param id: id пользователя.
        :param date: Дата тренировки.
        :return: ID добавленной тренировки.
        :raises: Exception, если пользователь не аутентифицирован или произошла ошибка при подключении к базе.
        """
        session = self.session_factory()
        new_train = TrainingSession(user_id=id, session_date=date, video_id=train_id)
        session.add(new_train)
        session.commit()
        return new_train.id

    def get_emails(self):
        """
        Возвращает все email пользователей.
        :return: list_emails зарегистрированные аккаунты.
        :raises: Exception, если пользователь не аутентифицирован или произошла ошибка при подключении к базе.
        """
        session = self.session_factory()
        list_emails = []
        users = session.query(User)
        for user in users:
            list_emails.append(user.email)
        return list_emails

    def get_trains_on_day(self, day):
        """
        Возвращает все доступные тренировки на день.
        :return: list_path_trains список доступных тренировок на день.
        :raises: Exception, если пользователь не аутентифицирован или произошла ошибка при подключении к базе.
        """
        session = self.session_factory()
        list_path_trains = []
        trains = session.query(TrainingVideo).filter(TrainingVideo.title == day)
        for train in trains:
            list_path_trains.append(train.video_url)
        return list_path_trains

    def get_id_train(self, path):
        """
        Возвращает id тренировки по названию пути.
        :return: path_train  путь до видео с тренировкой
        :raises: Exception, если пользователь не аутентифицирован или произошла ошибка при подключении к базе.
        """
        session = self.session_factory()
        trains = session.query(TrainingVideo).filter(TrainingVideo.video_url == path)
        for train in trains:
            return train.id

    def get_id_trains_current_week(self):
        """
        Возвращает id всех тренировок за неделю.
        :return: list_id  путь до видео с тренировкой
        :raises: Exception, если пользователь не аутентифицирован или произошла ошибка при подключении к базе.
        """
        try:
            list_id = []
            session = self.session_factory()
            trains = session.query(TrainingSession).where(
                TrainingSession.user_id == self.current_user.id
            )
            today = QDate(datetime.date.today()).weekNumber()
            for train in trains:
                date_train = QDate(train.session_date).weekNumber()
                if today[0] == date_train[0] and today[1] == date_train[1]:
                    list_id.append(train.video_id)
            return list_id
        except Exception as err:
            raise err

    def get_duration_train(self, id):
        """
        Возвращает время тренировки.
        :return: duration  время тренировки
        :raises: Exception, если пользователь не аутентифицирован или произошла ошибка при подключении к базе.
        """
        session = self.session_factory()
        trains = session.query(TrainingVideo).filter(TrainingVideo.id == id)
        for train in trains:
            return train.duration

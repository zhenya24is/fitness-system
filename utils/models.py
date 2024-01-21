#models.py
# -*- coding: utf-8 -*-

import re

from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base, validates
from sqlalchemy_utils import database_exists, create_database

from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String(512))

    @validates('email')
    def validate_email(self, key, email):
        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Некорректный адрес электронной почты")
        return email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    training_sessions = relationship("TrainingSession", back_populates="user")


class TrainingVideo(Base):
    __tablename__ = "training_videos"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    video_url = Column(String, nullable=False)
    duration = Column(Integer)

    training_sessions = relationship("TrainingSession", back_populates="training_video")


class TrainingSession(Base):
    __tablename__ = "training_sessions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    video_id = Column(Integer, ForeignKey("training_videos.id"))
    session_date = Column(Date, nullable=False)

    user = relationship("User", back_populates="training_sessions")
    training_video = relationship("TrainingVideo", back_populates="training_sessions")


if __name__ == "__main__":
    from config import USER, PASSWORD, HOST, PORT, DATABASE

    # Подключение к PostgreSQL
    connection_url = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

    engine = create_engine(connection_url)

    Base.metadata.drop_all(engine)

    # Если базы нет, создадим
    if not database_exists(connection_url):
        print(f"Создание базы {DATABASE}")
        create_database(connection_url)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Добавление пользователя root
    root_user = User(email='root@example.com')
    root_user.set_password('root')
    session.add(root_user)

    # Подтверждение транзакции
    session.commit()
    session.close()

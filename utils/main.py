#main.py
import sqlalchemy.exc

from ui.enter_window import Ui_enter_window
from ui.reg_window import Ui_RegWindow
from ui.app_window import Ui_AppWindow
from ui.add_video_window import Ui_AddVideoWindows
from manager import AuthenticationManager
from moviepy.editor import VideoFileClip

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
import sys

# Переменная для подключения к аутентификационному менеджеру
global connection
connection = AuthenticationManager()


class EnterWindow(QtWidgets.QMainWindow):
    """
    Окно входа в приложение
    """
    def __init__(self):
        super(EnterWindow, self).__init__()
        # Создание объекта Ui_enter_window
        self.ui = Ui_enter_window()
        # Настройка пользовательского интерфейса
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        # Настройка кнопок закрытия и сворачивания окна
        self.ui.exit.setIcon(QtGui.QIcon("icons/close.png"))
        self.ui.exit.setStyleSheet("text-align: center")
        self.ui.exit.clicked.connect(self.close)
        self.ui.min.setIcon(QtGui.QIcon("icons/minimize-sign.png"))
        self.ui.min.setStyleSheet("text-align: center")
        self.ui.min.clicked.connect(self.showMinimized)

    def check(self):
        """
        Функция для проверки входа и регистрации пользователя
        """
        self.show()
        self.ui.b_reg.clicked.connect(self.call_reg)
        self.ui.b_reg.clicked.connect(self.close)
        self.ui.b_enter.clicked.connect(self.call_enter)
        self.ui.b_enter.clicked.connect(self.close)

    def call_reg(self):
        """
        Вызов регистрации
        """
        self.reg_user = RegWindow()
        self.reg_user.reg_user()

    def call_enter(self):
        """
        Проверка ввода формы
        """
        email = self.ui.lineEdit_email.text()
        password = self.ui.lineEdit_password.text()

        # Проверка
        if email.replace(" ", "") == "" or password.replace(" ", "") == "":
            QtWidgets.QMessageBox.critical(
                self,
                "Ошибка",
                "Email и/или пароль не могут быть пустыми",
                QtWidgets.QMessageBox.Ok,
            )
            self.back = EnterWindow()
            self.back.check()
            return
        try:
            result = connection.authenticate_user(email, password)
        except sqlalchemy.exc.OperationalError:
            QtWidgets.QMessageBox.critical(
                self, "Ошибка", "Не удается подключиться к базе", QtWidgets.QMessageBox.Ok
            )
            return
        except Exception as error:
            QtWidgets.QMessageBox.critical(
                self, "Ошибка", "Непредвиденная ошибка", QtWidgets.QMessageBox.Ok
            )
            return

        if result is not True:
            QtWidgets.QMessageBox.critical(
                self, "Ошибка", "Неверный логин или пароль", QtWidgets.QMessageBox.Ok
            )
            self.back = EnterWindow()
            self.back.check()
            return
        else:

            # Проверяем, что это root-пользователь
            if email == 'root@example.com':
                self.add_window = AddVideoWindow()
                self.add_window.check()
            else:
                self.app_window = AppWindow()
                self.app_window.check()


class RegWindow(QtWidgets.QWidget):
    def __init__(self):
        super(RegWindow, self).__init__()
        # Создание объекта Ui_RegWindow
        self.ui = Ui_RegWindow()
        # Настройка пользовательского интерфейса
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # Установка иконки для кнопки закрытия и сворачивания окна
        self.ui.exit.setIcon(QtGui.QIcon("icons/close.png"))
        self.ui.exit.setStyleSheet("text-align: center")
        self.ui.exit.clicked.connect(self.close)
        self.ui.min.setIcon(QtGui.QIcon("icons/minimize-sign.png"))
        self.ui.min.setStyleSheet("text-align: center")
        self.ui.min.clicked.connect(self.showMinimized)

    def reg_user(self):
        self.show()
        self.ui.b_back.clicked.connect(self.call_back)
        self.ui.b_back.clicked.connect(self.close)
        self.ui.b_reg.clicked.connect(self.call_reg)
        self.ui.b_reg.clicked.connect(self.close)

    def call_back(self):
        self.enter_window = EnterWindow()
        self.enter_window.check()

    def call_reg(self):
        email = self.ui.lineEdit_email.text()
        password = self.ui.lineEdit_password.text()
        if email.replace(" ", "") == "" or password.replace(" ", "") == "":
            QtWidgets.QMessageBox.critical(
                self,
                "Ошибка",
                "Email и/или пароль не может быть быть пустым",
                QtWidgets.QMessageBox.Ok,
            )
            self.back = RegWindow()
            self.back.reg_user()
            return
        global connection

        try:
            emails = connection.get_emails()
        except Exception as error:
            QtWidgets.QMessageBox.critical(
                self, "Ошибка", "Нет соединения с базой", QtWidgets.QMessageBox.Ok
            )
            return
        if email in emails:
            QtWidgets.QMessageBox.critical(
                self,
                "Ошибка",
                "Такой пользователь уже существует",
                QtWidgets.QMessageBox.Ok,
            )
            self.back = RegWindow()
            self.back.reg_user()
            return
        try:
            connection.register_user(email, password)
            QtWidgets.QMessageBox.information(
                self, "Успех", "Пользователь зарегистрирован", QtWidgets.QMessageBox.Ok
            )
        except ValueError:
            QtWidgets.QMessageBox.critical(
                self, "Ошибка", "Некорректный email", QtWidgets.QMessageBox.Ok
            )
        except Exception:
            QtWidgets.QMessageBox.critical(
                self, "Ошибка", "Нет соединения с базой", QtWidgets.QMessageBox.Ok
            )
        else:
            self.enter_window = EnterWindow()
            self.enter_window.check()
            return
        finally:
            self.back = RegWindow()
            self.back.reg_user()
            return


class AppWindow(QtWidgets.QWidget):
    def __init__(self):
        super(AppWindow, self).__init__()
        # Инициализация и настройка пользовательского интерфейса для основного окна приложения
        self.ui = Ui_AppWindow()
        self.ui.setupUi(self)
        # Установка стиля окна без рамок
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Настройка действий для кнопок закрытия и сворачивания окна
        self.ui.exit.setIcon(QtGui.QIcon("icons/close.png"))
        self.ui.exit.setStyleSheet("text-align: center")
        self.ui.exit.clicked.connect(self.close)
        self.ui.min.setIcon(QtGui.QIcon("icons/minimize-sign.png"))
        self.ui.min.setStyleSheet("text-align: center")
        self.ui.min.clicked.connect(self.showMinimized)

    def check(self):
        self.show()
        # Получение и обработка статистики тренировок на текущей неделе
        list_trains = connection.get_id_trains_current_week()
        total_seconds = sum(int(connection.get_duration_train(id)) for id in list_trains)

        # Конвертация секунд в часы, минуты и секунды
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Отображение статистики на пользовательском интерфейсе
        self.ui.lable_stat.setText(
            f"Количество времени тренировок на текущей недели: {hours} часов {minutes} минут {seconds} секунд"
        )

        # Настройка действий для кнопок управления тренировками
        self.ui.b_train.clicked.connect(self.train)
        self.ui.calendarWidget.clicked.connect(self.change)
        self.ui.b_exit.clicked.connect(self.back)
        self.ui.b_exit.clicked.connect(self.close)

    def back(self):
        # Возвращение к окну входа
        self.back = EnterWindow()
        self.back.check()

    def change(self):
        # Обработка выбора даты в календаре и обновление списка тренировок
        day_of_week = self.ui.calendarWidget.selectedDate().dayOfWeek()
        dict_days = {
            1: "Понедельник", 2: "Вторник", 3: "Среда",
            4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"
        }
        selected_day = dict_days[day_of_week]
        trains = connection.get_video_path(selected_day)

        # Обновление выпадающего списка тренировок
        self.ui.comboBox_train.clear()
        if trains:
            self.ui.comboBox_train.addItems(trains)
        else:
            QtWidgets.QMessageBox.information(
                self, "Внимание", "На этот день тренировок нет!", QtWidgets.QMessageBox.Ok
            )

    def train(self):
        # Запуск тренировки, выбранной из выпадающего списка
        selected_train = self.ui.comboBox_train.currentText()
        if not selected_train:
            QtWidgets.QMessageBox.critical(self, "Ошибка",
                                           "Тренировка не выбрана",
                                           QtWidgets.QMessageBox.Ok)
        else:
            self.ui.video_train.choice(self.ui.comboBox_train.currentText())
            try:
                id_train = connection.get_id_train(self.ui.comboBox_train.currentText())
                connection.add_train(
                    connection.current_user.id,
                    str(self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")),
                    id_train,
                )
                QtWidgets.QMessageBox.information(
                    self, "Внимание", "Тренировка началась", QtWidgets.QMessageBox.Ok
                )
                self.check()
            except Exception as err:
                raise err


class AddVideoWindow(QtWidgets.QWidget):
    def __init__(self):
        super(AddVideoWindow, self).__init__()
        self.ui = Ui_AddVideoWindows()
        # Настройка пользовательского интерфейса для окна добавления видео
        self.ui.setupUi(self)
        # Установка стиля окна без рамок
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Установка иконок и действий для кнопок закрытия и сворачивания окна
        self.ui.exit.setIcon(QtGui.QIcon("icons/close.png"))
        self.ui.exit.setStyleSheet("text-align: center")
        self.ui.exit.clicked.connect(self.close)
        self.ui.min.setIcon(QtGui.QIcon("icons/minimize-sign.png"))
        self.ui.min.setStyleSheet("text-align: center")
        self.ui.min.clicked.connect(self.showMinimized)

    def check(self):
        # Отображение окна и настройка обработчиков событий кнопок
        self.show()
        self.ui.b_choice_video.clicked.connect(self.choice)
        self.ui.b_back.clicked.connect(self.call_back)
        self.ui.b_back.clicked.connect(self.close)
        self.ui.b_add.clicked.connect(self.add)

    def choice(self):
        # Выбор видео файла через диалоговое окно
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Selecciona los mediose",
            ".",
            "Video Files (*.mp4 *.flv *.ts *.mts *.avi)",
        )
        # Отображение выбранного пути файла в метке
        self.ui.label_choice.setText(fileName)

    def call_back(self):
        # Возвращение к предыдущему окну
        self.back = EnterWindow()
        self.back.check()

    def add(self):
        # Добавление выбранного видео
        path = self.ui.label_choice.text()
        day = self.ui.cb_day.currentText()
        if not path:
            QtWidgets.QMessageBox.critical(
                self, "Ошибка", "Видео не выбрано", QtWidgets.QMessageBox.Ok
            )
            return
        # Проверка на существование видео для выбранного дня
        exists_trains = connection.get_trains_on_day(day=day)
        if path in exists_trains:
            QtWidgets.QMessageBox.critical(
                self,
                "Ошибка",
                "Видео для этого дня уже в системе",
                QtWidgets.QMessageBox.Ok,
            )
            return
        try:
            # Получение длительности видео и добавление в базу данных
            clip = VideoFileClip(path)
            connection.add_video(day, path, clip.duration)
            QtWidgets.QMessageBox.information(
                self, "Успех", "Видео добавлено", QtWidgets.QMessageBox.Ok
            )
        except Exception as err:
            print(err)
            QtWidgets.QMessageBox.critical(
                self, "Ошибка", "Нет соединения с базой", QtWidgets.QMessageBox.Ok
            )


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = EnterWindow()
    window.check()  # Проверяем не нажато ли чего
    sys.exit(app.exec())

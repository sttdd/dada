import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from db import Connect, User  # Импортируем класс Connect и модель User

class MainWindow(QMainWindow):
    def __init__(self): #конструктор класса 
        super().__init__() #вызов методов базавого класса

        # Установка заголовка окна и его размера
        self.setWindowTitle("Главное окно с таблицей")
        self.setGeometry(100, 100, 800, 400)

        # Создание таблицы
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(["ID", "ФИО", "Email", "Телефон", "Должность", "Дата создания"])

        # Заполнение таблицы данными из базы данных
        self.load_data_from_db()

        # Установка вертикального макета
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget) #добавление таблицы в макет 

        # Создание виджета-контейнера и установка макета
        container = QWidget()
        container.setLayout(layout) #устанавливаем макет в контейнер
        self.setCentralWidget(container) #устанавливаем как центральный виджет главного окна

    def load_data_from_db(self):
        session = Connect.create_connection() # Создание сессии через класс Connect
        users = session.query(User).all() # Получаем данные пользователей из базы данных
        session.close() # Закрытие сессии после выполнения запроса
        self.table_widget.setRowCount(len(users)) # Установка количества строк в таблице в зависимости от количества пользователей

        # Заполнение таблицы данными пользователей
        for row, user in enumerate(users): #генерация последовательности пар
            self.table_widget.setItem(row, 0, QTableWidgetItem(str(user.id))) #название как в бд
            self.table_widget.setItem(row, 1, QTableWidgetItem(user.full_name)) #название как в бд
            self.table_widget.setItem(row, 2, QTableWidgetItem(user.email)) #название как в бд
            self.table_widget.setItem(row, 3, QTableWidgetItem(user.phone_number)) #название как в бд
            self.table_widget.setItem(row, 4, QTableWidgetItem(str(user.dol_id))) #название как в бд
            self.table_widget.setItem(row, 5, QTableWidgetItem(str(user.created_at))) #название как в бд

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

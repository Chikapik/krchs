import re
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from login_window import Ui_LoginForm
from main_window import Ui_MainWindow
import sqlite3
import bcrypt


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.number_in_decimal = 0
        self.letters = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20,
                   'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31,
                   'W': 32, 'X': 33, 'Y': 34, 'Z': 35}

        self.convertButton.clicked.connect(self.convert_to_decimal_calculation_system)

    def convert_to_decimal_calculation_system(self):
        number = self.numberEdit.text().upper()
        number_length = len(number)
        is_entry_correct = True
        self.number_in_decimal = 0

        for i in range(number_length):
            if number[i].isdigit():
                if int(number[i]) > int(self.spinBox_1.text()) - 1:
                    is_entry_correct = False
                    break
            else:
                if self.letters[number[i]] > int(self.spinBox_1.text()) - 1:
                    is_entry_correct = False
                    break

        if is_entry_correct:
            for i in range(number_length):
                number_length -= 1
                if number[i].isdigit():
                    self.number_in_decimal += int(number[i]) * int(self.spinBox_1.text()) ** number_length
                else:
                    self.number_in_decimal += self.letters[number[i]] * int(self.spinBox_1.text()) ** number_length
            self.convert_to_another_calculation_system()
        else:
            self.answerLabel.setText('Указанное число содержит недопустимые для исходной системы счисления символы.')

    def convert_to_another_calculation_system(self):
        number_in_another = ''

        while self.number_in_decimal != 0:
            temp_calculation = self.number_in_decimal % int(self.spinBox_2.text())
            if temp_calculation > 9:
                number_in_another += str(self.get_key(temp_calculation))
            else:
                number_in_another += str(temp_calculation)
            self.number_in_decimal //= int(self.spinBox_2.text())

        self.answerLabel.setText(f'Ответ: {number_in_another[::-1]}')

    def get_key(self, value):
        for k, v in self.letters.items():
            if v == value:
                return k


class LoginForm(QMainWindow, Ui_LoginForm):
    def __init__(self):
        super().__init__()
        self.main_window = None
        self.setupUi(self)

        self.login.clicked.connect(self.login_clicked)
        self.registration.clicked.connect(self.registration_clicked)

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()

    def login_clicked(self):
        username = self.loginEdit.text()
        password = self.passwordEdit.text()

        if not username or not password:
            self.label.setText("Введите логин и пароль для входа")
        else:
            conn = sqlite3.connect("../../Desktop/IraKursach/users.db")
            cursor = conn.cursor()

            cursor.execute("SELECT password FROM users WHERE username=?", (username,))
            user_data = cursor.fetchone()
            conn.close()

            if user_data and bcrypt.checkpw(password.encode('utf-8'), user_data[0]):
                self.close()
                self.open_main_window()
            else:
                self.label.setText("Не верно введен логин или пароль")
                self.passwordEdit.clear()

    def registration_clicked(self):
        username = self.loginEdit.text()
        password = self.passwordEdit.text()

        if not username or not password:
            self.label.setText("Введите логин и пароль для создания нового аккаунта")
        else:
            conn = sqlite3.connect("../../Desktop/IraKursach/users.db")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM users WHERE username=?", (username,))
            existing_user = cursor.fetchone()

            if existing_user:
                self.label.setText("Пользователь с таким логином уже существует")
            else:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
                conn.commit()
                conn.close()

                self.label.setText("Новый аккаунт успешно создан")

            self.loginEdit.clear()
            self.passwordEdit.clear()


if __name__ == '__main__':
    conn = sqlite3.connect("../../Desktop/IraKursach/users.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          username TEXT NOT NULL,
                          password TEXT NOT NULL)''')

    conn.commit()
    conn.close()

    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec_())

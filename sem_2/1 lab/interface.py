import warnings
from Convert import test_input_data, convert10to3, convert3to10
from sys import argv, exit
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt6.QtWidgets import QLCDNumber, QLabel, QMainWindow

warnings.filterwarnings('ignore')


class Calculator_Interface(QMainWindow):
    """class with frontend"""

    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)
        self.initUI()
        self.binding_keys()
        self.status = 0

    def initUI(self):
        """base settings"""
        self.setFixedSize(400, 620)
        self.setWindowTitle('Calculator')
        self.Status.setText('10 -> 3')

    def binding_keys(self):
        '''Binding Buttons'''
        self.AuthorMenu.triggered.connect(self.show_author_info)
        self.ClearMenu.triggered.connect(self.clear_monitor)

        self.PoundButton.clicked.connect(self.button_input)
        self.Button0.clicked.connect(self.button_input)
        self.Button1.clicked.connect(self.button_input)
        self.Button2.clicked.connect(self.button_input)
        self.Button3.clicked.connect(self.button_input)
        self.Button4.clicked.connect(self.button_input)
        self.Button5.clicked.connect(self.button_input)
        self.Button6.clicked.connect(self.button_input)
        self.Button7.clicked.connect(self.button_input)
        self.Button8.clicked.connect(self.button_input)
        self.Button9.clicked.connect(self.button_input)

        self.Mode0.clicked.connect(self.choose_mode)
        self.Mode1.clicked.connect(self.choose_mode)

        self.Convert.clicked.connect(self.convert)
        self.ClearButton.clicked.connect(self.clear_last)

    def button_input(self):
        """Считывание клавиш"""
        # self.label.setText(self.sender().text())
        text = self.sender().text()
        text_on_monitor = self.Monitor.text()
        self.Monitor.setText(text_on_monitor + text)

    def show_author_info(self):
        '''Вывод информации об авторе'''
        author_info = "Выполнил Попов Ю.А. ИУ7-22Б"
        QMessageBox.information(self, 'Об авторе', author_info)

    def clear_monitor(self):
        self.Monitor.setText('')

    def clear_last(self):
        """Clear last symbol in monitor"""
        text = self.Monitor.text()
        text = text[:-1]
        self.Monitor.setText(text)

    def choose_mode(self):
        """Func change calculator mode"""
        text = self.sender().text()
        if text == '10 -> 3':
            self.status = 0
        elif text == '3 -> 10':
            self.status = 1

        if self.status == 0:
            self.Button3.setEnabled(True)
            self.Button4.setEnabled(True)
            self.Button5.setEnabled(True)
            self.Button6.setEnabled(True)
            self.Button7.setEnabled(True)
            self.Button8.setEnabled(True)
            self.Button9.setEnabled(True)
            self.Status.setText('10 -> 3')
        elif self.status == 1:
            self.Button3.setEnabled(False)
            self.Button4.setEnabled(False)
            self.Button5.setEnabled(False)
            self.Button6.setEnabled(False)
            self.Button7.setEnabled(False)
            self.Button8.setEnabled(False)
            self.Button9.setEnabled(False)
            self.Status.setText('3 -> 10')

    def convert(self):
        """main func, that bind to convert button and validate data"""
        number = self.Monitor.text()
        test_result = test_input_data(number, self.status)
        if float(number) > 10 ** 60:
            self.Status2.setText('Слишком большое число')
            test_result = ''
        if test_result == 'letters in number':
            self.Status2.setText('letters in number')
            self.clear_monitor()
        elif test_result == '':
            pass
        elif test_result == 'too match pounds':
            self.Status2.setText('too match pounds')
            self.clear_monitor()
        elif test_result == 'incorrect digits for 3cc':
            self.Status2.setText('incorrect digits for 3cc')
        elif test_result == '1':
            self.Status2.setText('')
            if self.status == 0:
                result = convert10to3(number, precision=6)
                self.Monitor.setText(result)
            elif self.status == 1:
                result = convert3to10(number, precision=6)
                self.Monitor.setText(result)
            else:
                print('Что-то пошло не так')
        else:
            print('INCORRECT')
            self.Status2.setText('INCORRECT')


if __name__ == '__main__':
    app = QApplication(argv)
    calc = Calculator_Interface()
    calc.show()
    exit(app.exec())

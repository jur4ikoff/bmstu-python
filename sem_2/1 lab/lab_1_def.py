import warnings
from Convert import test_input_data, convert10to3, convert3to10
from sys import argv, exit
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QRadioButton
from PyQt6.QtWidgets import QLCDNumber, QLabel, QMainWindow
import sys

warnings.filterwarnings('ignore')


class Interface(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('calc_def.ui', self)
        self.initUI()
        self.binding_keys()
        self.check_radio()
        self.Output.setEnabled(False)

    def initUI(self):
        self.setFixedSize(400, 620)
        self.setWindowTitle('Resistor calculator')
        self.Status.setText('Последовательно')

    def show_author_info(self):
        '''Вывод информации об авторе'''
        author_info = "Выполнил Попов Ю.А. ИУ7-22Б"
        QMessageBox.information(self, 'Об авторе', author_info)

    def check_radio(self):
        self.status = 0
        if self.radio_button1.isChecked():
            self.status = 0
            self.Status.setText('Последовательно')
        elif self.radio_button2.isChecked():
            self.status = 1
            self.Status.setText('Параллельно')

    def binding_keys(self):
        self.Convert.clicked.connect(self.convert)
        self.AuthorMenu.triggered.connect(self.show_author_info)

    def convert(self):
        self.check_radio()
        r1 = self.Input1.text()
        r2 = self.Input2.text()

        if self.validate(r1) and self.validate(r2):
            r1 = float(r1)
            r2 = float(r2)

        else:
            self.Status.setText('Ошибка в веденных данных')
            return

        if self.status == 0:
            r3 = self.posl(r1, r2)
            self.Output.setText(str(r3))
            self.Status.setText('Последовательно')
        elif self.status == 1:
            r3 = self.paral(r1, r2)
            self.Output.setText(str(r3))
            self.Status.setText('Параллельно')

    def validate(self, value):
        if isinstance(value, (int, float)):
            return True
        elif isinstance(value, str) and value.isdigit():
            return True
        else:
            return False

    def posl(self, r1, r2):
        return r1 + r2

    def paral(self, r1, r2):
        r3 = (r1 * r2) / (r1 + r2)
        return r3


if __name__ == "__main__":
    app = QApplication(argv)
    calc = Interface()
    calc.show()
    exit(app.exec())

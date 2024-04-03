import warnings
from backend import calculate
from sys import argv, exit
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox, QDialog, QVBoxLayout
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget

warnings.filterwarnings('ignore')


class TableDialog(QDialog):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle('Таблица')
        self.setLayout(QVBoxLayout())

        table_widget = QTableWidget()
        table_widget.setColumnCount(6)
        table_widget.setHorizontalHeaderLabels(['Номер', 'Интервал', 'x', 'f(x)', 'Итерации', 'Код ошибки'])

        for row, row_data in enumerate(data):
            table_widget.insertRow(row)
            for col, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                table_widget.setItem(row, col, item)

        self.layout().addWidget(table_widget)


class MainWindow(QMainWindow):
    """class with frontend"""

    def __init__(self):
        super().__init__()
        uic.loadUi('second.ui', self)
        self.initUI()
        self.binding_keys()

    def initUI(self):
        """base settings"""
        self.setFixedSize(660, 780)
        self.setWindowTitle('secant_method')

    def binding_keys(self):
        '''Binding Buttons'''
        self.AuthorMenu.triggered.connect(self.show_author_info)
        self.ConvertButton.clicked.connect(self.convert)

    def button_input(self):
        """Считывание клавиш"""
        text = self.sender().text()
        text_on_monitor = self.Monitor.text()
        self.Monitor.setText(text_on_monitor + text)

    def show_author_info(self):
        '''Вывод информации об авторе'''
        author_info = "Выполнил Попов Ю.А. ИУ7-22Б"
        QMessageBox.information(self, 'Об авторе', author_info)

    def validate(self, string) -> float:
        if string:
            try:
                float(string)
            except Exception as e:
                print(e)
                return False
        else:
            return False
        return True

    def convert(self):
        f = self.Func.text()
        a = self.aLabel.text()
        b = self.bLabel.text()
        h = self.hLabel.text()
        eps = self.epsLabel.text()
        n_max = self.nLabel.text()

        a1, b1, h1, eps1, n_max1 = self.validate(a), self.validate(b), self.validate(h), self.validate(
            eps), self.validate(
            n_max)
        try:
            func = lambda x: eval(f)
        except Exception as e:
            print(e)
            self.statusLabel.setText("Wrong Function")

        flag = False
        if a1 and b1 and h1 and eps1 and n_max1:
            flag = True
            a = float(a)
            b = float(b)
            h = float(h)
            eps = float(eps)
            n_max = float(n_max)
            if abs(b - a) < h:
                self.statusLabel.setText("b - a must be bigger then step")
                flag = False
                pass
            if h <= 0 or eps <= 0 or n_max <= 0:
                self.statusLabel.setText("h, eps, n_max must be Positive")
                flag = False
        else:
            self.statusLabel.setText("Wrong Input")

        if flag:
            try:
                result = calculate(func, a, b, h, eps, n_max)

                data = [
                    [1, 'интервал1', 'x1', 'y1', 'количество итераций', 'код1'],

                ]
                data += result
                self.statusLabel.setText("")
                table_dialog = TableDialog(data)
                table_dialog.exec()
            except Exception as e:
                print(e)
                self.statusLabel.setText("Something went wrong")


if __name__ == '__main__':
    app = QApplication(argv)
    mn = MainWindow()
    mn.show()
    exit(app.exec())

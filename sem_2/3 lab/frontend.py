import warnings
# from backend import calculate
from sys import argv, exit
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox, QDialog, QVBoxLayout
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget
from PyQt6.QtGui import QPixmap

warnings.filterwarnings('ignore')

WEIGHT, HEIGHT = 800, 560


class MainWindow(QMainWindow):
    """class with frontend"""

    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        self.initUI()
        self.binding_keys()
        self.load_picture()

    def initUI(self):
        """base settings"""
        self.setFixedSize(WEIGHT, HEIGHT)
        self.setWindowTitle('Стеганография')

    def binding_keys(self):
        '''Binding Buttons'''
        self.AuthorMenu.triggered.connect(self.show_author_info)
        # self.ConvertButton.clicked.connect(self.convert)

    def button_input(self):
        """Считывание клавиш"""
        text = self.sender().text()
        text_on_monitor = self.Monitor.text()
        self.Monitor.setText(text_on_monitor + text)

    def show_author_info(self):
        '''Вывод информации об авторе'''
        author_info = "Выполнил Попов Ю.А. ИУ7-22Б"
        QMessageBox.information(self, 'Об авторе', author_info)

    def load_picture(self):
        pixmap = QPixmap('image.bmp')  # Укажите путь к изображению
        scaled_pixmap = pixmap.scaled(640, 360)
        label = self.showImage
        label.setPixmap(pixmap)
        label = self.showImage2
        label.setPixmap(pixmap)



if __name__ == '__main__':
    app = QApplication(argv)
    mn = MainWindow()
    mn.show()
    exit(app.exec())

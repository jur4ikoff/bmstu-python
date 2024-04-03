import warnings
from sys import argv, exit
from PyQt6 import uic
from fnmatch import fnmatch
from backend import encrypt, decrypt
from PyQt6.QtWidgets import QApplication, QMessageBox, QDialog, QVBoxLayout, QFileDialog
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QTableWidget
from PyQt6.QtGui import QPixmap

warnings.filterwarnings('ignore')

WEIGHT, HEIGHT = 800, 740


class MainWindow(QMainWindow):
    """class with frontend"""

    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        self.initUI()

    def initUI(self):
        """base settings"""
        self.binding_keys()
        self.status = 0
        self.mode = 0
        self.file = -2
        self.setFixedSize(WEIGHT, HEIGHT)
        self.setWindowTitle('Стеганография')

    def binding_keys(self):
        '''Binding Buttons'''
        self.AuthorMenu.triggered.connect(self.show_author_info)
        self.comboBox.activated.connect(self.on_combobox_activated)
        self.chooseFile.clicked.connect(self.open_file_dialog)
        self.convertButton.clicked.connect(self.convert)

    def show_author_info(self):
        '''Вывод информации об авторе'''
        author_info = "Выполнил Попов Ю.А. ИУ7-22Б"
        QMessageBox.information(self, 'Об авторе', author_info)

    def on_combobox_activated(self):
        selected_text = self.comboBox.currentText()
        if selected_text == "Шифрование":
            self.mode = 0
        else:
            self.mode = 1
        self.set_status_label(selected_text, 0)

    def load_picture(self, image):
        if fnmatch(image, "*.bmp"):
            pixmap = QPixmap(image)
            label = self.showImage
            label.setPixmap(pixmap)
            label.setScaledContents(True)
            self.status += 1
        else:
            self.file = -1

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Text files (*.bmp);;All files (*.*)")

        if file_dialog.exec():
            selected_file = file_dialog.selectedFiles()
            self.file = selected_file[0]
            self.set_status_label(f"Выбран файл: {self.file}", 1)
            self.load_picture(self.file)
        else:
            self.file = -1

    def set_status_label(self, text, label):
        if label == 0:
            self.statusLabel.setText(text)
        elif label == 1:
            self.fileStatus.setText(text)

    def get_lineEdit_text(self):
        self.entered_text = self.textToCrypt.toPlainText()
        self.status += 1

    def convert(self):
        self.get_lineEdit_text()
        if self.status < 2:
            print(self.file, self.entered_text, self.status)
            self.status = 0

            self.set_status_label(f"Ошибка в данных", 0)
            return 1

        if self.mode == 0:
            try:
                self.path = encrypt(self.entered_text, self.file)
                self.load_picture(self.path)
                self.mode = 1
                self.set_status_label(f"Зашифровано, режим дешифровки", 0)
                self.set_status_label(f"Выбран файл: {self.path}", 1)
            except Exception as e:
                self.set_status_label(f"Произошла ошибка {e}", 0)
        elif self.mode == 1:
            text = decrypt(self.path)
            print(text)
            self.textToCrypt.setPlainText(text)
            self.mode = 0
            self.set_status_label(f"Расшифровано, режим шифровки", 0)


if __name__ == '__main__':
    app = QApplication(argv)
    mn = MainWindow()
    mn.show()
    exit(app.exec())

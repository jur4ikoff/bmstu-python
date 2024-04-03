from PyQt6.QtWidgets import QApplication
from frontend import MainWindow, argv

# Лабораторная работа номер 3 - “Стеганография”
# Автор - Попов Ю.А. ИУ7-22Б


if __name__ == '__main__':
    app = QApplication(argv)
    mn = MainWindow()
    mn.show()
    exit(app.exec())

import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import threading, queue
from time import sleep
from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

class MainWindow(QtWidgets.QMainWindow):
    
    openFile = None
    itemQ = queue.Queue()

    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        rootDir = os.path.dirname(os.path.abspath(__file__))

        self.ui = uic.loadUi(rootDir + '\design.ui', self)
        self.btnBrowse.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
                                                            # при нажатии кнопки
        self.btnNext.clicked.connect(self.next_part_data)  # Выполнить функцию browse_folder
        self.initUI()
    
    # Инициализация интерфейса
    def initUI(self):
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)

    # Открытие файла
    def browse_folder(self):
       pass
       
    # Запись данных в очередь
    def file_gen(self):
       pass
    
    # Получение следующей порции данных
    def next_part_data(self):        
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()







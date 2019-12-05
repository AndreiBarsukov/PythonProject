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

    # Запись данных в очередь
    def file_gen(self):
        while True and not self.openFile.closed:  
            data = self.openFile.readline()
            if not data:
                self.openFile.close()     
                break            
            #sleep(0.3)  
            self.itemQ.put(data)
            print("Элементов в очереди: " + str(self.itemQ.qsize()))

    # Открытие файла
    def browse_folder(self):
        pathFile = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите папку", './','CSV files(*.csv)')
        if pathFile[0] != '':
            self.openFile = open(pathFile[0]) 
            #self.next_part_data()
        t = threading.Thread(target=self.file_gen, name = "Th ")
        t.setDaemon(True) # позволяет завершать основной поток, не дожидаясь порожденных
        t.start()
        self.next_part_data()
    
    # Получение следующей порции данных
    def next_part_data(self):        
        try:
            print('PyQt5 button click')
            if self.openFile == None or self.itemQ.empty():
                raise Exception("Файл не выбран, либо полностью просмотрен!\nЗакрыть программу?")
            self.curentRow = 0
            for i in range(5):
                elem = self.itemQ.get()
                line = elem.split(",")
                for col in range(3):
                    self.tableWidget.setItem(i, col, QTableWidgetItem(line[col]))            
        except Exception as identifier:
            buttonReply = QMessageBox.question(self, 
                                               'Warning!', 
                                               str(identifier), 
                                               QMessageBox.Yes)
            if buttonReply == QMessageBox.Yes:
                exit()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()







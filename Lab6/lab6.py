import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def file_gen(f_obj,limit):
    lim = 0
    while True:
        if lim >= limit:
            break
        data = f_obj.readline()
        if not data:
            f_obj.close()
            raise Exception("End of the file!")
            break       
        lim += 1
        yield data

f = open('conversionRates.csv') 
  
class App(QWidget):    
    def __init__(self):
        super().__init__()
        self.title = 'Большое представление о состоянии науки о данных и машинного обучения.'
        self.left = 0
        self.top = 0
        self.width = 350
        self.height = 230
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createTable()

        # Добавлен layout, и занесена таблица в layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 
        
        button = QPushButton('Next', self)
        button.setToolTip('This is an example button')
        button.move(235,185)
        button.clicked.connect(self.on_click2)

        # Отображение виджета
        self.show()

    def createTable(self):
       # Создание таблицы
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(3)

        
        row = 0
        titles = f.readline()
        for elem in file_gen(f, 5):            
            line = elem.split(",")
            print(line)
            for col in range(3):
                self.tableWidget.setItem(row, col, QTableWidgetItem(line[col]))
                print("row", row)
                print("col", col)
            row += 1               
        self.tableWidget.move(0,0)
        # Вызов функции на выбор ячейки
        self.tableWidget.doubleClicked.connect(self.on_click)
    
    
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), 
                  currentQTableWidgetItem.column(), 
                  currentQTableWidgetItem.text())
    
    def on_click2(self):        
        try:
            row = 0
            print('PyQt5 button click')
            for elem in file_gen(f, 5):            
                line = elem.split(",")
                print(line)
                for col in range(3):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(line[col]))
                row += 1      
        except Exception as identifier:
            buttonReply = QMessageBox.question(self, 
                                               'Конец файла', 
                                               "Файл закончился, закрыть программу?", 
                                               QMessageBox.Yes)
            if buttonReply == QMessageBox.Yes:
                exit()
          
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())  
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QInputDialog,QLineEdit
from PyQt5.QtGui import QIcon
class App(QWidget):
   def __init__(self):
           super().__init__()
           self.title='Hello, world!'
           self.left=10
           self.top=10
           self.width=300
           self.height=250
           self.initUI()
   def initUI(self):
           self.setWindowTitle(self.title)
           self.setGeometry(self.left,self.top,self.width,self.height)
           self.getDouble()
           self.show()
   def getDouble(self):
           d,okPressed=QInputDialog.getDouble(self,'Get double','Value',9,0.5,100,9.5)
           if okPressed:
                   print(d)
if __name__=='__main__':
   app=QApplication(sys.argv)
   ex=App()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox
from PyQt5 import uic
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
 def __init__(self):
  QMainWindow.__init__(self)
  self.resize(800, 500) #Tamaño inicial de la ventana 800x500
  #Barra de estado
  self.statusBar().showMessage("Bienvenid@")
  #Objeto menuBar
  menu = self.menuBar()
  #Menú padre
  menu_archivo = menu.addMenu("&Archivo")
  #Menú padre
  menu_editar = menu.addMenu("&Editar")
  
  #Agregar un elemento acción al menu_archivo
  menu_archivo_abrir = QAction(QIcon(), "&Abrir", self)
  menu_archivo_abrir.setShortcut("Ctrl+o") #Atajo de teclado
  menu_archivo_abrir.setStatusTip("Abrir") #Mensaje en la barra de estado
  menu_archivo_abrir.triggered.connect(self.menuArchivoAbrir) #Lanzador
  menu_archivo.addAction(menu_archivo_abrir)
  
  #Agregar un elemento acción al menu_archivo
  menu_archivo_cerrar = QAction(QIcon(), "&Cerrar", self)
  menu_archivo_cerrar.setShortcut("Ctrl+w") #Atajo de teclado
  menu_archivo_cerrar.setStatusTip("Cerrar") #Mensaje en la barra de estado
  menu_archivo_cerrar.triggered.connect(self.menuArchivoCerrar) #Lanzador
  menu_archivo.addAction(menu_archivo_cerrar)
  
  #Agregar un submenú al menú menu_editar
  menu_editar_opciones = menu_editar.addMenu("&Opciones")
  menu_editar_opciones_buscar = QAction(QIcon(), "&Buscar", self)
  menu_editar_opciones_buscar.setShortcut("Ctrl+f") #Atajo de teclado
  menu_editar_opciones_buscar.setStatusTip("Buscar") #Mensaje en la barra de estado
  menu_editar_opciones_buscar.triggered.connect(self.menuEditarOpcionesBuscar)
  menu_editar_opciones.addAction(menu_editar_opciones_buscar)
  
 def menuArchivoAbrir(self):
  QMessageBox.information(self, "Abrir", "Acción Abrir", QMessageBox.Discard)
  
 def menuArchivoCerrar(self):
  QMessageBox.information(self, "Cerrar", "Acción Cerrar", QMessageBox.Discard)
  
 def menuEditarOpcionesBuscar(self):
  QMessageBox.information(self, "Buscar", "Acción Buscar", QMessageBox.Discard)
  
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec_()


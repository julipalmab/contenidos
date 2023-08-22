import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap

class MiVentana(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        """
        Este método inicializa la interfaz y todos sus widgets.
        """
        
        # Ajustamos la geometría de la ventana y su título
        self.setGeometry(200, 100, 200, 200)
        self.setWindowTitle('Ventana con imagen')
        
        
        # Creamos el QLabel que contendrá la imagen y definimos su tamaño
        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 100, 100)
        
        # Escribimos la ruta al archivo que contiene la imagen.
        # La imagen obtenida en https://en.wikipedia.org/wiki/Python_(genus)
        ruta_imagen = os.path.join('img', 'python.jpg')
        
        # Cargamos la imagen como pixeles 
        pixeles = QPixmap(ruta_imagen)
        
        # Agregamos los pixeles al elemento QLabel
        self.label.setPixmap(pixeles)
        
        # Finalmente, ajustamos tamaño de contenido al tamaño del elemento (100 x 100)
        self.label.setScaledContents(True)
        
        
        # Una vez que fueron agregados
        # todos los elementos a la ventana la
        # desplegamos en pantalla
        self.show()


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())
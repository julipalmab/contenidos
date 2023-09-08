from random import randint
from time import sleep

from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QPixmap, QColor
from PyQt6.QtWidgets import QLabel, QWidget, QApplication
import sys


class Cuadrado(QThread):
    identificador = 0

    def __init__(self, senal_mover, limite_x, limite_y):
        super().__init__()
        self.id = Cuadrado.identificador
        Cuadrado.identificador += 1

        # guardamos la señal
        self.senal_mover = senal_mover

        # Seteamos la posición inicial y la guardamos para usarla como una property
        self._posicion = (0, 0)
        self.posicion = (randint(0, limite_x), randint(0, limite_y))

    @property
    def posicion(self):
        return self._posicion

    # Cada vez que se actualicé la posición,
    # se actualiza la posición de la etiqueta
    @posicion.setter
    def posicion(self, valor):
        self._posicion = valor
        self.senal_mover.emit(self.id, *self.posicion)

    def run(self):
        while True:
            sleep(0.1)
            nuevo_x = self.posicion[0] + randint(-2, 2)
            nuevo_y = self.posicion[1] + randint(-2, 2)
            self.posicion = (nuevo_x, nuevo_y)


class MiVentana(QWidget):
    senal_mover = pyqtSignal(int, int, int)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Correcto uso de señales")
        self.setGeometry(200, 200, 500, 500)

        # Definimos QLabel para el fondo de la ventana
        self.fondo = QLabel(self)
        self.fondo.setStyleSheet("background: orange")
        self.fondo.setGeometry(0, 0, 500, 500)

        self.cuadrados = []
        self.labels = {}

        for i in range(100):
            self.crear_cuadrado()

        self.senal_mover.connect(self.mover)
        self.show()

    def crear_cuadrado(self):
        # Creamos el label y se lo pasamos al Cuadrado
        label = QLabel(self)
        label.setGeometry(-50, -50, 50, 50)
        # Creamos un QPixmap de color aleatorio
        pixmap = QPixmap(50, 50)
        pixmap.fill(QColor(randint(20, 200), randint(20, 200), randint(20, 200)))
        label.setPixmap(pixmap)
        label.show()

        nuevo_cuadrado = Cuadrado(self.senal_mover, self.width(), self.height())
        self.labels[nuevo_cuadrado.id] = label
        self.cuadrados.append(nuevo_cuadrado)
        nuevo_cuadrado.start()

    def mover(self, id, x, y):
        self.labels[id].move(x, y)


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication([])
    ex = MiVentana()
    sys.exit(app.exec())

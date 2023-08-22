import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QGridLayout, QVBoxLayout)


class MiVentana(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.show()

    def init_gui(self):

        # Creamos una etiqueta para status. Recordar que los widgets simples
        # no tienen StatusBar.
        self.label = QLabel('Status:', self)

        # Creamos la grilla para ubicar los widgets de manera matricial
        self.grilla = QGridLayout()

        valores = ['1', '2', '3',
                   '4', '5', '6',
                   '7', '8', '9',
                   '0', 'CE', 'C']

        # Generamos las posiciones de los botones en la grilla y le asociamos
        # el texto que debe desplegar cada botón guardados en la lista valores
        posiciones = [(i, j) for i in range(4) for j in range(3)]
        
        for posicion, valor in zip(posiciones, valores):
            boton = QPushButton(valor, self)
            self.grilla.addWidget(boton, *posicion)

        # Creamos un layout vertical
        vbox = QVBoxLayout()

        # Agregamos el label al layout con addWidget
        vbox.addWidget(self.label)

        # Agregamos el layout de la grilla al layout vertical con addLayout
        vbox.addLayout(self.grilla)
        self.setLayout(vbox)

        self.move(300, 150)
        self.setWindowTitle('Calculator')


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    form = MiVentana()
    sys.exit(app.exec())
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit)


class Ventana(QWidget):

    def __init__(self):
        super().__init__()
        self.inicializa_gui()

    def inicializa_gui(self):

        self.etiqueta = QLabel(
            'Ingresa una lista de números separados por comas:', self)
        self.etiqueta.move(20, 10)
        self.etiqueta.resize(self.etiqueta.sizeHint())

        self.input = QLineEdit('', self)
        self.input.setGeometry(20, 40, 360, 20)

        self.boton = QPushButton('Ordenar', self)
        self.boton.setGeometry(20, 70, 360, 30)
        self.boton.clicked.connect(self.revisar_y_ordenar)

        self.resultado = QLabel('', self)
        self.resultado.move(20, 100)
        self.resultado.resize(self.resultado.sizeHint())

        self.setGeometry(700, 300, 400, 200)
        self.setWindowTitle('Ordenador de números')
        self.show()

    def revisar_y_ordenar(self):
        texto_input = self.input.text()
        if texto_input:
            texto_input = texto_input.replace(' ', '').strip(',')
            caracteres_posibles = list(map(str, range(0, 10))) + [',']
            for caracter in texto_input:
                if caracter not in caracteres_posibles:
                    self.resultado.setText('Input no válido')
                    self.resultado.resize(self.resultado.sizeHint())
                    return
            lista_de_numeros = [int(porcion)
                                for porcion in texto_input.split(',')]
            numeros_ordenados = []
            while len(lista_de_numeros) > 0:
                minimo_actual = lista_de_numeros[0]
                for numero in lista_de_numeros:
                    if numero < minimo_actual:
                        minimo_actual = numero
                numeros_ordenados.append(minimo_actual)
                lista_de_numeros.remove(minimo_actual)
            texto_resultado = ", ".join([str(numero)
                                        for numero in numeros_ordenados])
            self.resultado.setText(texto_resultado)
            self.resultado.resize(self.resultado.sizeHint())
            self.resultado.repaint()


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook
    
    app = QApplication([])
    ventana = Ventana()
    sys.exit(app.exec())
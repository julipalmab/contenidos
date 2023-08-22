# calculadora.py
from PyQt5.QtCore import pyqtSignal, QObject
# ventana.py
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QLineEdit)

class Calculadora(QObject):

    senal_mostrar_resultado = pyqtSignal(str)

    def suma(self, valor1, valor2):
        string_resultado = str(int(valor1) + int(valor2))
        self.senal_mostrar_resultado.emit(string_resultado)

    def resta(self, valor1, valor2):
        string_resultado = str(int(valor1) - int(valor2))
        self.senal_mostrar_resultado.emit(string_resultado)

    def cuociente(self, valor1, valor2):
        string_resultado = str(float(valor1) / float(valor2))
        self.senal_mostrar_resultado.emit(string_resultado)

    def multiplicacion(self, valor1, valor2):
        string_resultado = str(int(valor1) * int(valor2))
        self.senal_mostrar_resultado.emit(string_resultado)

    def validar_input(self, accion):
        # método que recibe como señal un diccionario de la forma
        # accion = {'operación': operacion, 'valor1': valor1, 'valor2: valor2'}
        if accion['valor1'].isnumeric() and accion['valor2'].isnumeric():
            if accion['operacion'] == "sumar":
                self.suma(accion['valor1'], accion['valor2'])
            elif accion['operacion'] == "restar":
                self.resta(accion['valor1'], accion['valor2'])
            elif accion['operacion'] == "multiplicar":
                self.multiplicacion(accion['valor1'], accion['valor2'])
            elif accion['operacion'] == "dividir":
                if accion['valor2'] == 0:
                    self.senal_mostrar_resultado.emit('Error: No dividir por cero')
                else:
                    self.cuociente(accion['valor1'], accion['valor2'])
        else:
            self.senal_mostrar_resultado.emit('Error: Input inválido')


class Ventana(QWidget):
    senal_calcular = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        self.etiqueta_valor1 = QLabel('Valor 1:', self)
        self.input_valor1 = QLineEdit('', self)
        self.etiqueta_valor2 = QLabel('Valor 2:', self)
        self.input_valor2 = QLineEdit('', self)
        self.boton_suma = QPushButton('+', self)
        self.boton_resta = QPushButton('-', self)
        self.boton_multiplicacion = QPushButton('x', self)
        self.boton_cuociente = QPushButton(':', self)
        self.resultado = QLabel('Resultado: ', self)

        self.inicializa_gui()

    def inicializa_gui(self):

        self.etiqueta_valor1.move(20, 10)
        self.etiqueta_valor1.resize(self.etiqueta_valor1.sizeHint())

        self.input_valor1.setGeometry(20, 40, 360, 20)

        self.etiqueta_valor2.move(20, 70)
        self.etiqueta_valor2.resize(self.etiqueta_valor2.sizeHint())

        self.input_valor2.setGeometry(20, 100, 360, 20)

        self.boton_suma.setGeometry(20, 130, 30, 30)
        self.boton_suma.clicked.connect(self.sumar)

        self.boton_resta.setGeometry(60, 130, 30, 30)
        self.boton_resta.clicked.connect(self.restar)

        self.boton_multiplicacion.setGeometry(100, 130, 30, 30)
        self.boton_multiplicacion.clicked.connect(self.multiplicar)

        self.boton_cuociente.setGeometry(140, 130, 30, 30)
        self.boton_cuociente.clicked.connect(self.dividir)

        self.resultado.move(20, 180)
        self.resultado.resize(self.resultado.sizeHint())

        self.setGeometry(700, 300, 420, 220)
        self.setWindowTitle('Calculadora')
        self.show()

    def sumar(self):
        valor1 = self.input_valor1.text()
        valor2 = self.input_valor2.text()
        self.senal_calcular.emit({'operacion': 'sumar', 'valor1': valor1, 'valor2': valor2})

    def restar(self):
        valor1 = self.input_valor1.text()
        valor2 = self.input_valor2.text()
        self.senal_calcular.emit({'operacion': 'restar', 'valor1': valor1, 'valor2': valor2})

    def multiplicar(self):
        valor1 = self.input_valor1.text()
        valor2 = self.input_valor2.text()
        self.senal_calcular.emit({'operacion': 'multiplicar', 'valor1': valor1, 'valor2': valor2})

    def dividir(self):
        valor1 = self.input_valor1.text()
        valor2 = self.input_valor2.text()
        self.senal_calcular.emit({'operacion': 'dividir', 'valor1': valor1, 'valor2': valor2})

    def mostrar_resultado(self, text):
        texto = f'Resultado: {text}'
        self.resultado.setText(texto)
        self.resultado.resize(self.resultado.sizeHint())
        self.resultado.repaint()



if __name__ == '__main__':
    app = QApplication([])
    calculadora = Calculadora()
    ventana = Ventana()
    # conectar señales a continuación

    ventana.senal_calcular.connect(calculadora.validar_input)
    calculadora.senal_mostrar_resultado.connect(ventana.mostrar_resultado)




    
    sys.exit(app.exec())
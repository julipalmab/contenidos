from PyQt6.QtWidgets import QApplication
from frontend.ventana import Ventana
import sys
import parametros_general as p

# Usar Uno de los 2 "Juego".
# from backend.logica_qthread import Juego
from backend.logica_qtimer import Juego


class Simulacion:
    def __init__(self):
        # Instanciamos nuestros objeto Ventana y Juego
        self.frontend = Ventana(p.TAMAÑO_VENTANA)
        self.backend = Juego(p.TAMAÑO_VENTANA)

    # Conectamos señales
    def conectar(self):
        # Frontend notifica al backend cuando queremos detener un cuadrado
        self.frontend.senal_parar_icono.connect(self.backend.parar_icono)

        # Backend notifica al frontend cuando empieza todo, aparece un ícono
        # y se mueve un ícono
        self.backend.senal_empezar.connect(self.frontend.empezar)
        self.backend.senal_aparecer_icono.connect(self.frontend.aparecer_icono)
        self.backend.senal_mover_icono.connect(self.frontend.mover_icono)

    # Empezamos todo. En este caso es el backend quien comienza la ejecución de todo
    def iniciar(self):
        self.backend.empezar()


if __name__ == "__main__":

    def hook(type_, value, traceback):
        print(type_)
        print(traceback)

    sys.__excepthook__ = hook

    app = QApplication([])
    simulacion = Simulacion()
    simulacion.conectar()
    simulacion.iniciar()

    sys.exit(app.exec())

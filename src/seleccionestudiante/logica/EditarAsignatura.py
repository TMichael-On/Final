import sys
import os

from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import uic
from tkinter import messagebox


class Dialogo(QDialog):


    def __init__(self):
        ruta = os.path.dirname(os.path.abspath(__file__)) + r"\..\vista\EditarAsignatura.ui"
        QDialog.__init__(self)
        uic.loadUi(ruta, self)

        #self.btnConvertir.clicked.connect(self.calculate_convert)
        #self.btnSalir.clicked.connect(self.exit_app)

    def editarAsignatura(self):
        pass

    def exit_app(self):
        resultado = messagebox.askquestion("Salir", "¿Está seguro que desea salir?")
        if resultado == "yes":
            # exit(0)
            quit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = Dialogo()
    dialogo.show()
    app.exec()
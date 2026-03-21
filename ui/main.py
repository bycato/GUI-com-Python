from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        ui_file = QFile("ui/tela.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        self.ui.buttonCalcular.clicked.connect(self.calcular)

    def calcular(self):
        v1 = int(self.ui.lineEditValor1.text())
        v2 = int(self.ui.lineEditValor2.text())
        resultado = v1 + v2
        self.ui.lineEditResultado.setText(str(resultado))

app = QApplication(sys.argv)
window = MainWindow()
window.ui.show()
sys.exit(app.exec())

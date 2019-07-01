import sys
import window
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = PyReaderMainWindow.Ui_MainWindow()
    # ui.show()
    sys.exit(app.exec_())

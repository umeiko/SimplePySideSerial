from mainWindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
import sys

main_window = Ui_MainWindow() # 主界面
app = QApplication(sys.argv)
w = QMainWindow()
main_window.setupUi(w)

def init_methods():
    pass

def close_methods(*args):
    pass

def bind_methods():
    pass

def main():
    w.closeEvent = close_methods
    w.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
from PySide6.QtWidgets import *
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QCursor, QPixmap

from package.ui.ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx
        self.setWindowFlags(Qt.FramelessWindowHint)

        css_file = self.ctx.get_resource("main.css")
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())

        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)
        UIFunctions.uiDefinitions(self)



class UIFunctions(MainWindow):
    def uiDefinitions(self):
        self.ui.btn_close.clicked.connect(lambda: self.close())
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())





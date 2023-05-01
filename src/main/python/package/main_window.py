from PySide6.QtWidgets import *
from PySide6.QtCore import QSize, Qt, QPropertyAnimation, QEasingCurve
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

# BUTTONS CLICK METHOD
    # /////////////////////////////////////////////////////////////////////////////////////////////////////
    def buttonMenuClick(self):
        button = self.sender()
        name = button.objectName()

        match name:
            case "btn_home":
                self.ui.stackedWidget.setCurrentWidget(self.ui.home)
            case "btn_company":
                self.ui.stackedWidget.setCurrentWidget(self.ui.company)
            case "btn_project":
                self.ui.stackedWidget.setCurrentWidget(self.ui.project)
            case "btn_plan":
                self.ui.stackedWidget.setCurrentWidget(self.ui.plan)
            case "btn_dispatch":
                self.ui.stackedWidget.setCurrentWidget(self.ui.dispatch)
            case "btn_archive":
                self.ui.stackedWidget.setCurrentWidget(self.ui.archive)
            case "btn_settings":
                self.ui.stackedWidget.setCurrentWidget(self.ui.settings)


class UIFunctions(MainWindow):
    def uiDefinitions(self):
        # MINIMIZE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        # CLOSE APPLICATION
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        # TOGGLE MENU
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET HOME PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        # BUTTONS CLICK - MENU
        self.ui.btn_home.clicked.connect(self.buttonMenuClick)
        self.ui.btn_project.clicked.connect(self.buttonMenuClick)
        self.ui.btn_company.clicked.connect(self.buttonMenuClick)
        self.ui.btn_plan.clicked.connect(self.buttonMenuClick)
        self.ui.btn_dispatch.clicked.connect(self.buttonMenuClick)
        self.ui.btn_archive.clicked.connect(self.buttonMenuClick)
        self.ui.btn_settings.clicked.connect(self.buttonMenuClick)



    # TOGGLE MENU ANIMATION
    # /////////////////////////////////////////////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        if not enable:
            return
        # GET WIDTH
        width = self.ui.menuBackground_frame.width()

        # SET MAX WIDTH
        STANDARD = 60
        widthExtended = 240 if width == 60 else STANDARD

        # ANIMATION
        self.animation = QPropertyAnimation(self.ui.menuBackground_frame, b"minimumWidth")
        TIME_ANIMATION = 500
        self.animation.setDuration(TIME_ANIMATION)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.setEasingCurve(QEasingCurve.InOutQuart)
        self.animation.start()







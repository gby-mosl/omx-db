from PySide6.QtWidgets import *

class Ui_home(QWidget):
    def __init__(self):
        super().__init__()
        self.home_ui()

    def home_ui(self):
        # HOME PAGE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.homeBackGround_layout = QVBoxLayout(self)
        self.homeBackGround_layout.setContentsMargins(10, 10, 10, 10)
        self.homeBackGround_layout.setSpacing(0)

        self.home_frame = QFrame(self)
        self.home_frame.setObjectName("home_frame")

        self.homeBackGround_layout.addWidget(self.home_frame)

        self.home_layout = QVBoxLayout(self.home_frame)
        self.home_layout.setContentsMargins(0, 0 ,0 ,0)
        self.home_layout.setSpacing(0)








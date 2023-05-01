from PySide6.QtWidgets import *

class Ui_dispatch(QWidget):
    def __init__(self):
        super().__init__()
        self.dispatch_ui()

    def dispatch_ui(self):
        # COMPANY PAGE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.dispatchBackGround_layout = QVBoxLayout(self)
        self.dispatchBackGround_layout.setContentsMargins(10, 10, 10, 10)
        self.dispatchBackGround_layout.setSpacing(0)

        self.dispatch_frame = QFrame(self)
        self.dispatch_frame.setObjectName("dispatch_frame")

        self.dispatchBackGround_layout.addWidget(self.dispatch_frame)

        self.dispatch_layout = QVBoxLayout(self.dispatch_frame)
        self.dispatch_layout.setContentsMargins(0, 0, 0, 0)
        self.dispatch_layout.setSpacing(0)





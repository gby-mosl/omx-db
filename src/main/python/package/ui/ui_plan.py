from PySide6.QtWidgets import *

class Ui_plan(QWidget):
    def __init__(self):
        super().__init__()
        self.plan_ui()

    def plan_ui(self):
        # COMPANY PAGE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.planBackGround_layout = QVBoxLayout(self)
        self.planBackGround_layout.setContentsMargins(10, 10, 10, 10)
        self.planBackGround_layout.setSpacing(0)

        self.plan_frame = QFrame(self)
        self.plan_frame.setObjectName("plan_frame")

        self.planBackGround_layout.addWidget(self.plan_frame)

        self.plan_layout = QVBoxLayout(self.plan_frame)
        self.plan_layout.setContentsMargins(0, 0 ,0 ,0)
        self.plan_layout.setSpacing(0)






from PySide6.QtWidgets import *

class Ui_project(QWidget):
    def __init__(self):
        super().__init__()
        self.project_ui()

    def project_ui(self):
        # HOME PAGE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.projectBackGround_layout = QVBoxLayout(self)
        self.projectBackGround_layout.setContentsMargins(10, 10, 10, 10)
        self.projectBackGround_layout.setSpacing(0)

        self.project_frame = QFrame(self)
        self.project_frame.setObjectName("project_frame")

        self.projectBackGround_layout.addWidget(self.project_frame)

        self.project_layout = QVBoxLayout(self.project_frame)
        self.project_layout.setContentsMargins(0, 0 ,0 ,0)
        self.project_layout.setSpacing(0)





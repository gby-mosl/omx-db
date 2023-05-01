from PySide6.QtWidgets import *


class Ui_archive(QWidget):
    def __init__(self):
        super().__init__()
        self.archive_ui()

    def archive_ui(self):
        # COMPANY PAGE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.archiveBackGround_layout = QVBoxLayout(self)
        self.archiveBackGround_layout.setContentsMargins(10, 10, 10, 10)
        self.archiveBackGround_layout.setSpacing(0)

        self.archive_frame = QFrame(self)
        self.archive_frame.setObjectName("archive_frame")

        self.archiveBackGround_layout.addWidget(self.archive_frame)

        self.archive_layout = QVBoxLayout(self.archive_frame)
        self.archive_layout.setContentsMargins(0, 0, 0, 0)
        self.archive_layout.setSpacing(0)





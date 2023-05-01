from PySide6.QtWidgets import *


class Ui_settings(QWidget):
    def __init__(self):
        super().__init__()
        self.settings_ui()

    def settings_ui(self):
        # COMPANY PAGE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.settingsBackGround_layout = QVBoxLayout(self)
        self.settingsBackGround_layout.setContentsMargins(10, 10, 10, 10)
        self.settingsBackGround_layout.setSpacing(0)

        self.settings_frame = QFrame(self)
        self.settings_frame.setObjectName("settings_frame")

        self.settingsBackGround_layout.addWidget(self.settings_frame)

        self.settings_layout = QVBoxLayout(self.settings_frame)
        self.settings_layout.setContentsMargins(0, 0, 0, 0)
        self.settings_layout.setSpacing(0)





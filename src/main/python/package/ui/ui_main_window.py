from PySide6.QtWidgets import *
from PySide6.QtCore import QSize, Qt, QRect
from PySide6.QtGui import QCursor, QPixmap

from package.ui.ui_home import *
from package.ui.ui_project import *
from package.ui.ui_company import *
from package.ui.ui_plan import *
from package.ui.ui_dispatch import *
from package.ui.ui_archive import *
from package.ui.ui_settings import *

class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Base de données")
        MainWindow.setFixedSize(QSize(1280, 820))


        MainWindow.central_widget = QWidget()
        MainWindow.setCentralWidget(MainWindow.central_widget)

        self.app_ui(MainWindow)

    # APP UI
    # /////////////////////////////////////////////////////////////////////////////////////////////////////
    def app_ui(self, MainWindow):
        self.appMargins_layout = QVBoxLayout(MainWindow.central_widget)
        self.appMargins_layout.setSpacing(0)
        self.appMargins_layout.setContentsMargins(0, 0, 0, 0)

        self.app_frame = QFrame(MainWindow.central_widget)
        self.app_frame.setObjectName("app_frame")

        self.appMargins_layout.addWidget(self.app_frame)

        self.app_layout = QHBoxLayout(self.app_frame)
        self.app_layout.setSpacing(0)
        self.app_layout.setContentsMargins(0, 0, 0, 0)

        self.appMenu_ui()
        self.appCentral_ui()

    # APP MENU UI
    # /////////////////////////////////////////////////////////////////////////////////////////////////////
    def appMenu_ui(self):
        self.menuBackground_frame = QFrame(self.app_frame)
        self.menuBackground_frame.setObjectName("menuBackground_frame")
        self.menuBackground_frame.setMinimumSize(QSize(60, 0))
        self.menuBackground_frame.setMaximumSize(QSize(60, 20000))


        self.app_layout.addWidget(self.menuBackground_frame)

        self.menuBackground_layout = QVBoxLayout(self.menuBackground_frame)
        self.menuBackground_layout.setContentsMargins(0, 0, 0, 0)
        self.menuBackground_layout.setSpacing(0)

        self.topLogoInfo_frame = QFrame(self.menuBackground_frame)
        self.topLogoInfo_frame.setObjectName("topLogoInfo_frame")
        self.topLogoInfo_frame.setMaximumSize(QSize(20000, 50))
        self.topLogoInfo_frame.setMinimumSize(QSize(0, 50))

        self.menuBackground_layout.addWidget(self.topLogoInfo_frame)

        # TOP LOGO UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.topLogo_frame = QFrame(self.topLogoInfo_frame)
        self.topLogo_frame.setObjectName("topLogo_frame")
        self.topLogo_frame.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo_frame.setMaximumSize(QSize(42, 42))
        self.topLogo_frame.setMinimumSize(QSize(42, 42))

        self.lbl_titleApp = QLabel(self.topLogoInfo_frame)
        self.lbl_titleApp.setObjectName("lbl_titleApp")
        self.lbl_titleApp.setText("OMEXOM Nancy")
        self.lbl_titleApp.setGeometry(QRect(70, 8, 160, 20))
        self.lbl_titleApp.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.lbl_subtitleApp = QLabel(self.topLogoInfo_frame)
        self.lbl_subtitleApp.setObjectName("lbl_subtitleApp")
        self.lbl_subtitleApp.setText("Base de données")
        self.lbl_subtitleApp.setGeometry(QRect(70, 27, 160, 16))
        self.lbl_subtitleApp.setMaximumSize(QSize(20000, 16))
        self.lbl_subtitleApp.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        # MENU UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.menu_frame = QFrame(self.menuBackground_frame)
        self.menu_frame.setObjectName("menu_frame")

        self.menuBackground_layout.addWidget(self.menu_frame)

        self.menu_layout = QVBoxLayout(self.menu_frame)
        self.menu_layout.setContentsMargins(0, 0, 0, 0)
        self.menu_layout.setSpacing(0)

        # BUTTON TOGGLE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.toggle_frame = QFrame(self.menu_frame)
        self.toggle_frame.setObjectName("toggle_frame")
        self.toggle_frame.setMaximumSize(QSize(20000, 45))

        self.menu_layout.addWidget(self.toggle_frame)

        self.toggle_layout = QVBoxLayout(self.toggle_frame)
        self.toggle_layout.setContentsMargins(0, 0, 0, 0)
        self.toggle_layout.setSpacing(0)

        self.btn_toggle = QPushButton(self.toggle_frame)
        self.btn_toggle.setObjectName("btn_toggle")
        self.btn_toggle.setText("Masquer")
        btn_sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        btn_sizePolicy.setHorizontalStretch(0)
        btn_sizePolicy.setVerticalStretch(0)
        btn_sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(btn_sizePolicy)
        self.btn_toggle.setMinimumSize(QSize(0, 45))
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toggle.setLayoutDirection(Qt.LeftToRight)

        self.toggle_layout.addWidget(self.btn_toggle)

        self.topMenu_frame = QFrame(self.menu_frame)
        self.topMenu_frame.setObjectName("topMenu_frame")

        self.menu_layout.addWidget(self.topMenu_frame, 0, Qt.AlignTop)

        # TOP MENU UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.topMenu_layout = QVBoxLayout(self.topMenu_frame)
        self.topMenu_layout.setContentsMargins(0, 0, 0, 0)
        self.topMenu_layout.setSpacing(0)

        # BUTTON HOME UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.btn_home = QPushButton(self.topMenu_frame)
        self.btn_home.setObjectName("btn_home")
        self.btn_home.setText("Accueil")
        btn_sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(btn_sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)

        self.topMenu_layout.addWidget(self.btn_home)

        # BUTTON PROJECT UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.btn_project = QPushButton(self.topMenu_frame)
        self.btn_project.setObjectName("btn_project")
        self.btn_project.setText("Affaires")
        btn_sizePolicy.setHeightForWidth(self.btn_project.sizePolicy().hasHeightForWidth())
        self.btn_project.setSizePolicy(btn_sizePolicy)
        self.btn_project.setMinimumSize(QSize(0, 45))
        self.btn_project.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_project.setLayoutDirection(Qt.LeftToRight)

        self.topMenu_layout.addWidget(self.btn_project)

        # BUTTON COMPANY UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.btn_company = QPushButton(self.topMenu_frame)
        self.btn_company.setObjectName("btn_company")
        self.btn_company.setText("Contacts")
        btn_sizePolicy.setHeightForWidth(self.btn_company.sizePolicy().hasHeightForWidth())
        self.btn_company.setSizePolicy(btn_sizePolicy)
        self.btn_company.setMinimumSize(QSize(0, 45))
        self.btn_company.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_company.setLayoutDirection(Qt.LeftToRight)

        self.topMenu_layout.addWidget(self.btn_company)

        # BUTTON PLAN UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.btn_plan = QPushButton(self.topMenu_frame)
        self.btn_plan.setObjectName("btn_plan")
        self.btn_plan.setText("Plans")
        btn_sizePolicy.setHeightForWidth(self.btn_company.sizePolicy().hasHeightForWidth())
        self.btn_plan.setSizePolicy(btn_sizePolicy)
        self.btn_plan.setMinimumSize(QSize(0, 45))
        self.btn_plan.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plan.setLayoutDirection(Qt.LeftToRight)

        self.topMenu_layout.addWidget(self.btn_plan)

        # BUTTON DISPATCH UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.btn_dispatch = QPushButton(self.topMenu_frame)
        self.btn_dispatch.setObjectName("btn_dispatch")
        self.btn_dispatch.setText("Envois")
        btn_sizePolicy.setHeightForWidth(self.btn_dispatch.sizePolicy().hasHeightForWidth())
        self.btn_dispatch.setSizePolicy(btn_sizePolicy)
        self.btn_dispatch.setMinimumSize(QSize(0, 45))
        self.btn_dispatch.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dispatch.setLayoutDirection(Qt.LeftToRight)

        self.topMenu_layout.addWidget(self.btn_dispatch)

        # BUTTON ARCHIVE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.btn_archive = QPushButton(self.topMenu_frame)
        self.btn_archive.setObjectName("btn_archive")
        self.btn_archive.setText("Archive")
        btn_sizePolicy.setHeightForWidth(self.btn_archive.sizePolicy().hasHeightForWidth())
        self.btn_archive.setSizePolicy(btn_sizePolicy)
        self.btn_archive.setMinimumSize(QSize(0, 45))
        self.btn_archive.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_archive.setLayoutDirection(Qt.LeftToRight)

        self.topMenu_layout.addWidget(self.btn_archive)

        # BOTTOM MENUE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.bottomMenu_frame = QFrame(self.menu_frame)
        self.bottomMenu_frame.setObjectName("bottomMenu_frame")

        self.menu_layout.addWidget(self.bottomMenu_frame, 0, Qt.AlignBottom)

        self.bottomMenu_layout = QVBoxLayout(self.bottomMenu_frame)
        self.bottomMenu_layout.setContentsMargins(0, 0, 0, 0)
        self.bottomMenu_layout.setSpacing(0)

        # BUTTON SETTINGS UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.btn_settings = QPushButton(self.bottomMenu_frame)
        self.btn_settings.setObjectName("btn_settings")
        self.btn_settings.setText("Réglages")
        btn_sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(btn_sizePolicy)
        self.btn_settings.setMinimumSize(QSize(0, 45))
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)

        self.bottomMenu_layout.addWidget(self.btn_settings)

    # CENTRAL APP UI
    # /////////////////////////////////////////////////////////////////////////////////////////////////////
    def appCentral_ui(self):
        self.centralBackground_frame = QFrame(self.app_frame)
        self.centralBackground_frame.setObjectName("centralBackground_frame")

        self.app_layout.addWidget(self.centralBackground_frame)

        self.central_layout = QVBoxLayout(self.centralBackground_frame)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.setSpacing(0)

        # INSERTING TOP BAR
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.topBar_ui()

        # INSERTING CONTENT
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.content_ui()

        # INSERTING BOTTOM BAR
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.bottomBar_ui()

    # TOP BAR UI
    # /////////////////////////////////////////////////////////////////////////////////////////////////////
    def topBar_ui(self):
        self.topBarBackground_frame = QFrame(self.centralBackground_frame)
        self.topBarBackground_frame.setObjectName("topBarBackground_frame")
        self.topBarBackground_frame.setMinimumSize(QSize(0, 50))
        self.topBarBackground_frame.setMaximumSize(QSize(20000, 50))

        self.central_layout.addWidget(self.topBarBackground_frame)

        self.topBarBackground_layout = QHBoxLayout(self.topBarBackground_frame)
        self.topBarBackground_layout.setContentsMargins(0, 0, 0, 0)
        self.topBarBackground_layout.setSpacing(0)

        # LEFT BOX UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.topBarLeftBox_frame = QFrame(self.topBarBackground_frame)
        self.topBarLeftBox_frame.setObjectName("topBarLeftBox_frame")
        topBarLeftBox_sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        topBarLeftBox_sizePolicy.setHorizontalStretch(0)
        topBarLeftBox_sizePolicy.setVerticalStretch(0)
        topBarLeftBox_sizePolicy.setHeightForWidth(self.topBarLeftBox_frame.sizePolicy().hasHeightForWidth())
        self.topBarLeftBox_frame.setSizePolicy(topBarLeftBox_sizePolicy)

        self.topBarBackground_layout.addWidget(self.topBarLeftBox_frame)

        self.topBarLeftBox_layout = QHBoxLayout(self.topBarLeftBox_frame)
        self.topBarLeftBox_layout.setContentsMargins(0, 0, 0, 0)
        self.topBarLeftBox_layout.setSpacing(0)

        # LEFT BOX TITLE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.lbl_topBarLeftBoxTitle = QLabel(self.topBarLeftBox_frame)
        self.lbl_topBarLeftBoxTitle.setObjectName("lbl_topBarLeftBoxTitle")
        self.lbl_topBarLeftBoxTitle.setText("OMEXOM NANCY  |  Bureau d'Etudes - Base de données")
        topBarLeftBoxTitle_sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        topBarLeftBoxTitle_sizePolicy.setHorizontalStretch(0)
        topBarLeftBoxTitle_sizePolicy.setVerticalStretch(0)
        topBarLeftBoxTitle_sizePolicy.setHeightForWidth(self.lbl_topBarLeftBoxTitle.sizePolicy().hasHeightForWidth())
        self.lbl_topBarLeftBoxTitle.setSizePolicy(topBarLeftBoxTitle_sizePolicy)
        self.lbl_topBarLeftBoxTitle.setMaximumSize(QSize(20000, 45))
        self.lbl_topBarLeftBoxTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.topBarLeftBox_layout.addWidget(self.lbl_topBarLeftBoxTitle)

        # RIGHT BOX UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.topBarRightBox_frame = QFrame(self.topBarBackground_frame)
        self.topBarRightBox_frame.setObjectName("topBarRightBox_frame")
        self.topBarRightBox_frame.setMinimumSize(QSize(0, 28))

        self.topBarBackground_layout.addWidget(self.topBarRightBox_frame)

        self.topBarRightBox_layout = QHBoxLayout(self.topBarRightBox_frame)
        self.topBarRightBox_layout.setContentsMargins(0, 0, 0, 0)
        self.topBarRightBox_layout.setSpacing(5)

        # RIGHT BOX : BUTTONS UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        topBar_buttons = ["minimize", "close"]
        for button in topBar_buttons:
            self.button = QPushButton(self.topBarRightBox_frame)
            self.button.setObjectName(f"btn_{button}")
            if button == "close":
                self.btn_close = self.button
            elif button == "maximize":
                self.btn_maximize = self.button
            elif button == "minimize":
                self.btn_minimize = self.button
            self.button.setMinimumSize(QSize(28, 28))
            self.button.setMaximumSize(QSize(28, 28))
            self.button.setCursor(QCursor(Qt.PointingHandCursor))
            self.button.setIcon(QPixmap(f"/Users/guillaume/Code/omx_db/src/main/resources/base/icons/images/icon_{button}.png"))
            self.button.setIconSize(QSize(20,20))

            self.topBarRightBox_layout.addWidget(self.button)

    # CONTENT UI
    # /////////////////////////////////////////////////////////////////////////////////////////////////////
    def content_ui(self):
        self.contentBackground_frame = QFrame(self.centralBackground_frame)
        self.contentBackground_frame.setObjectName("contentBackground_frame")

        self.central_layout.addWidget(self.contentBackground_frame)

        self.contentBackground_layout = QVBoxLayout(self.contentBackground_frame)
        self.contentBackground_layout.setContentsMargins(0, 0, 0, 0)
        self.contentBackground_layout.setSpacing(0)

        self.content_frame = QFrame(self.contentBackground_frame)
        self.content_frame.setObjectName("content_frame")

        self.contentBackground_layout.addWidget(self.content_frame)

        self.content_layout = QHBoxLayout(self.content_frame)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)

        # PAGE CONTAINER & STACKEDWIDGET UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.container_frame = QFrame(self.content_frame)
        self.container_frame.setObjectName("container_frame")

        self.content_layout.addWidget(self.container_frame)

        self.container_layout = QVBoxLayout(self.container_frame)
        self.container_layout.setContentsMargins(0, 0, 0 ,0)
        self.container_layout.setSpacing(0)

        self.stackedWidget = QStackedWidget(self.container_frame)
        self.stackedWidget.setObjectName("stackedWidget")

        self.container_layout.addWidget(self.stackedWidget)

        # INSERTING HOME PAGE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.home = Ui_home()
        self.stackedWidget.addWidget(self.home)

        # INSERTING PROJECT PAGE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.project = Ui_project()
        self.stackedWidget.addWidget(self.project)

        # INSERTING COMPANY PAGE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.company = Ui_company()
        self.stackedWidget.addWidget(self.company)

        # INSERTING PLAN PAGE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.plan = Ui_plan()
        self.stackedWidget.addWidget(self.plan)

        # INSERTING DISPATCH PAGE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.dispatch = Ui_dispatch()
        self.stackedWidget.addWidget(self.dispatch)

        # INSERTING ARCHIVE PAGE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.archive = Ui_archive()
        self.stackedWidget.addWidget(self.archive)

        # INSERTING SETTINGS PAGE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.settings = Ui_settings()
        self.stackedWidget.addWidget(self.settings)

        # DEFAULT CURRENT INDEX OF STACKEDWIDGET
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.stackedWidget.setCurrentIndex(0)

    # BOTTOM BAR UI
    # /////////////////////////////////////////////////////////////////////////////////////////////////////
    def bottomBar_ui(self):
        self.bottomBarBackground_frame = QFrame(self.centralBackground_frame)
        self.bottomBarBackground_frame.setObjectName("bottomBarBackground_frame")
        self.bottomBarBackground_frame.setMinimumSize(QSize(0, 22))
        self.bottomBarBackground_frame.setMaximumSize(QSize(20000, 22))

        self.central_layout.addWidget(self.bottomBarBackground_frame)

        self.bottomBarBackground_layout = QHBoxLayout(self.bottomBarBackground_frame)
        self.bottomBarBackground_layout.setContentsMargins(0, 0, 0, 0)
        self.bottomBarBackground_layout.setSpacing(0)

        # BOTTOM BAR - LABELS UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.lbl_credits = QLabel(self.bottomBarBackground_frame)
        self.lbl_credits.setText("By: G. BARTHELEMY")
        self.lbl_credits.setObjectName("lbl_credits")
        self.lbl_credits.setMaximumSize(QSize(20000, 16))
        self.lbl_credits.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.bottomBarBackground_layout.addWidget(self.lbl_credits)

        self.lbl_version =QLabel(self.bottomBarBackground_frame)
        self.lbl_version.setText("v1.0.0 - Avril 2023")
        self.lbl_version.setObjectName("lbl_version")
        self.lbl_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.bottomBarBackground_layout.addWidget(self.lbl_version)

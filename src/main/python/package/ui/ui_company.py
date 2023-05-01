from PySide6.QtWidgets import *
from PySide6.QtCore import QSize, Qt

from package.api.company import Company, getAllCompanies

class Ui_company(QWidget):
    def __init__(self):
        super().__init__()
        self.company_ui()
        self.populate_companies()

    def company_ui(self):
        # COMPANY PAGE UI
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.companyBackGround_layout = QVBoxLayout(self)
        self.companyBackGround_layout.setContentsMargins(10, 10, 10, 10)
        self.companyBackGround_layout.setSpacing(0)

        self.companyPage_frame = QFrame(self)
        self.companyPage_frame.setObjectName("companyPage_frame")

        self.companyBackGround_layout.addWidget(self.companyPage_frame)

        self.companyPage_layout = QVBoxLayout(self.companyPage_frame)

        # TOP : COMPANY FORM
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.company_frame = QFrame(self.companyPage_frame)
        self.company_frame.setObjectName("company_frame")

        self.companyPage_layout.addWidget(self.company_frame)

        self.company_layout = QHBoxLayout(self.company_frame)

        # TOP LEFT : COMPANY LISTVIEW ######################
        self.companyList_frame = QFrame(self.company_frame)
        self.companyList_frame.setObjectName("companyList_frame")
        self.companyList_frame.setStyleSheet(u"max-width: 500px;")

        self.company_layout.addWidget(self.companyList_frame)

        self.companyList_layout = QVBoxLayout(self.companyList_frame)

        # TREEVIEW OF COMPANIES LIST
        self.lw_company = QListWidget()
        self.lw_company.itemSelectionChanged.connect(self.populate_company_info)

        self.companyList_layout.addWidget(self.lw_company)

        # TOP RIGHT : COMPANY FORM ######################
        self.companyForm_frame = QFrame(self.company_frame)
        self.companyForm_frame.setObjectName("companyForm_frame")

        self.company_layout.addWidget(self.companyForm_frame)

        self.companyForm_layout = QGridLayout(self.companyForm_frame)

        # COMPANY FORM'S WIDGET
        self.lbl_companyName = QLabel(self.companyForm_frame)
        self.lbl_companyName.setText("Nom de l'entreprise:")
        self.lbl_companyName.setAlignment(Qt.AlignLeft)
        self.le_companyName = QLineEdit(self.companyForm_frame)
        self.le_companyName.setTextMargins(5, 0, 0, 0)

        self.companyForm_layout.addWidget(self.lbl_companyName, 0, 0, 1, 30)
        self.companyForm_layout.addWidget(self.le_companyName, 1, 0, 1, 30)

        self.lbl_companyAddress = QLabel(self.companyForm_frame)
        self.lbl_companyAddress.setText("Rue:")
        self.le_companyAddress = QLineEdit(self.companyForm_frame)
        self.le_companyAddress.setTextMargins(5, 0, 0, 0)

        self.companyForm_layout.addWidget(self.lbl_companyAddress, 2, 0, 1, 30)
        self.companyForm_layout.addWidget(self.le_companyAddress, 3, 0, 1, 30)

        self.lbl_companyPostCode = QLabel(self.companyForm_frame)
        self.lbl_companyPostCode.setText("Code postal:")
        self.le_companyPostCode = QLineEdit(self.companyForm_frame)
        self.le_companyPostCode.setTextMargins(5, 0, 0, 0)

        self.companyForm_layout.addWidget(self.lbl_companyPostCode, 4, 0, 1, 5)
        self.companyForm_layout.addWidget(self.le_companyPostCode, 5, 0, 1, 5)

        self.lbl_companyCity = QLabel(self.companyForm_frame)
        self.lbl_companyCity.setText("Ville:")
        self.le_companyCity = QLineEdit(self.companyForm_frame)
        self.le_companyCity.setTextMargins(5, 0, 0, 0)

        self.companyForm_layout.addWidget(self.lbl_companyCity, 4, 6, 1, 24)
        self.companyForm_layout.addWidget(self.le_companyCity, 5, 6, 1, 24)

        self.btn_newCompany = QPushButton(self.companyForm_frame)
        self.btn_newCompany.setText("+")
        self.btn_newCompany.setStyleSheet(u"margin-top: 20px;")

        self.companyForm_layout.addWidget(self.btn_newCompany, 6, 19, 1, 1)

        self.btn_saveCompany = QPushButton(self.companyForm_frame)
        self.btn_saveCompany.setText("Enregistrer")
        self.btn_saveCompany.setStyleSheet(u"margin-top: 20px;")

        self.companyForm_layout.addWidget(self.btn_saveCompany, 6, 20, 1, 10)

        # BOTTOM : CONTACTS FORM
        # /////////////////////////////////////////////////////////////////////////////////////////////////////
        self.contact_frame = QFrame(self.companyPage_frame)
        self.contact_frame.setObjectName("contact_frame")

        self.companyPage_layout.addWidget(self.contact_frame)

        self.contact_layout = QHBoxLayout(self.contact_frame)

        # BOTTOM LEFT : CONTACTLISTVIEW ######################
        self.contactList_frame = QFrame(self.contact_frame)
        self.contactList_frame.setObjectName("contactList_frame")

        self.contact_layout.addWidget(self.contactList_frame)

        self.contactList_layout = QVBoxLayout(self.contactList_frame)

        # TABLEVIEW OF CONTACTS LIST
        self.tw_contact = QTableWidget(self.contactList_frame)
        self.tw_contact.setColumnCount(7)
        # self.tw_contact.setGeometry(100, 100 ,100 ,100)
        # self.tw_contact.horizontalHeader().setMinimumSectionSize(110)
        self.tw_contact.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tw_contactHeader = ["Status", "Titre", "Nom", "Prénom", "E-mail", "Tél. Bureau", "Tél. Mobile"]
        self.tw_contact.setHorizontalHeaderLabels(tw_contactHeader)

        self.contactList_layout.addWidget(self.tw_contact)

        # BOTTOM RIGHT : CONTACT FORM ######################
        self.contactForm_frame = QFrame(self.contact_frame)
        self.contactForm_frame.setObjectName("contactForm_frame")
        self.contactForm_frame.setStyleSheet(u"max-width: 350px;")

        self.contact_layout.addWidget(self.contactForm_frame)

        self.contactForm_layout = QGridLayout(self.contactForm_frame)

        # CONTACT FORM'S WIDGET
        self.rad_contactType = QRadioButton("M.")
        self.rad_contactType.type = "M."
        self.contactForm_layout.addWidget(self.rad_contactType, 0, 0, 1 ,5)

        self.rad_contactType = QRadioButton("Mme.")
        self.rad_contactType.type = "Mme."
        self.contactForm_layout.addWidget(self.rad_contactType, 0, 5, 1 ,5)

        self.lbl_contactLastname = QLabel(self.contactForm_frame)
        self.lbl_contactLastname.setText("Nom:")
        self.le_contactLastname = QLineEdit(self.contactForm_frame)
        self.le_contactLastname.setTextMargins(5, 0, 0, 0)

        self.contactForm_layout.addWidget(self.lbl_contactLastname, 1, 0, 1, 30)
        self.contactForm_layout.addWidget(self.le_contactLastname, 2, 0, 1, 30)

        self.lbl_contactFirstname = QLabel(self.contactForm_frame)
        self.lbl_contactFirstname.setText("Prénom:")
        self.le_contactFirstname = QLineEdit(self.contactForm_frame)
        self.le_contactFirstname.setTextMargins(5, 0, 0, 0)

        self.contactForm_layout.addWidget(self.lbl_contactFirstname, 3, 0, 1, 30)
        self.contactForm_layout.addWidget(self.le_contactFirstname, 4, 0, 1, 30)

        self.lbl_contactMail = QLabel(self.contactForm_frame)
        self.lbl_contactMail.setText("E-mail:")
        self.le_contactMail = QLineEdit(self.contactForm_frame)
        self.le_contactMail.setTextMargins(5, 0, 0, 0)

        self.contactForm_layout.addWidget(self.lbl_contactMail, 5, 0, 1, 30)
        self.contactForm_layout.addWidget(self.le_contactMail, 6, 0, 1, 30)

        self.lbl_contactPhoneNumber = QLabel(self.contactForm_frame)
        self.lbl_contactPhoneNumber.setText("Tél. Bureau:")
        self.le_contactPhoneNumber= QLineEdit(self.contactForm_frame)
        self.le_contactPhoneNumber.setTextMargins(5, 0, 0, 0)

        self.contactForm_layout.addWidget(self.lbl_contactPhoneNumber, 7, 0, 1, 12)
        self.contactForm_layout.addWidget(self.le_contactPhoneNumber, 8, 0, 1, 12)

        self.lbl_contactGsm = QLabel(self.contactForm_frame)
        self.lbl_contactGsm.setText("Tél. Mobile:")
        self.le_contactGsm = QLineEdit(self.contactForm_frame)
        self.le_contactGsm.setTextMargins(5, 0, 0, 0)

        self.contactForm_layout.addWidget(self.lbl_contactGsm, 7, 13, 1, 13)
        self.contactForm_layout.addWidget(self.le_contactGsm, 8, 13, 1, 13)

        self.rad_contactStatus = QRadioButton("Actif")
        self.rad_contactStatus.status = "Actif"
        self.rad_contactStatus.setChecked(True)
        self.contactForm_layout.addWidget(self.rad_contactStatus, 9, 0, 1, 6)

        self.rad_contactStatus = QRadioButton("Inactif")
        self.rad_contactStatus.status = "Inactif"
        self.contactForm_layout.addWidget(self.rad_contactStatus, 9, 6, 1, 6)

        self.btn_newContact = QPushButton(self.contactForm_frame)
        self.btn_newContact.setText("+")

        self.contactForm_layout.addWidget(self.btn_newContact, 10, 15, 1, 5)

        self.btn_saveContact = QPushButton(self.contactForm_frame)
        self.btn_saveContact.setText("Enregistrer")

        self.contactForm_layout.addWidget(self.btn_saveContact, 10, 20, 1, 10)

        # END UI

    def add_company_to_list_widget(self, company):
        lw_item = QListWidgetItem(company.name)
        lw_item.company = company
        self.lw_company.addItem(lw_item)

    def populate_companies(self):
        companies = getAllCompanies()
        for company in companies:
            self.add_company_to_list_widget(company)

    def get_selected_lw_item(self):
        if selected_items := self.lw_company.selectedItems():
            return selected_items[0]
        return None

    def populate_company_info(self):
        if selected_item := self.get_selected_lw_item():
            self.le_companyName.setText(selected_item.company.name)
            self.le_companyAddress.setText(selected_item.company.address)
            self.le_companyPostCode.setText(selected_item.company.post_code)
            self.le_companyCity.setText(selected_item.company.city)









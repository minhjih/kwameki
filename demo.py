# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'demo.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setMouseTracking(False)
        Widget.setAutoFillBackground(False)
        Widget.setStyleSheet(u"QWidget{background:   rgb(244, 244, 244)  }\n"
"QLabel{color: rgb(0, 0, 0)}")
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 81, 601))
        font = QFont()
        font.setFamilies([u"Noto Sans KR"])
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"background-color: rgb(240, 240, 240);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.workspace_1 = QPushButton(self.frame)
        self.workspace_1.setObjectName(u"workspace_1")
        self.workspace_1.setGeometry(QRect(20, 80, 41, 41))
        self.workspace_1.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 238);")
        self.workspace_3 = QPushButton(self.frame)
        self.workspace_3.setObjectName(u"workspace_3")
        self.workspace_3.setGeometry(QRect(20, 180, 41, 41))
        self.workspace_3.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 238);")
        self.workspace_2 = QPushButton(self.frame)
        self.workspace_2.setObjectName(u"workspace_2")
        self.workspace_2.setGeometry(QRect(20, 130, 41, 41))
        self.workspace_2.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(238, 238, 238);")
        self.workspace = QLabel(self.frame)
        self.workspace.setObjectName(u"workspace")
        self.workspace.setGeometry(QRect(1, 49, 81, 21))
        self.workspace.setAutoFillBackground(False)
        self.workspace.setStyleSheet(u"font: 12pt \"AppleSDGothicNeoM00\";\n"
"color: rgb(0, 0, 0);")
        self.workspace.setAlignment(Qt.AlignCenter)
        self.home_button = QPushButton(self.frame)
        self.home_button.setObjectName(u"home_button")
        self.home_button.setGeometry(QRect(20, 10, 51, 31))
        self.scrollArea = QScrollArea(Widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(80, 50, 571, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 569, 549))
        self.top_menubar = QFrame(self.scrollAreaWidgetContents)
        self.top_menubar.setObjectName(u"top_menubar")
        self.top_menubar.setGeometry(QRect(-10, -10, 731, 561))
        self.top_menubar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.top_menubar.setFrameShape(QFrame.StyledPanel)
        self.top_menubar.setFrameShadow(QFrame.Raised)
        self.file = QLabel(self.top_menubar)
        self.file.setObjectName(u"file")
        self.file.setGeometry(QRect(40, 30, 58, 16))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        font1.setStrikeOut(False)
        self.file.setFont(font1)
        self.file.setFrameShape(QFrame.WinPanel)
        self.file.setFrameShadow(QFrame.Raised)
        self.file.setLineWidth(2)
        self.file.setTextFormat(Qt.AutoText)
        self.file.setAlignment(Qt.AlignCenter)
        self.file.setWordWrap(False)
        self.file.setMargin(0)
        self.last_save = QLabel(self.top_menubar)
        self.last_save.setObjectName(u"last_save")
        self.last_save.setGeometry(QRect(500, 30, 58, 16))
        self.file1_savedate = QLabel(self.top_menubar)
        self.file1_savedate.setObjectName(u"file1_savedate")
        self.file1_savedate.setGeometry(QRect(500, 80, 61, 31))
        self.file2_savedate = QLabel(self.top_menubar)
        self.file2_savedate.setObjectName(u"file2_savedate")
        self.file2_savedate.setGeometry(QRect(500, 160, 61, 31))
        self.file3_savedate = QLabel(self.top_menubar)
        self.file3_savedate.setObjectName(u"file3_savedate")
        self.file3_savedate.setGeometry(QRect(500, 240, 61, 31))
        self.file4_savedate = QLabel(self.top_menubar)
        self.file4_savedate.setObjectName(u"file4_savedate")
        self.file4_savedate.setGeometry(QRect(500, 310, 61, 31))
        self.file5_savedate = QLabel(self.top_menubar)
        self.file5_savedate.setObjectName(u"file5_savedate")
        self.file5_savedate.setGeometry(QRect(500, 390, 61, 31))
        self.file6_savedate = QLabel(self.top_menubar)
        self.file6_savedate.setObjectName(u"file6_savedate")
        self.file6_savedate.setGeometry(QRect(500, 470, 61, 31))
        self.file_1 = QLabel(self.top_menubar)
        self.file_1.setObjectName(u"file_1")
        self.file_1.setGeometry(QRect(40, 70, 441, 31))
        self.file_2 = QLabel(self.top_menubar)
        self.file_2.setObjectName(u"file_2")
        self.file_2.setGeometry(QRect(40, 150, 441, 31))
        self.file_3 = QLabel(self.top_menubar)
        self.file_3.setObjectName(u"file_3")
        self.file_3.setGeometry(QRect(40, 230, 441, 31))
        self.file_4 = QLabel(self.top_menubar)
        self.file_4.setObjectName(u"file_4")
        self.file_4.setGeometry(QRect(40, 300, 441, 31))
        self.file_5 = QLabel(self.top_menubar)
        self.file_5.setObjectName(u"file_5")
        self.file_5.setGeometry(QRect(40, 380, 441, 31))
        self.file_6 = QLabel(self.top_menubar)
        self.file_6.setObjectName(u"file_6")
        self.file_6.setGeometry(QRect(40, 460, 441, 31))
        self.check1 = QCheckBox(self.top_menubar)
        self.check1.setObjectName(u"check1")
        self.check1.setGeometry(QRect(20, 80, 16, 21))
        self.check2 = QCheckBox(self.top_menubar)
        self.check2.setObjectName(u"check2")
        self.check2.setGeometry(QRect(20, 160, 16, 21))
        self.check6 = QCheckBox(self.top_menubar)
        self.check6.setObjectName(u"check6")
        self.check6.setGeometry(QRect(20, 470, 16, 21))
        self.check5 = QCheckBox(self.top_menubar)
        self.check5.setObjectName(u"check5")
        self.check5.setGeometry(QRect(20, 390, 16, 21))
        self.check4 = QCheckBox(self.top_menubar)
        self.check4.setObjectName(u"check4")
        self.check4.setGeometry(QRect(20, 310, 16, 21))
        self.check3 = QCheckBox(self.top_menubar)
        self.check3.setObjectName(u"check3")
        self.check3.setGeometry(QRect(20, 240, 16, 21))
        self.upload_button = QPushButton(self.top_menubar)
        self.upload_button.setObjectName(u"upload_button")
        self.upload_button.setGeometry(QRect(280, 20, 71, 31))
        self.show_button = QPushButton(self.top_menubar)
        self.show_button.setObjectName(u"show_button")
        self.show_button.setGeometry(QRect(200, 20, 71, 31))
        self.download_button = QPushButton(self.top_menubar)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setGeometry(QRect(360, 20, 71, 31))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.right_Serverbar = QFrame(Widget)
        self.right_Serverbar.setObjectName(u"right_Serverbar")
        self.right_Serverbar.setGeometry(QRect(650, 50, 151, 551))
        self.right_Serverbar.setStyleSheet(u"background-color: rgb(207, 207, 207);")
        self.right_Serverbar.setFrameShape(QFrame.StyledPanel)
        self.right_Serverbar.setFrameShadow(QFrame.Raised)
        self.remote_storage = QLabel(self.right_Serverbar)
        self.remote_storage.setObjectName(u"remote_storage")
        self.remote_storage.setGeometry(QRect(20, 10, 121, 21))
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(True)
        self.remote_storage.setFont(font2)
        self.remote_storage.setFrameShape(QFrame.Box)
        self.remote_storage.setLineWidth(3)
        self.remote_storage.setAlignment(Qt.AlignCenter)
        self.remote_storage10 = QLabel(self.right_Serverbar)
        self.remote_storage10.setObjectName(u"remote_storage10")
        self.remote_storage10.setGeometry(QRect(30, 500, 101, 31))
        self.remote_storage9 = QLabel(self.right_Serverbar)
        self.remote_storage9.setObjectName(u"remote_storage9")
        self.remote_storage9.setGeometry(QRect(30, 450, 101, 31))
        self.remote_storage8 = QLabel(self.right_Serverbar)
        self.remote_storage8.setObjectName(u"remote_storage8")
        self.remote_storage8.setGeometry(QRect(30, 400, 101, 31))
        self.remote_storage7 = QLabel(self.right_Serverbar)
        self.remote_storage7.setObjectName(u"remote_storage7")
        self.remote_storage7.setGeometry(QRect(30, 350, 101, 31))
        self.remote_storage6 = QLabel(self.right_Serverbar)
        self.remote_storage6.setObjectName(u"remote_storage6")
        self.remote_storage6.setGeometry(QRect(30, 300, 101, 31))
        self.remote_storage5 = QLabel(self.right_Serverbar)
        self.remote_storage5.setObjectName(u"remote_storage5")
        self.remote_storage5.setGeometry(QRect(30, 250, 101, 31))
        self.remote_storage4 = QLabel(self.right_Serverbar)
        self.remote_storage4.setObjectName(u"remote_storage4")
        self.remote_storage4.setGeometry(QRect(30, 200, 101, 31))
        self.remote_storage3 = QLabel(self.right_Serverbar)
        self.remote_storage3.setObjectName(u"remote_storage3")
        self.remote_storage3.setGeometry(QRect(30, 150, 101, 31))
        self.remote_storage2 = QLabel(self.right_Serverbar)
        self.remote_storage2.setObjectName(u"remote_storage2")
        self.remote_storage2.setGeometry(QRect(30, 100, 101, 31))
        self.remote_storage1 = QLabel(self.right_Serverbar)
        self.remote_storage1.setObjectName(u"remote_storage1")
        self.remote_storage1.setGeometry(QRect(30, 50, 101, 31))
        self.remote_check1 = QCheckBox(self.right_Serverbar)
        self.remote_check1.setObjectName(u"remote_check1")
        self.remote_check1.setGeometry(QRect(10, 50, 16, 21))
        self.remote_check2 = QCheckBox(self.right_Serverbar)
        self.remote_check2.setObjectName(u"remote_check2")
        self.remote_check2.setGeometry(QRect(10, 100, 16, 21))
        self.remote_check3 = QCheckBox(self.right_Serverbar)
        self.remote_check3.setObjectName(u"remote_check3")
        self.remote_check3.setGeometry(QRect(10, 150, 16, 21))
        self.remote_check4 = QCheckBox(self.right_Serverbar)
        self.remote_check4.setObjectName(u"remote_check4")
        self.remote_check4.setGeometry(QRect(10, 200, 16, 21))
        self.remote_check5 = QCheckBox(self.right_Serverbar)
        self.remote_check5.setObjectName(u"remote_check5")
        self.remote_check5.setGeometry(QRect(10, 250, 16, 21))
        self.remote_check6 = QCheckBox(self.right_Serverbar)
        self.remote_check6.setObjectName(u"remote_check6")
        self.remote_check6.setGeometry(QRect(10, 300, 16, 21))
        self.remote_check7 = QCheckBox(self.right_Serverbar)
        self.remote_check7.setObjectName(u"remote_check7")
        self.remote_check7.setGeometry(QRect(10, 350, 16, 21))
        self.remote_check8 = QCheckBox(self.right_Serverbar)
        self.remote_check8.setObjectName(u"remote_check8")
        self.remote_check8.setGeometry(QRect(10, 400, 16, 21))
        self.remote_check9 = QCheckBox(self.right_Serverbar)
        self.remote_check9.setObjectName(u"remote_check9")
        self.remote_check9.setGeometry(QRect(10, 450, 16, 21))
        self.remote_check10 = QCheckBox(self.right_Serverbar)
        self.remote_check10.setObjectName(u"remote_check10")
        self.remote_check10.setGeometry(QRect(10, 500, 16, 21))
        self.top_menubar_2 = QFrame(Widget)
        self.top_menubar_2.setObjectName(u"top_menubar_2")
        self.top_menubar_2.setGeometry(QRect(80, 0, 731, 51))
        self.top_menubar_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.top_menubar_2.setFrameShape(QFrame.StyledPanel)
        self.top_menubar_2.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.top_menubar_2)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(20, 10, 331, 31))
        font3 = QFont()
        font3.setFamilies([u"AppleSDGothicNeoEB00"])
        font3.setPointSize(14)
        self.title.setFont(font3)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.top_menubar_2.raise_()
        self.frame.raise_()
        self.scrollArea.raise_()
        self.right_Serverbar.raise_()

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.workspace_1.setText(QCoreApplication.translate("Widget", u"1", None))
        self.workspace_3.setText(QCoreApplication.translate("Widget", u"3", None))
        self.workspace_2.setText(QCoreApplication.translate("Widget", u"2", None))
        self.workspace.setText(QCoreApplication.translate("Widget", u"workspace", None))
        self.home_button.setText(QCoreApplication.translate("Widget", u"Home", None))
        self.file.setText(QCoreApplication.translate("Widget", u"Files", None))
        self.last_save.setText(QCoreApplication.translate("Widget", u"Last Save", None))
        self.file1_savedate.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.file2_savedate.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.file3_savedate.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.file4_savedate.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.file5_savedate.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.file6_savedate.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.file_1.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.file_2.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.file_3.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.file_4.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.file_5.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.file_6.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.check1.setText("")
        self.check2.setText("")
        self.check6.setText("")
        self.check5.setText("")
        self.check4.setText("")
        self.check3.setText("")
        self.upload_button.setText(QCoreApplication.translate("Widget", u"Upload", None))
        self.show_button.setText(QCoreApplication.translate("Widget", u"Show", None))
        self.download_button.setText(QCoreApplication.translate("Widget", u"Download", None))
        self.remote_storage.setText(QCoreApplication.translate("Widget", u"Remote Storage", None))
        self.remote_storage10.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.remote_storage9.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.remote_storage8.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.remote_storage7.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.remote_storage6.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.remote_storage5.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.remote_storage4.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.remote_storage3.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.remote_storage2.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.remote_storage1.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.remote_check1.setText("")
        self.remote_check2.setText("")
        self.remote_check3.setText("")
        self.remote_check4.setText("")
        self.remote_check5.setText("")
        self.remote_check6.setText("")
        self.remote_check7.setText("")
        self.remote_check8.setText("")
        self.remote_check9.setText("")
        self.remote_check10.setText("")
        self.title.setText(QCoreApplication.translate("Widget", u"Document Version Controll, NAO", None))
    # retranslateUi


        self.bundle_check = [self.check1, self.check2, self.check3, self.check4, self.check5, self.check6]
        self.bundle_file = [self.file_1, self.file2, self.file_3, self.file_4, self.file_5, self.file6]
        self.bundle_savedate = [self.file1_savedate, self.file2_savedate, self.file3_savedate, self.file4_savedate, self.file5_savedate, self.file6_savedate]

    def set(self, bundle_of_united_fileclass):
        for i in range(len(bundle_of_united_fileclass)):
            self.bundle_file[i].setText(QCoreApplication.translate("Widget",bundle_of_united_fileclass[i].file_name,None))
            self.bundle_savedate[i].setText(QCoreApplication.translate("Widget", bundle_of_united_fileclass[i].file_version[-1], None))
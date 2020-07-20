from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimediaWidgets, QtMultimedia
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor, QMoveEvent, QKeySequence, QPainter, QImage
from PyQt5.QtCore import QDir, Qt, QUrl, QSize, Qt, QPoint, QRect, pyqtSignal
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QVideoFrame, QAbstractVideoBuffer, QVideoSurfaceFormat, \
    QAbstractVideoSurface
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar, QShortcut,
                             QDialog)
from translate import translateLang

class SettingDialog(QDialog):

    def __init__(self):
        super(SettingDialog, self).__init__()

        self.setObjectName("self")
        self.resize(477, 248)
        self.setStyleSheet("background-color:black;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.close = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close.sizePolicy().hasHeightForWidth())
        self.close.setSizePolicy(sizePolicy)
        self.close.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon_sets/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon2)
        self.close.setIconSize(QtCore.QSize(27, 27))
        self.close.setDefault(False)
        self.close.setFlat(True)
        self.close.setObjectName("close")
        self.close.clicked.connect(self.exit)
        self.verticalLayout_2.addWidget(self.close)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setStyleSheet(" QGroupBox\n"
                                    "        {\n"
                                    "            color: white;\n"
                                    "            border: 5px solid #2f3338;\n"
                                    "            font-weight: bold;\n"
                                    "            font-size: 8pt;\n"
                                    "        }")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox)
        self.scrollArea.setStyleSheet("            color:rgb(255, 255, 255)    ;\n"
                                      "            border: 0px solid #2f3338;\n"
                                      "            font-weight: bold;\n"
                                      "            font-size: 8pt;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 402, 337))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.arabic_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.arabic_radio.setObjectName("arabic_radio")
        self.verticalLayout.addWidget(self.arabic_radio)
        self.bulgarian_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.bulgarian_radio.setObjectName("bulgarian_radio")
        self.verticalLayout.addWidget(self.bulgarian_radio)
        self.danish_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.danish_radio.setObjectName("danish_radio")
        self.verticalLayout.addWidget(self.danish_radio)
        self.english_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.english_radio.setObjectName("english_radio")
        self.verticalLayout.addWidget(self.english_radio)
        self.german_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.german_radio.setObjectName("german_radio")
        self.verticalLayout.addWidget(self.german_radio)
        self.greek_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.greek_radio.setObjectName("greek_radio")
        self.verticalLayout.addWidget(self.greek_radio)
        self.hindi_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.hindi_radio.setObjectName("hindi_radio")
        self.verticalLayout.addWidget(self.hindi_radio)
        self.italian_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.italian_radio.setObjectName("italian_radio")
        self.verticalLayout.addWidget(self.italian_radio)
        self.japanese_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.japanese_radio.setObjectName("japanese_radio")
        self.verticalLayout.addWidget(self.japanese_radio)
        self.korean_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.korean_radio.setObjectName("korean_radio")
        self.verticalLayout.addWidget(self.korean_radio)
        self.persian_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.persian_radio.setObjectName("persian")
        self.verticalLayout.addWidget(self.persian_radio)
        self.polish_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.polish_radio.setObjectName("polish_radio")
        self.verticalLayout.addWidget(self.polish_radio)
        self.spanish_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.spanish_radio.setObjectName("spanish_radio")
        self.verticalLayout.addWidget(self.spanish_radio)
        self.urdu_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.urdu_radio.setObjectName("urdu_radio")
        self.verticalLayout.addWidget(self.urdu_radio)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.language = [
            "English",
            "Spanish",
            "French",
            "Arabic",
            "Bulgarian",
            "Danish",
            "German",
            "Greek",
            "Persian",
            "Hindi",
            "Italian",
            "Japanese",
            "Korean",
            "Polish",
            "Urdu",
        ]

        QtCore.QMetaObject.connectSlotsByName(self)
        self.setTabOrder(self.scrollArea, self.arabic_radio)
        self.setTabOrder(self.arabic_radio, self.bulgarian_radio)
        self.setTabOrder(self.bulgarian_radio, self.danish_radio)
        self.setTabOrder(self.danish_radio, self.english_radio)
        self.setTabOrder(self.english_radio, self.german_radio)
        self.setTabOrder(self.german_radio, self.greek_radio)
        self.setTabOrder(self.greek_radio, self.hindi_radio)
        self.setTabOrder(self.hindi_radio, self.italian_radio)
        self.setTabOrder(self.italian_radio, self.japanese_radio)
        self.setTabOrder(self.japanese_radio, self.korean_radio)
        self.setTabOrder(self.korean_radio, self.persian_radio)
        self.setTabOrder(self.persian_radio, self.polish_radio)
        self.setTabOrder(self.polish_radio, self.spanish_radio)
        self.setTabOrder(self.spanish_radio, self.urdu_radio)

        self.btnList = [self.arabic_radio,
                        self.bulgarian_radio,
                        self.danish_radio,
                        self.english_radio,
                        self.german_radio,
                        self.greek_radio,
                        self.hindi_radio,
                        self.italian_radio,
                        self.japanese_radio,
                        self.korean_radio,
                        self.persian_radio,
                        self.polish_radio,
                        self.spanish_radio,
                        self.urdu_radio
                        ]

        self.arabic_radio.toggled.connect(self.checkRadio)
        self.bulgarian_radio.toggled.connect(self.checkRadio)
        self.danish_radio.toggled.connect(self.checkRadio)
        self.english_radio.toggled.connect(self.checkRadio)
        self.german_radio.toggled.connect(self.checkRadio)
        self.greek_radio.toggled.connect(self.checkRadio)
        self.hindi_radio.toggled.connect(self.checkRadio)
        self.italian_radio.toggled.connect(self.checkRadio)
        self.japanese_radio.toggled.connect(self.checkRadio)
        self.korean_radio.toggled.connect(self.checkRadio)
        self.persian_radio.toggled.connect(self.checkRadio)
        self.polish_radio.toggled.connect(self.checkRadio)
        self.spanish_radio.toggled.connect(self.checkRadio)
        self.urdu_radio.toggled.connect(self.checkRadio)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.groupBox.setTitle(_translate("self", "Language"))
        self.arabic_radio.setText(_translate("self", "Arabic"))
        self.bulgarian_radio.setText(_translate("self", "Bulgarian"))
        self.danish_radio.setText(_translate("self", "Danish"))
        self.english_radio.setText(_translate("self", "English"))
        self.german_radio.setText(_translate("self", "German"))
        self.greek_radio.setText(_translate("self", "Greek"))
        self.hindi_radio.setText(_translate("self", "Hindi"))
        self.italian_radio.setText(_translate("self", "Italian"))
        self.japanese_radio.setText(_translate("self", "Japanese"))
        self.korean_radio.setText(_translate("self", "Korean"))
        self.persian_radio.setText(_translate("self", "Persian"))
        self.polish_radio.setText(_translate("self", "Polish"))
        self.spanish_radio.setText(_translate("self", "Spanish"))
        self.urdu_radio.setText(_translate("self", "Urdu"))

    def exit(self):
        self.hide()

    def checkRadio(self):
        for btn in self.btnList:
            if btn.isChecked():
                self.changeLanguage(btn.text())
                break

    def changeLanguage(self, lang):
        langdict = translateLang(lang)
        statusList = langdict['present']
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowIcon(QIcon('play-button.ico'))
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setStyleSheet("color:White;")
        msg.setText("Restart Required to Apply Change")
        msg.setWindowTitle("! IMPORTANT")
        # msg.windowFlags(Qt.FramelessWindowHint)
        msg.setDetailedText("The details are as follows: Restart Required to change language")
        msg.show()
        # self.hide()

    def mouseMoveEvent (self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() \
                        - QPoint(self.geometry().width() / 2, self.geometry().height() / 2))
            event.accept()

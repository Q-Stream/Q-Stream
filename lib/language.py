# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newsetting.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(477, 248)
        Dialog.setStyleSheet("background-color:black;\n"
                             "")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.close = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close.sizePolicy().hasHeightForWidth())
        self.close.setSizePolicy(sizePolicy)
        self.close.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.close.setText("")
        self.close.setIconSize(QtCore.QSize(16, 16))
        self.close.setDefault(False)
        self.close.setFlat(True)
        self.close.setObjectName("close")
        self.verticalLayout_2.addWidget(self.close)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
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
        self.english_radio.setChecked(True)
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
        self.persian = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.persian.setObjectName("persian")
        self.verticalLayout.addWidget(self.persian)
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

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.scrollArea, self.arabic_radio)
        Dialog.setTabOrder(self.arabic_radio, self.bulgarian_radio)
        Dialog.setTabOrder(self.bulgarian_radio, self.danish_radio)
        Dialog.setTabOrder(self.danish_radio, self.english_radio)
        Dialog.setTabOrder(self.english_radio, self.german_radio)
        Dialog.setTabOrder(self.german_radio, self.greek_radio)
        Dialog.setTabOrder(self.greek_radio, self.hindi_radio)
        Dialog.setTabOrder(self.hindi_radio, self.italian_radio)
        Dialog.setTabOrder(self.italian_radio, self.japanese_radio)
        Dialog.setTabOrder(self.japanese_radio, self.korean_radio)
        Dialog.setTabOrder(self.korean_radio, self.persian)
        Dialog.setTabOrder(self.persian, self.polish_radio)
        Dialog.setTabOrder(self.polish_radio, self.spanish_radio)
        Dialog.setTabOrder(self.spanish_radio, self.urdu_radio)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "Language"))
        self.arabic_radio.setText(_translate("Dialog", "Arabic"))
        self.bulgarian_radio.setText(_translate("Dialog", "Bulgarian"))
        self.danish_radio.setText(_translate("Dialog", "Danish"))
        self.english_radio.setText(_translate("Dialog", "English"))
        self.german_radio.setText(_translate("Dialog", "German"))
        self.greek_radio.setText(_translate("Dialog", "Greek"))
        self.hindi_radio.setText(_translate("Dialog", "Hindi"))
        self.italian_radio.setText(_translate("Dialog", "Italian"))
        self.japanese_radio.setText(_translate("Dialog", "Japanese"))
        self.korean_radio.setText(_translate("Dialog", "Korean"))
        self.persian.setText(_translate("Dialog", "Persian"))
        self.polish_radio.setText(_translate("Dialog", "Polish"))
        self.spanish_radio.setText(_translate("Dialog", "Spanish"))
        self.urdu_radio.setText(_translate("Dialog", "Urdu"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

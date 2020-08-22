from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os, pickle, getpass, sys, uuid
from lib.translate import translateLang

class SettingDialog(QDialog):
    _translate = QtCore.QCoreApplication.translate
    settingsfile = 'settings.bat'
    def __init__(self):
        super(SettingDialog, self).__init__()
        self.setObjectName("self")
        self.resize(500, 400)
        self.setStyleSheet("background:black;")
        self.setup_ui()

    def setup_ui(self):
        self.dialog_VLayout = QtWidgets.QVBoxLayout(self)
        self.dialog_VLayout.setObjectName("dialog_VLayout")
        self.close_widget = QtWidgets.QWidget(self)
        self.close_ui()
        
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setObjectName("tab_widget")
        # self.tab_widget.setStyleSheet("")
        self.dialog_VLayout.addWidget(self.tab_widget)

        self.lang_tab = QtWidgets.QWidget()
        self.lang_tab_ui()
        self.lang_tab_content()

        self.hotkey_tab = QtWidgets.QWidget()
        self.hotkey_tab_ui()
        self.hotkey_tab_content()

        self.screenshot_tab = QtWidgets.QWidget()
        self.screenshot_tab_ui()
        self.screenshot_tab_content()

    def mouseMoveEvent (self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() \
                        - QPoint(self.geometry().width() / 2, self.geometry().height() / 2))
            event.accept()

    def close_ui(self):
        self.close_widget.setObjectName("close_widget")
        self.close_HLayout = QtWidgets.QHBoxLayout(self.close_widget)
        self.close_HLayout.setObjectName("close_HLayout")

        close_spacerItem = QtWidgets.QSpacerItem(413, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.close_HLayout.addItem(close_spacerItem)

        self.close_btn = QtWidgets.QPushButton(self.close_widget)
        self.close_btn.clicked.connect(self.exit)
        self.close_btn.setText("")

        close_icon = QtGui.QIcon()
        close_icon.addPixmap(QtGui.QPixmap("icon_sets/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(close_icon)

        self.close_btn.setObjectName("close_btn")        
        self.close_HLayout.addWidget(self.close_btn)
        self.dialog_VLayout.addWidget(self.close_widget)

    def exit(self):
        self.close()

    def lang_tab_ui(self):
        self.lang_tab.setStyleSheet("color:white;")
        self.lang_tab.setObjectName("lang_tab")
        self.tab_widget.addTab(self.lang_tab, "")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.lang_tab), self._translate("self", "Languages"))

    def hotkey_tab_ui(self):
        self.hotkey_tab.setStyleSheet("color:white;")
        self.hotkey_tab.setObjectName("hotkeys_tab")
        self.tab_widget.addTab(self.hotkey_tab, "")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.hotkey_tab), self._translate("self", "HotKeys"))

    def screenshot_tab_ui(self):
        self.screenshot_tab.setStyleSheet("color:white;")
        self.screenshot_tab.setObjectName("screenshot_tab")
        self.tab_widget.addTab(self.screenshot_tab, "")
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.screenshot_tab), self._translate("self", "Screenshot"))

    def lang_tab_content(self):
        self.lang_VLayout = QtWidgets.QVBoxLayout(self.lang_tab)
        self.lang_VLayout.setObjectName("lang_VLayout")

        self.lang_groupBox = QtWidgets.QGroupBox(self.lang_tab)
        self.lang_groupBox.setObjectName("lang_groupBox")
        self.lang_groupBox.setTitle(self._translate("self", "Languages"))

        self.lang_screenshot_groupBox_HLayout = QtWidgets.QHBoxLayout(self.lang_groupBox)
        self.lang_screenshot_groupBox_HLayout.setObjectName("lang_screenshot_groupBox_HLayout")

        self.lang_scrollArea = QtWidgets.QScrollArea(self.lang_groupBox)
        self.lang_scrollArea.setWidgetResizable(True)
        self.lang_scrollArea.setObjectName("lang_scrollArea")

        self.lang_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.lang_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -166, 403, 393))
        self.lang_scrollAreaWidgetContents.setObjectName("lang_scrollAreaWidgetContents")

        self.lang_scrollAreaWidgetContents_GLayout = QtWidgets.QGridLayout(self.lang_scrollAreaWidgetContents)
        self.lang_scrollAreaWidgetContents_GLayout.setObjectName("lang_scrollAreaWidgetContents_VGayout")

        self.arabic_radio = QtWidgets.QRadioButton(self.lang_scrollAreaWidgetContents)
        self.arabic_radio.setObjectName("arabic_radio")
        self.arabic_radio.setText(self._translate("self", "Arabic"))
        self.lang_scrollAreaWidgetContents_GLayout.addWidget(self.arabic_radio, 0, 0, 1, 1)

        self.bulgarian_radio = QtWidgets.QRadioButton(self.lang_scrollAreaWidgetContents)
        self.bulgarian_radio.setObjectName("bulgarian_radio")
        self.bulgarian_radio.setText(self._translate("self", "Bulgarian"))
        self.lang_scrollAreaWidgetContents_GLayout.addWidget(self.bulgarian_radio, 0, 1, 1, 1)

        self.danish_radio = QtWidgets.QRadioButton(self.lang_scrollAreaWidgetContents)
        self.danish_radio.setObjectName("danish_radio")
        self.danish_radio.setText(self._translate("self", "Danish"))
        self.lang_scrollAreaWidgetContents_GLayout.addWidget(self.danish_radio, 3, 1, 1, 1)

        self.english_radio = QtWidgets.QRadioButton(self.lang_scrollAreaWidgetContents)
        self.english_radio.setObjectName("english_radio")
        self.english_radio.setText(self._translate("self", "English"))
        self.lang_scrollAreaWidgetContents_GLayout.addWidget(self.english_radio, 3, 0, 1, 1)

        self.german_radio = QtWidgets.QRadioButton(self.lang_scrollAreaWidgetContents)
        self.german_radio.setObjectName("german_radio")
        self.german_radio.setText(self._translate("self", "German"))
        self.lang_scrollAreaWidgetContents_GLayout.addWidget(self.german_radio, 4, 0, 1, 1)

        self.greek_radio = QtWidgets.QRadioButton(self.lang_scrollAreaWidgetContents)
        self.greek_radio.setObjectName("greek_radio")
        self.greek_radio.setText(self._translate("self", "Greek"))
        self.lang_scrollAreaWidgetContents_GLayout.addWidget(self.greek_radio, 4, 1, 1, 1)

        self.hindi_radio = QtWidgets.QRadioButton(self.lang_scrollAreaWidgetContents)
        self.hindi_radio.setObjectName("hindi_radio")
        self.hindi_radio.setText(self._translate("self", "Hindi"))
        self.lang_scrollAreaWidgetContents_GLayout.addWidget(self.hindi_radio, 6, 0, 1, 1)

        self.italian_radio = QtWidgets.QRadioButton(self.lang_scrollAreaWidgetContents)
        self.italian_radio.setObjectName("italian_radio")
        self.italian_radio.setText(self._translate("self", "Italian"))
        self.lang_scrollAreaWidgetContents_GLayout.addWidget(self.italian_radio, 6, 1, 1, 1)

        self.japanese_radio = QtWidgets.QRadioButton(self.lang_scrollAreaWidgetContents)
        self.japanese_radio.setObjectName("japanese_radio")
        self.japanese_radio.setText(self._translate("self", "Japanese"))
        self.lang_scrollAreaWidgetContents_GLayout.addWidget(self.japanese_radio, 9, 0, 1, 1)

        self.korean_radio = QtWidgets.QRadioButton(self.lang_scrollAreaWidgetContents)
        self.korean_radio.setObjectName("korean_radio")
        self.korean_radio.setText(self._translate("self", "Korean"))
        self.lang_scrollAreaWidgetContents_GLayout.addWidget(self.korean_radio, 9, 1, 1, 1)

        self.persian_radio = QtWidgets.QRadioButton(self.lang_scrollAreaWidgetContents)
        self.persian_radio.setObjectName("persian_radio")
        self.persian_radio.setText(self._translate("self", "Persian"))
        self.lang_scrollAreaWidgetContents_GLayout.addWidget(self.persian_radio, 11, 0, 1, 1)

        self.polish_radio = QtWidgets.QRadioButton(self.lang_scrollAreaWidgetContents)
        self.polish_radio.setObjectName("polish_radio")
        self.polish_radio.setText(self._translate("self", "Poslish"))
        self.lang_scrollAreaWidgetContents_GLayout.addWidget(self.polish_radio, 11, 1, 1, 1)

        self.spanish_radio = QtWidgets.QRadioButton(self.lang_scrollAreaWidgetContents)
        self.spanish_radio.setObjectName("spanish_radio")
        self.spanish_radio.setText(self._translate("self", "Spanish"))
        self.lang_scrollAreaWidgetContents_GLayout.addWidget(self.spanish_radio, 13, 0, 1, 1)

        self.urdu_radio = QtWidgets.QRadioButton(self.lang_scrollAreaWidgetContents)
        self.urdu_radio.setObjectName("urdu_radio")
        self.urdu_radio.setText(self._translate("self", "Urdu"))
        self.lang_scrollAreaWidgetContents_GLayout.addWidget(self.urdu_radio, 13, 1, 1, 1)

        self.lang_scrollArea.setWidget(self.lang_scrollAreaWidgetContents)
        self.lang_screenshot_groupBox_HLayout.addWidget(self.lang_scrollArea)
        self.lang_VLayout.addWidget(self.lang_groupBox)

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
        self.setTabOrder(self.lang_scrollArea, self.arabic_radio)
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

    def hotkey_tab_content(self):
        self.hotkey_VLayout = QtWidgets.QVBoxLayout(self.hotkey_tab)
        self.hotkey_VLayout.setObjectName("hotkey_VLayout")
        
        self.hotkey_groupBox = QtWidgets.QGroupBox(self.hotkey_tab)
        self.hotkey_groupBox.setObjectName("hotkey_groupBox")
        self.hotkey_groupBox.setTitle(self._translate("self", "Hotkeys"))
        
        self.hotkey_groupBox_HLayout = QtWidgets.QHBoxLayout(self.hotkey_groupBox)
        self.hotkey_groupBox_HLayout.setObjectName("hotkey_groupBox_HLayout")
        
        self.hotkey_scrollArea = QtWidgets.QScrollArea(self.hotkey_groupBox)
        self.hotkey_scrollArea.setWidgetResizable(True)
        self.hotkey_scrollArea.setObjectName("hotkey_scrollArea")
        
        self.hotkey_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.hotkey_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -431, 403, 658))
        self.hotkey_scrollAreaWidgetContents.setObjectName("hotkey_scrollAreaWidgetContents")
        
        self.hotkey_scrollAreaWidgetContents_VLayout = QtWidgets.QVBoxLayout(self.hotkey_scrollAreaWidgetContents)
        self.hotkey_scrollAreaWidgetContents_VLayout.setObjectName("hotkey_scrollAreaWidgetContents_VLayout")
        
        self.fullscreen_widget = QtWidgets.QWidget(self.hotkey_scrollAreaWidgetContents)
        self.fullscreen_widget.setObjectName("fullscreen_widget")
        self.fullscreen_widget_HLayout = QtWidgets.QHBoxLayout(self.fullscreen_widget)
        self.fullscreen_widget_HLayout.setObjectName("fullscreen_widget_HLayout")
        self.fullscreen_label = QtWidgets.QLabel(self.fullscreen_widget)
        self.fullscreen_label.setObjectName("fullscreen_label")
        self.fullscreen_label.setText(self._translate("self", "Fullscreen"))
        self.fullscreen_edit = QKeySequenceEdit(self.fullscreen_widget)
        self.fullscreen_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        fullscreen_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.fullscreen_widget_HLayout.addWidget(self.fullscreen_label)
        self.fullscreen_widget_HLayout.addItem(fullscreen_spacerItem)
        self.fullscreen_widget_HLayout.addWidget(self.fullscreen_edit)
        self.hotkey_scrollAreaWidgetContents_VLayout.addWidget(self.fullscreen_widget)
        
        self.exit_fullscreen_widget = QtWidgets.QWidget(self.hotkey_scrollAreaWidgetContents)
        self.exit_fullscreen_widget.setObjectName("exit_fullscreen_widget")
        self.exit_fullscreen_widget_HLayout = QtWidgets.QHBoxLayout(self.exit_fullscreen_widget)
        self.exit_fullscreen_widget_HLayout.setObjectName("exit_fullscreen_widget_HLayout")
        self.exit_fullscreen_label = QtWidgets.QLabel(self.exit_fullscreen_widget)
        self.exit_fullscreen_label.setObjectName("exit_fullscreen_label")
        self.exit_fullscreen_label.setText(self._translate("self", "Exit Fullscreen"))
        self.exit_fullscreen_edit = QKeySequenceEdit(self.exit_fullscreen_widget)
        self.exit_fullscreen_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        exit_fullscreen_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.exit_fullscreen_widget_HLayout.addWidget(self.exit_fullscreen_label)
        self.exit_fullscreen_widget_HLayout.addItem(exit_fullscreen_spacerItem)
        self.exit_fullscreen_widget_HLayout.addWidget(self.exit_fullscreen_edit)
        self.hotkey_scrollAreaWidgetContents_VLayout.addWidget(self.exit_fullscreen_widget)
        
        self.play_pause_widget = QtWidgets.QWidget(self.hotkey_scrollAreaWidgetContents)
        self.play_pause_widget.setObjectName("play_pause_widget")
        self.play_pause_widget_HLayout = QtWidgets.QHBoxLayout(self.play_pause_widget)
        self.play_pause_widget_HLayout.setObjectName("play_pause_widget_HLayout")
        self.play_pause_label = QtWidgets.QLabel(self.play_pause_widget)
        self.play_pause_label.setObjectName("play_pause_label")
        self.play_pause_label.setText(self._translate("self", "Play / Pause"))
        self.play_pause_edit = QKeySequenceEdit(self.play_pause_widget)
        self.play_pause_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        play_pause_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.play_pause_widget_HLayout.addWidget(self.play_pause_label)
        self.play_pause_widget_HLayout.addItem(play_pause_spacerItem)
        self.play_pause_widget_HLayout.addWidget(self.play_pause_edit)
        self.hotkey_scrollAreaWidgetContents_VLayout.addWidget(self.play_pause_widget)
        
        self.stop_widget = QtWidgets.QWidget(self.hotkey_scrollAreaWidgetContents)
        self.stop_widget.setObjectName("stop_widget")
        self.stop_widget_HLayout = QtWidgets.QHBoxLayout(self.stop_widget)
        self.stop_widget_HLayout.setObjectName("stop_widget_HLayout")
        self.stop_label = QtWidgets.QLabel(self.stop_widget)
        self.stop_label.setObjectName("stop_label")
        self.stop_label.setText(self._translate("self", "Stop Playback"))
        self.stop_edit = QKeySequenceEdit(self.stop_widget)
        self.stop_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        stop_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.stop_widget_HLayout.addWidget(self.stop_label)
        self.stop_widget_HLayout.addItem(stop_spacerItem)
        self.stop_widget_HLayout.addWidget(self.stop_edit)
        self.hotkey_scrollAreaWidgetContents_VLayout.addWidget(self.stop_widget)
        
        self.mute_widget = QtWidgets.QWidget(self.hotkey_scrollAreaWidgetContents)
        self.mute_widget.setObjectName("mute_widget")
        self.mute_widget_HLayout = QtWidgets.QHBoxLayout(self.mute_widget)
        self.mute_widget_HLayout.setObjectName("mute_widget_HLayout")
        self.mute_label = QtWidgets.QLabel(self.mute_widget)
        self.mute_label.setObjectName("mute_label")
        self.mute_label.setText(self._translate("self", "Mute"))
        self.mute_edit = QKeySequenceEdit(self.mute_widget)
        self.mute_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        mute_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mute_widget_HLayout.addWidget(self.mute_label)
        self.mute_widget_HLayout.addItem(mute_spacerItem)
        self.mute_widget_HLayout.addWidget(self.mute_edit)
        self.hotkey_scrollAreaWidgetContents_VLayout.addWidget(self.mute_widget)
        
        self.vol_up_widget = QtWidgets.QWidget(self.hotkey_scrollAreaWidgetContents)
        self.vol_up_widget.setObjectName("vol_up_widget")
        self.vol_up_widget_HLayout = QtWidgets.QHBoxLayout(self.vol_up_widget)
        self.vol_up_widget_HLayout.setObjectName("vol_up_widget_HLayout")
        self.vol_up_label = QtWidgets.QLabel(self.vol_up_widget)
        self.vol_up_label.setObjectName("vol_up_label")
        self.vol_up_label.setText(self._translate("self", "Volume Up"))
        self.vol_up_edit = QKeySequenceEdit(self.vol_up_widget)
        self.vol_up_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        vol_up_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.vol_up_widget_HLayout.addWidget(self.vol_up_label)
        self.vol_up_widget_HLayout.addItem(vol_up_spacerItem)
        self.vol_up_widget_HLayout.addWidget(self.vol_up_edit)
        self.hotkey_scrollAreaWidgetContents_VLayout.addWidget(self.vol_up_widget)
        
        self.vol_down_widget = QtWidgets.QWidget(self.hotkey_scrollAreaWidgetContents)
        self.vol_down_widget.setObjectName("vol_down_widget")
        self.vol_down_widget_HLayout = QtWidgets.QHBoxLayout(self.vol_down_widget)
        self.vol_down_widget_HLayout.setObjectName("vol_down_widget_HLayout")
        self.vol_down_label = QtWidgets.QLabel(self.vol_down_widget)
        self.vol_down_label.setObjectName("vol_down_label")
        self.vol_down_label.setText(self._translate("self", "Volume Down"))
        self.vol_down_edit = QKeySequenceEdit(self.vol_down_widget)
        self.vol_down_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        vol_down_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.vol_down_widget_HLayout.addWidget(self.vol_down_label)
        self.vol_down_widget_HLayout.addItem(vol_down_spacerItem)
        self.vol_down_widget_HLayout.addWidget(self.vol_down_edit)
        self.hotkey_scrollAreaWidgetContents_VLayout.addWidget(self.vol_down_widget)
        
        self.sforward_widget = QtWidgets.QWidget(self.hotkey_scrollAreaWidgetContents)
        self.sforward_widget.setObjectName("sforward_widget")
        self.sforward_widget_HLayout = QtWidgets.QHBoxLayout(self.sforward_widget)
        self.sforward_widget_HLayout.setObjectName("sforward_widget_HLayout")
        self.sforward_label = QtWidgets.QLabel(self.sforward_widget)
        self.sforward_label.setObjectName("sforward_label")
        self.sforward_label.setText(self._translate("self", "Short Forward (1sec)"))
        self.sforward_edit = QKeySequenceEdit(self.sforward_widget)
        self.sforward_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        sforward_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.sforward_widget_HLayout.addWidget(self.sforward_label)
        self.sforward_widget_HLayout.addItem(sforward_spacerItem)
        self.sforward_widget_HLayout.addWidget(self.sforward_edit)
        self.hotkey_scrollAreaWidgetContents_VLayout.addWidget(self.sforward_widget)
        
        self.sbackground_widget = QtWidgets.QWidget(self.hotkey_scrollAreaWidgetContents)
        self.sbackground_widget.setObjectName("sbackground_widget")
        self.sbackground_widget_HLayout = QtWidgets.QHBoxLayout(self.sbackground_widget)
        self.sbackground_widget_HLayout.setObjectName("sbackground_widget_HLayout")
        self.sbackground_label = QtWidgets.QLabel(self.sbackground_widget)
        self.sbackground_label.setObjectName("sbackground_label")
        self.sbackground_label.setText(self._translate("self", "Short Backward (1sec)"))
        self.sbackground_edit = QKeySequenceEdit(self.sbackground_widget)
        self.sbackground_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        sbackground_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.sbackground_widget_HLayout.addWidget(self.sbackground_label)
        self.sbackground_widget_HLayout.addItem(sbackground_spacerItem)
        self.sbackground_widget_HLayout.addWidget(self.sbackground_edit)
        self.hotkey_scrollAreaWidgetContents_VLayout.addWidget(self.sbackground_widget)
        
        self.mforward_widget = QtWidgets.QWidget(self.hotkey_scrollAreaWidgetContents)
        self.mforward_widget.setObjectName("mforward_widget")
        self.mforward_widget_HLayout = QtWidgets.QHBoxLayout(self.mforward_widget)
        self.mforward_widget_HLayout.setObjectName("mforward_widget_HLayout")
        self.mforward_label = QtWidgets.QLabel(self.mforward_widget)
        self.mforward_label.setObjectName("mforward_label")
        self.mforward_label.setText(self._translate("self", "Medium Forward (5sec)"))
        self.mforward_edit = QKeySequenceEdit(self.mforward_widget)
        self.mforward_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        mforward_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mforward_widget_HLayout.addWidget(self.mforward_label)
        self.mforward_widget_HLayout.addItem(mforward_spacerItem)
        self.mforward_widget_HLayout.addWidget(self.mforward_edit)
        self.hotkey_scrollAreaWidgetContents_VLayout.addWidget(self.mforward_widget)
        
        self.mbackward_widget = QtWidgets.QWidget(self.hotkey_scrollAreaWidgetContents)
        self.mbackward_widget.setObjectName("mbackward_widget")
        self.mbackward_widget_HLayout = QtWidgets.QHBoxLayout(self.mbackward_widget)
        self.mbackward_widget_HLayout.setObjectName("mbackward_widget_HLayout")
        self.mbackward_label = QtWidgets.QLabel(self.mbackward_widget)
        self.mbackward_label.setObjectName("mbackward_label")
        self.mbackward_label.setText(self._translate("self", "Medium Backward (5sec)"))
        self.mbackward_edit = QKeySequenceEdit(self.mbackward_widget)
        self.mbackward_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        mbackward_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mbackward_widget_HLayout.addWidget(self.mbackward_label)
        self.mbackward_widget_HLayout.addItem(mbackward_spacerItem)
        self.mbackward_widget_HLayout.addWidget(self.mbackward_edit)
        self.hotkey_scrollAreaWidgetContents_VLayout.addWidget(self.mbackward_widget)
        
        self.lforward_widget = QtWidgets.QWidget(self.hotkey_scrollAreaWidgetContents)
        self.lforward_widget.setObjectName("lforward_widget")
        self.lforward_widget_HLayout = QtWidgets.QHBoxLayout(self.lforward_widget)
        self.lforward_widget_HLayout.setObjectName("lforward_widget_HLayout")
        self.lforward_label = QtWidgets.QLabel(self.lforward_widget)
        self.lforward_label.setObjectName("lforward_label")
        self.lforward_label.setText(self._translate("self", "Long Forward (10sec)"))
        self.lforward_edit = QKeySequenceEdit(self.lforward_widget)
        self.lforward_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        lforward_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lforward_widget_HLayout.addWidget(self.lforward_label)
        self.lforward_widget_HLayout.addItem(lforward_spacerItem)
        self.lforward_widget_HLayout.addWidget(self.lforward_edit)
        self.hotkey_scrollAreaWidgetContents_VLayout.addWidget(self.lforward_widget)
        
        self.lbackward_widget = QtWidgets.QWidget(self.hotkey_scrollAreaWidgetContents)
        self.lbackward_widget.setObjectName("lbackward_widget")
        self.lbackward_widget_HLayout = QtWidgets.QHBoxLayout(self.lbackward_widget)
        self.lbackward_widget_HLayout.setObjectName("lbackward_widget_HLayout")
        self.lbackward_label = QtWidgets.QLabel(self.lbackward_widget)
        self.lbackward_label.setObjectName("lbackward_label")
        self.lbackward_label.setText(self._translate("self", "Long Backward (10sec)"))
        self.lbackward_edit = QKeySequenceEdit(self.lbackward_widget)
        self.lbackward_edit.setMaximumSize(QtCore.QSize(100, 16777215))
        lbackward_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lbackward_widget_HLayout.addWidget(self.lbackward_label)
        self.lbackward_widget_HLayout.addItem(lbackward_spacerItem)
        self.lbackward_widget_HLayout.addWidget(self.lbackward_edit)
        self.hotkey_scrollAreaWidgetContents_VLayout.addWidget(self.lbackward_widget)
        
        self.hotkey_scrollArea.setWidget(self.hotkey_scrollAreaWidgetContents)
        self.hotkey_groupBox_HLayout.addWidget(self.hotkey_scrollArea)
        self.hotkey_VLayout.addWidget(self.hotkey_groupBox)

    def screenshot_tab_content(self):
        self.screenshot_VLayout = QtWidgets.QVBoxLayout(self.screenshot_tab)
        self.screenshot_VLayout.setObjectName("screenshot_VLayout")
        
        self.screenshot_groupBox = QtWidgets.QGroupBox(self.screenshot_tab)
        self.screenshot_groupBox.setObjectName("screenshot_groupBox")
        self.screenshot_groupBox.setTitle(self._translate("self", "Screenshot"))
        
        self.screenshot_groupBox_HLayout = QtWidgets.QHBoxLayout(self.screenshot_groupBox)
        self.screenshot_groupBox_HLayout.setObjectName("screenshot_groupBox_HLayout")
        
        self.path_widget = QtWidgets.QWidget(self.screenshot_groupBox)
        self.path_widget.setObjectName("path_widget")
        
        self.path_HLayout = QtWidgets.QHBoxLayout(self.path_widget)
        self.path_HLayout.setObjectName("path_HLayout")
        
        self.path_label = QtWidgets.QLabel(self.path_widget)
        self.path_label.setObjectName("path_label")
        self.path_label.setText(self._translate("self", "Screenshot Path"))
        
        self.path_line = QtWidgets.QLineEdit(self.path_widget)
        self.path_line.setObjectName("path_line")
        filename = "screenshot" + str(uuid.uuid4()) + ".png"
        username = getpass.getuser()

        if os.path.exists(self.settingsfile):
            with open(self.settingsfile, 'rb') as sf:
                paths = pickle.load(sf)
                path = paths['ss_path']
            self.path_line.setText(self._translate("self", path))
        else:
            if sys.platform == 'win32':
                path = 'C:/Users/' + username + '/Pictures/'
            elif sys.platform == 'linux' or sys.platform == 'Darwin':    
                path = '/home/' + username + '/Pictures/'
            self.path_line.setText(self._translate("self", path))

        self.screenshot_path_btn = QtWidgets.QPushButton(self.path_widget)
        self.screenshot_path_btn.setStyleSheet("border : 1px solid white;")
        self.screenshot_path_btn.setMinimumSize(QtCore.QSize(30, 16777215))
        self.screenshot_path_btn.setObjectName("screenshot_path_btn")
        self.screenshot_path_btn.clicked.connect(self.browseSlot)
        self.screenshot_path_btn.setText(self._translate("self", "..."))
        
        self.path_HLayout.addWidget(self.path_label)
        self.path_HLayout.addWidget(self.path_line)
        self.path_HLayout.addWidget(self.screenshot_path_btn)

        self.screenshot_groupBox_HLayout.addWidget(self.path_widget)
        self.screenshot_VLayout.addWidget(self.screenshot_groupBox)

    def browseSlot(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory(
                        self, "Select Directory", "")
        if fileName:
            print(fileName)

            file = {}
            file['ss_path'] = fileName
            # print('write: ', file)
            with open(self.settingsfile, 'wb') as sf:
                pickle.dump(file, sf)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # dialog = QtWidgets.QDialog()
    ui = SettingDialog()
    ui.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
    ui.show()
    sys.exit(app.exec_())
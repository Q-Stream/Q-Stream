from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimediaWidgets, QtMultimedia
from PyQt5.QtGui import QFocusEvent, QIcon, QFont, QPalette, QColor, QMoveEvent, QKeySequence, QPainter, QImage
from PyQt5.QtCore import QDir, QUrl, QSize, Qt, QPoint, QRect, pyqtSignal
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QVideoFrame, QAbstractVideoBuffer, QVideoSurfaceFormat, \
    QAbstractVideoSurface
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar, QShortcut,
                             QDialog)
import os
import requests, json, pickle

import pyautogui, uuid, getpass

class window(QWidget):
    import time
    @staticmethod
    def leaveEvent(event):
        
        if ui.isMini:
            ui.frame_2.hide()
            ui.pos_frame.hide()
            ui.frame.hide()

    @staticmethod
    def enterEvent(event):
            ui.frame_2.show()
            ui.pos_frame.show()
            ui.frame.show()

class Videowidget(QVideoWidget):
    def __init__(self,master):
        super().__init__(parent = master)

    @staticmethod
    def mouseMoveEvent (event):
        if event.buttons() == Qt.LeftButton:
            Form.move(event.globalPos() \
                        - QPoint(int(Form.geometry().width() / 2), int(Form.geometry().height() / 2)))
            event.accept()  

    @staticmethod
    def mouseDoubleClickEvent (event):
        if event.buttons() == Qt.LeftButton:
            ui.fullscreen_video()

    
        

class PosSlider(QSlider):
    def __init__(self,master):
        super().__init__(parent = master)
          
    def mousePressEvent (self, event):
        if event.buttons() == Qt.LeftButton:
            ui.mediaPlayer.setPosition(QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), event.x(), self.width()))
            

    def mouseMoveEvent (self, event):
        if event.buttons() == Qt.LeftButton:
            ui.mediaPlayer.setPosition(QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), event.x(), self.width()))


class VolSlider(QSlider):
    def __init__(self,master):
        super().__init__(parent = master)
          
    def mousePressEvent (self, event):
        if event.buttons() == Qt.LeftButton:
            self.setValue(QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), event.x(), self.width()))
            

    def mouseMoveEvent (self, event):
        if event.buttons() == Qt.LeftButton:
            self.setValue(QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), event.x(), self.width()))
    

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 400)
        Form.setMinimumSize(QtCore.QSize(200, 199))
        Form.setStyleSheet("background-color:black;")
        
        self.isOnline = False
        self.isMini = False
        self.isOnTop = True
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.mainFrame = QtWidgets.QFrame(Form)
        self.mainFrame.setMinimumSize(QtCore.QSize(200, 82))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Player_name = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Player_name.sizePolicy().hasHeightForWidth())
        self.Player_name.setSizePolicy(sizePolicy)
        self.Player_name.setStyleSheet("QLabel\n"
                                        "    {\n"
                                        "    font: 12pt \"Helvetica\";\n"
                                        "    color: white;\n"
                                        "    border: 0px solid #076100;\n"
                                        "    }")
        self.Player_name.setObjectName("status_label")
        self.horizontalLayout_6.addWidget(self.Player_name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.minimize_button = QtWidgets.QPushButton(self.frame_3)
        self.minimize_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.minimize_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon_sets/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_button.setIconSize(QSize(25,17))
        self.minimize_button.setMaximumSize(QSize(25,17))
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QtCore.QSize(27, 20))
        # self.minimize_button.setFlat(True)
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_6.addWidget(self.minimize_button)
        self.maximize_button = QtWidgets.QPushButton(self.frame_3)
        self.maximize_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.maximize_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon_sets/maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maximize_button.setIcon(icon1)
        self.maximize_button.setIconSize(QSize(25,17))
        self.maximize_button.setMaximumSize(QSize(25,17))
        self.maximize_button.setIconSize(QtCore.QSize(27, 20))
        # self.maximize_button.setFlat(True)
        self.maximize_button.setObjectName("maximize_button")
        self.horizontalLayout_6.addWidget(self.maximize_button)
        self.cross_button = QtWidgets.QPushButton(self.frame_3)
        self.cross_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.cross_button.setText("")
        self.cross_button.setIconSize(QSize(25,17))
        self.cross_button.setMaximumSize(QSize(25,17))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon_sets/cross.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cross_button.setIcon(icon2)
        self.cross_button.setIconSize(QtCore.QSize(27, 20))
        # self.cross_button.setFlat(True)
        self.cross_button.setObjectName("cross_button")
        self.horizontalLayout_6.addWidget(self.cross_button)
        self.verticalLayout.addWidget(self.frame_3)

        self.video_playback = Videowidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(200)
        sizePolicy.setHeightForWidth(self.video_playback.sizePolicy().hasHeightForWidth())
        self.video_playback.setSizePolicy(sizePolicy)
        self.video_playback.setMinimumSize(QtCore.QSize(200, 100))
        self.video_playback.setMouseTracking(False)
        self.video_playback.setTabletTracking(False)
        self.video_playback.setAcceptDrops(False)
        self.video_playback.setAutoFillBackground(False)
        self.video_playback.setObjectName("video_playback")
        self.video_playback.setStyleSheet("background-color:grey")

        
        self.verticalLayout.addWidget(self.video_playback)
        self.pos_frame = QtWidgets.QFrame(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.pos_frame.sizePolicy().hasHeightForWidth())
        self.pos_frame.setSizePolicy(sizePolicy)
        self.pos_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pos_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pos_frame.setObjectName("pos_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.pos_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.position_slider = PosSlider(self.pos_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.position_slider.sizePolicy().hasHeightForWidth())
        self.position_slider.setSizePolicy(sizePolicy)
        self.position_slider.setMouseTracking(True)
        self.position_slider.setAutoFillBackground(False)
        self.position_slider.setStyleSheet("QSlider::handle:horizontal \n"
                                           "    {\n"
                                           "    background: transparent;\n"
                                           "    width: 8px;\n"
                                           "    }\n"
                                           "QSlider::groove:horizontal {\n"
                                           "    border: 1px solid white;\n"
                                           "    height: 8px;\n"
                                           "    background: qlineargradient(y1: 0, y2: 1,stop: 0 #2e3436, stop: 1.0 #353941);\n"
                                           "}\n"
                                           " QSlider::sub-page:horizontal {\n"
                                           "    background:qlineargradient( y1: 0, y2: 1,\n"
                                        "        stop: 0 #42a6db, stop: 1 #0074e0); \n"
                                           "    border: 1px solid white;\n"
                                           "    height: 8px;\n"
                                           "}\n"
                                           "QSlider::handle:horizontal:hover {\n"
                                           "    background: black;\n"
                                           "    height: 8px;\n"
                                           "    width: 8px;\n"
                                           "    border: 1px solid white;\n"
                                           "    }\n"
                                           "")
        self.position_slider.setOrientation(QtCore.Qt.Horizontal)
        self.position_slider.setInvertedAppearance(False)
        self.position_slider.setInvertedControls(False)
        self.position_slider.setObjectName("position_slider")
        self.horizontalLayout.addWidget(self.position_slider)

        self.time_status = QtWidgets.QLabel(self.pos_frame)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.time_status.setFont(font)
        self.time_status.setStyleSheet("QLabel\n"
                                       "    {\n"
                                       "    \n"
                                       "    font: 8pt \"Arial Rounded MT Bold\";\n"
                                       "    color: white;\n"
                                       "    border: 0px solid #076100;\n"
                                       "\n"
                                       "    }")
        self.time_status.setObjectName("time_status")
        self.horizontalLayout.addWidget(self.time_status)

        self.backslash = QtWidgets.QLabel(self.pos_frame)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.backslash.setFont(font)
        self.backslash.setStyleSheet("QLabel\n"
                                     "    {\n"
                                     "    \n"
                                     "    font: 8pt \"Arial Rounded MT Bold\";\n"
                                     "    color: white;\n"
                                     "    border: 0px solid #076100;\n"
                                     "\n"
                                     "    }")
        self.backslash.setObjectName("backslash")
        self.horizontalLayout.addWidget(self.backslash)

        self.duration_status = QtWidgets.QLabel(self.pos_frame)
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.duration_status.setFont(font)
        self.duration_status.setStyleSheet("QLabel\n"
                                           "    {\n"
                                           "    \n"
                                           "    font: 8pt \"Arial Rounded MT Bold\";\n"
                                           "    color: white;\n"
                                           "    border: 0px solid #076100;\n"
                                           "\n"
                                           "    }")
        self.duration_status.setObjectName("duration_status")
        self.horizontalLayout.addWidget(self.duration_status)
        self.verticalLayout.addWidget(self.pos_frame)

        self.frame_2 = QtWidgets.QFrame(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(22)
        # sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())

        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setContentsMargins(0,0,0,0)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setStyleSheet("")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.play_button = QtWidgets.QPushButton(self.frame_2)
        self.play_button.setEnabled(False)
        self.play_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.play_button.setStyleSheet("QPushButton[play=true]{image:url(icon_sets/play/play.png);width:22px;height:22px}\n"

                                        "QPushButton[play=false]{image:url(icon_sets/pause/pause.png);width:22px;height:22px }\n"
                                        )
        self.play_button.setProperty("play", True)
        self.play_button.setText("")
        self.play_button.setObjectName("play_button")
        self.horizontalLayout_4.addWidget(self.play_button)

        self.playback_button = QtWidgets.QPushButton(self.frame_2)
        self.playback_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.playback_button.setStyleSheet("QPushButton{image:url(icon_sets/playback/playback.png);width:22px;height:22px }\n")
        self.playback_button.setText("")
        self.playback_button.setObjectName("playback_button")
        self.horizontalLayout_4.addWidget(self.playback_button)



        self.always_on_top_button = QtWidgets.QPushButton(self.frame_2)
        self.always_on_top_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.always_on_top_button.setStyleSheet("QPushButton[top=false]{image : url(icon_sets/always_on_top/top_off.png) }\n"
                                                
                                                "QPushButton[top=true]{image : url(icon_sets/always_on_top/top_on.png) }\n"
                                                )
        self.always_on_top_button.setProperty("top", True)
        self.always_on_top_button.setText("")
        self.always_on_top_button.setObjectName("always_on_top_button")
        self.horizontalLayout_4.addWidget(self.always_on_top_button)

        self.miniplayer_button = QtWidgets.QPushButton(self.frame_2)
        self.miniplayer_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.miniplayer_button.setStyleSheet("QPushButton[mini=false]{image : url(icon_sets/standard_player/standard.png) }\n"
                                                # "QPushButton[mini=false]:hover{ image:url(icon_sets/standard_player/.png) }\n"
                                                
                                                "QPushButton[mini=true]{image : url(icon_sets/mini_player/mini.png) }\n"
                                                # "QPushButton[mini=true]:hover{ image:url(icon_sets/mini_player/.png) }\n"
                                                 )
        self.miniplayer_button.setProperty("mini",False)
        self.miniplayer_button.setContentsMargins(0,0,0,0)
        self.miniplayer_button.setText("")
        self.miniplayer_button.setObjectName("miniplayer_button")
        self.horizontalLayout_4.addWidget(self.miniplayer_button)

        self.open_File_button = QtWidgets.QPushButton(self.frame_2)
        self.open_File_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.open_File_button.setStyleSheet("QPushButton{image:url(icon_sets/new_file/new_file.png);width:22px;height:22px }\n")
        self.open_File_button.setText("")
        self.open_File_button.setObjectName("playback_button")
        self.horizontalLayout_4.addWidget(self.open_File_button)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        
        self.screenshot_button = QtWidgets.QPushButton(self.frame_2)
        self.screenshot_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.screenshot_button.setStyleSheet("QPushButton{image : url(icon_sets/snapshot/snapshot.png);width:22px;height:22px} \n"
                                            )
        self.screenshot_button.setText("")
        self.screenshot_button.setObjectName("screenshot_button")
        self.horizontalLayout_4.addWidget(self.screenshot_button)


        ''' Video Setting button for Video subs and dubs'''
        # self.video_setting_button = QtWidgets.QPushButton(self.frame_2)
        # self.video_setting_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        # self.video_setting_button.setText("")
        # self.video_setting_button.setIconSize(QtCore.QSize(22, 22))
        # self.video_setting_button.setStyleSheet("QPushButton{image : url(icon_sets/video_setting/video_settings.png) }\n"
        #                                         )
        # self.video_setting_button.setObjectName("video_setting_button")
        # self.horizontalLayout_4.addWidget(self.video_setting_button)

        self.setting_button = QtWidgets.QPushButton(self.frame_2)
        self.setting_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.setting_button.setStyleSheet("QPushButton{image : url(icon_sets/settings/settings.png) }\n"
                                        )
        self.setting_button.setText("")
        self.setting_button.setObjectName("setting_button")
        self.horizontalLayout_4.addWidget(self.setting_button)

        self.Quality_box = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Quality_box.sizePolicy().hasHeightForWidth())
        self.Quality_box.setSizePolicy(sizePolicy)
        self.Quality_box.setStyleSheet("QComboBox\n"
                                       "    {\n"
                                       "	border-image :url(icon_sets/quality/border.png);\n"
                                       "    color: #fcffff;\n"
                                       "    font-size: 8pt;\n"
                                       "    font-weight: bold;\n"
                                    #    "    width: 41px;\n"
                                       "    background-color: #353941;\n"
                                       "    }\n"
                                       "    QComboBox QAbstractItemView \n"
                                       "    {\n"
                                       "    background: #fcffff;\n"
                                       "    border: 2px solid darkgray;\n"
                                       "    selection-background-color: #353941;\n"
                                       "    }\n"
    
                                       "QComboBox::drop-down {\n"
                                       "    border: 0px;\n"
                                       "    subcontrol-origin: padding;\n"
                                       "    subcontrol-position: top right;\n"
                                       "\n"
                                       "    border-top-right-radius: 3px;\n"
                                       "    border-bottom-right-radius: 3px;\n"
                                       "}\n"
                                       )
        self.Quality_box.setIconSize(QtCore.QSize(0, 0))
        self.Quality_box.setDuplicatesEnabled(False)
        self.Quality_box.setObjectName("comboBox")
        self.Quality_box.addItem("     -")
        self.horizontalLayout_4.addWidget(self.Quality_box)

        self.volume_button = QtWidgets.QPushButton(self.frame_2)
        self.volume_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.volume_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon_sets/volume/volume1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.volume_button.setIcon(icon9)
        self.volume_button.setIconSize(QtCore.QSize(22, 22))
        self.volume_button.setCheckable(True)
        # self.volume_button.setFlat(True)
        self.volume_button.setObjectName("volume_button")
        self.horizontalLayout_4.addWidget(self.volume_button)

        self.volumeslider = VolSlider(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumeslider.sizePolicy().hasHeightForWidth())
        self.volumeslider.setSizePolicy(sizePolicy)
        self.volumeslider.setAutoFillBackground(False)
        self.volumeslider.setStyleSheet("QSlider::handle:horizontal \n"
                                        "    {\n"
                                        "    background: transparent;\n"
                                        "    width: 5px;\n"
                                        "    }\n"
                                        "QSlider::groove:horizontal {\n"
                                        "    border: 1px solid #444444;\n"
                                        "    height: 5px;\n"
                                        "    background: qlineargradient(y1: 0, y2: 1,stop: 0 grey, stop: 1.0 grey);\n"
                                        "}\n"
                                        " QSlider::sub-page:horizontal {\n"
                                        "    background:qlineargradient( y1: 0, y2: 1,\n"
                                        "        stop: 0 #42a6db, stop: 1 #0074e0); \n"
                                        "    border: 1px solid #777;\n"
                                        "    height: 5px;\n"
                                        "}\n"
                                        "QSlider::handle:horizontal:hover {\n"
                                        "    background: #353941;\n"
                                        "    height: 5px;\n"
                                        "    width: 5px;\n"
                                        "    border: 1px solid #0074e0;\n"
                                        "    }\n"
                                        "QSlider::sub-page:horizontal:disabled{background:qlineargradient( y1: 0, y2: 1,\n"
                                        "        stop: 0 #909090, stop: 1 #A8A8A8 );}\n"
                                        "")
        self.volumeslider.setOrientation(QtCore.Qt.Horizontal)
        self.volumeslider.setObjectName("volume_slider")
        self.horizontalLayout_4.addWidget(self.volumeslider)

        self.volume_percentage  = QtWidgets.QLabel(self.frame_2)
        self.volume_percentage.setStyleSheet("QLabel\n"
                                        "    {\n"
                                        "    font: 7pt \"Arial Rounded MT Bold\";\n"
                                        "    color: white;\n"
                                        "    border: 0px solid #076100;\n"
                                        "    }")
        self.volume_percentage.setObjectName("volume_status")
        self.volume_percentage.setMinimumWidth(35)
        self.volume_percentage.setText(" 20 %")
        self.horizontalLayout_4.addWidget(self.volume_percentage)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QtWidgets.QFrame(self.mainFrame)
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        sizegrip_2 = QtWidgets.QSizeGrip(Form)
        sizegrip_2.setStyleSheet("image:url(icon_sets/.png)")
        self.horizontalLayout_5.addWidget(sizegrip_2, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeft)
        
        # self.enter_url_label = QtWidgets.QLabel(self.frame)
        # font = QtGui.QFont()
        # font.setFamily("Arial Rounded MT Bold")
        # font.setPointSize(8)
        # font.setBold(False)
        # font.setItalic(False)
        # font.setWeight(50)
        # self.enter_url_label.setFont(font)
        # self.enter_url_label.setStyleSheet("QLabel\n"
        #                                    "    {\n"
        #                                    "    \n"
        #                                    "    font: 8pt \"Arial Rounded MT Bold\";\n"
        #                                    "    color: white;\n"
        #                                    "    border: 0px solid #076100;\n"
        #                                    "    }")
        # self.enter_url_label.setObjectName("enter_url_label")
        # self.horizontalLayout_5.addWidget(self.enter_url_label)
        
    
        self.url_box = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.url_box.sizePolicy().hasHeightForWidth())
        self.url_box.setSizePolicy(sizePolicy)
        self.url_box.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.url_box.setMouseTracking(False)
        self.url_box.setAcceptDrops(False)
        self.url_box.setWhatsThis("")
        self.url_box.setAccessibleDescription("")
        self.url_box.setAutoFillBackground(True)
        self.url_box.setStyleSheet("QComboBox\n"
                                   "    {\n"
                                   "    border: 2px solid #0074e0;\n"
                                   "    color: #fcffff;\n"
                                   "    font-size: 10pt;\n"
                                   "    font-family: Arial;\n"
                                   "    font-weight: Bold;\n"
                                   "    background-color: #353941;\n"
                                   "    border-radius: 5px;\n"
                                   "    }\n"
                                   "    QComboBox QAbstractItemView \n"
                                   "    {\n"
                                   "    background: #dddddd;\n"
                                   "    border: 2px solid darkgray;\n"
                                   "    selection-background-color: #5a5a5a;\n"
                                   "    }\n"
                                   "QComboBox::down-arrow {\n"
                                   "    width : 20px\n"
                                   "    background-color: #5f85db\n"
                                   "}\n"
                                   "QComboBox::down-arrow:pressed\n"
                                   "{\n"
                                   "background-color : #5f85db;\n"
                                   "}\n"
                                   "QComboBox::drop-down {\n"
                                   "    subcontrol-origin: padding;\n"
                                   "    subcontrol-position: top right;\n"
                                   "    width: 20px;\n"
                                   " \n"
                                   "    border-top-right-radius: 3px;\n"
                                   "    border-bottom-right-radius: 3px;\n"
                                   "}")
        self.url_box.setInputMethodHints(QtCore.Qt.ImhUrlCharactersOnly)
        
        self.url_box.setEditable(True)
        
        self.url_box.setMaxVisibleItems(100)
        self.url_box.setMaxCount(100)
        self.url_box.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.url_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.url_box.setMinimumContentsLength(2)
        self.url_box.setIconSize(QtCore.QSize(20, 20))
        self.url_box.setDuplicatesEnabled(False)
        self.url_box.setFrame(True)
        self.url_box.setObjectName("url_box")
        
        self.horizontalLayout_5.addWidget(self.url_box)
        

        self.playOnline_button = QtWidgets.QPushButton(self.frame)
        self.playOnline_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.playOnline_button.setStyleSheet("QPushButton{image : url(icon_sets/globe.png) }\n")
        self.playOnline_button.setText("")
        self.playOnline_button.setObjectName("playOnline_button")
        self.horizontalLayout_5.addWidget(self.playOnline_button)


        self.verticalLayout.addWidget(self.frame)

        sizegrip_1 = QtWidgets.QSizeGrip(Form)
        sizegrip_1.setStyleSheet("image:url(icon_sets/size.png);width:15; height:18;")
        self.horizontalLayout_5.addWidget(sizegrip_1, 0, QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.mainFrame)

        self.retranslateUi(Form)
        self.url_box.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Q-Stream Player"))
        self.Player_name.setText(_translate("Form", "Q-Stream Player"))
        self.time_status.setText(_translate("Form", "00:00:00"))
        self.backslash.setText(_translate("Form", "/"))
        self.duration_status.setText(_translate("Form", "00:00:00"))
        # self.enter_url_label.setText(_translate("Form", statusList[4]))





        # Set intial Volume
        self.volumeslider.setRange(0, 100)
        self.volumeslider.setValue(20)
        self.mediaPlayer.setVolume(20)
        self.position_slider.setRange(0, 100)

        # connecting buttons
        self.miniplayer_button.clicked.connect(self.setupMiniPlayer)
        self.position_slider.sliderMoved.connect(self.setPosition)
        self.position_slider.sliderMoved.connect(self.handleLabel)
        self.volume_button.clicked.connect(self.mute)
        self.volumeslider.valueChanged.connect(self.setVolume)
        self.screenshot_button.clicked.connect(self.screenshot)
        self.playback_button.clicked.connect(self.stopplayback)
        self.always_on_top_button.clicked.connect(self.checkOnTop)
        self.play_button.clicked.connect(self.play)
        self.open_File_button.clicked.connect(self.openFile)
        # self.video_setting_button.clicked.connect(self.handleQuality)
        self.setting_button.clicked.connect(self.handleSetting)
        self.Quality_box.currentTextChanged.connect(self.handleQuality)
        self.cross_button.clicked.connect(self.exit)
        self.maximize_button.clicked.connect(self.max)
        self.minimize_button.clicked.connect(self.min)
        self.playOnline_button.clicked.connect(self.onlineThread)

        # Shortcuts
        shortcut = QShortcut(QKeySequence('Esc'), self.video_playback)
        shortcut.activated.connect(self.EscFun)
        shortcut = QShortcut(QKeySequence('Space'), self.video_playback)
        shortcut.activated.connect(self.play)
        shortcut = QShortcut(QKeySequence('f'), self.video_playback)
        shortcut.activated.connect(self.fullscreen_video)
        shortcut = QShortcut(QKeySequence('c'), self.video_playback)
        shortcut.activated.connect(self.setupMiniPlayer)
        shortcut = QShortcut(QKeySequence('o'), self.video_playback)
        shortcut.activated.connect(self.openFile)
        shortcut = QShortcut(QKeySequence('a'), self.video_playback)
        shortcut.activated.connect(self.checkOnTop)
        shortcut = QShortcut(QKeySequence("Return"), self.video_playback)
        shortcut.activated.connect(self.onlineThread)
        shortcut = QShortcut(QKeySequence('m'), self.video_playback)
        shortcut.activated.connect(self.mute)
        shortcut = QShortcut(QKeySequence(Qt.Key_Right), self.video_playback)
        shortcut.activated.connect(self.forwardSlider)
        shortcut = QShortcut(QKeySequence(Qt.Key_Left), self.video_playback)
        shortcut.activated.connect(self.backSlider)
        self.volupshortcut = QShortcut(QKeySequence(Qt.Key_Up), self.video_playback)
        self.volupshortcut.activated.connect(self.volumeUp)
        self.voldownshortcut = QShortcut(QKeySequence(Qt.Key_Down), self.video_playback)
        self.voldownshortcut.activated.connect(self.volumeDown)
        shortcut = QShortcut(QKeySequence(Qt.ControlModifier + Qt.Key_Right), self.video_playback)
        shortcut.activated.connect(self.forwardSlider10)
        shortcut = QShortcut(QKeySequence(Qt.ControlModifier + Qt.Key_Left), self.video_playback)
        shortcut.activated.connect(self.backSlider10)
        shortcut = QShortcut(QKeySequence(Qt.AltModifier + Qt.Key_Left), self.video_playback)
        shortcut.activated.connect(self.backSlider5)
        shortcut = QShortcut(QKeySequence(Qt.AltModifier + Qt.Key_Right), self.video_playback)
        shortcut.activated.connect(self.forwardSlider5)

        # loading history to Url Box
        items = self.load()
        self.url_box.addItems(items)
        self.url_box.setCurrentIndex(-1)

        # icon size
        # iconSize = QSize(5,5)
        # self.play_button.setIconSize(iconSize)
        # self.playback_button.setIconSize(iconSize)
        # self.screenshot_button.setIconSize(iconSize)
        # self.always_on_top_button.setIconSize(iconSize)
        # self.miniplayer_button.setIconSize(iconSize)
        # self.setting_button.setIconSize(iconSize)
        # self.volume_button.setIconSize(iconSize)

        # button size 
        btnSize = QSize(22,22)
        self.play_button.setMaximumSize(btnSize)
        self.playback_button.setMaximumSize(btnSize)
        self.screenshot_button.setMaximumSize(btnSize)
        self.always_on_top_button.setMaximumSize(btnSize)
        self.miniplayer_button.setMaximumSize(btnSize)
        # self.video_setting_button.setMaximumSize(btnSize)
        self.setting_button.setMaximumSize(btnSize)
        self.volume_button.setMaximumSize(btnSize)



        # set margin
        self.horizontalLayout.setContentsMargins(10, 5, 9, 0)
        self.horizontalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_5.setContentsMargins(0, 5, 5, 5)
        self.horizontalLayout_6.setContentsMargins(9, 0, 9, 0)

        # Media player settings
        self.mediaPlayer.setVideoOutput(self.video_playback)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.positionChanged.connect(self.handleLabel)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        

    def handleLabel(self):
        self.time_status.clear()
        mtime = QtCore.QTime(0, 0, 0, 0)
        self.time = mtime.addMSecs(self.mediaPlayer.position())
        self.time_status.setText(self.time.toString())
    

    def hide_all(self):
        self.frame_3.close()
        # self.frame.close()
        self.url_box.close()
        self.playOnline_button.close()
        self.playback_button.close()
        self.screenshot_button.close()
        self.Quality_box.close()
        self.volume_button.close()
        # self.video_setting_button.close()
        # self.setting_button.close()

    def show_all(self):
        self.frame_3.show()
        # self.frame.show()
        self.url_box.show()
        self.playOnline_button.show()
        self.playback_button.show()
        self.screenshot_button.show()
        self.Quality_box.show()
        self.volume_button.show()
        # self.video_setting_button.show()
        self.setting_button.show()

    def checkOnTop(self):
        self.isOnTop = not self.isOnTop
        if self.isOnTop:
            self.always_on_top_button.setProperty("top", True)
            self.always_on_top_button.setStyle(self.always_on_top_button.style())
            Form.setWindowFlags(Form.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        else:
            self.always_on_top_button.setProperty("top", False)
            self.always_on_top_button.setStyle(self.always_on_top_button.style())
            Form.setWindowFlags(Form.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
        Form.show()

    def miniProperty(self):
        self.video_playback.setMinimumSize(QSize(200,100))
        # self.video_playback.resize(QSize(550,270))
        # Form.resize(QSize(550,270))
        Form.setMinimumSize(QSize(200,175))
        self.mainFrame.setMinimumSize(QSize(200,60))
        # self.mainFrame.resize(QSize(200,53))

    def standardProperty(self):
        self.video_playback.setMinimumSize(QSize(200,100))
        self.mainFrame.setMinimumSize(QSize(200,82))
        Form.setMinimumSize(QSize(200,202))
        # Form.resize(550, 369)

    def setupMiniPlayer(self):
        self.isMini = not self.isMini
        if self.isMini :
            self.miniplayer_button.setProperty("mini",True)
            self.miniplayer_button.setStyle(self.miniplayer_button.style())
            self.hide_all()
            self.miniProperty()
            
        else:
            self.miniplayer_button.setProperty("mini",False)
            self.miniplayer_button.setStyle(self.miniplayer_button.style())
            self.standardProperty()
            
            self.show_all()

    @staticmethod
    def load():
        scorefile = "db.bat"
        if os.path.exists(scorefile):
            with open(scorefile, 'rb') as sf:
                scores = pickle.load(sf)
        else:
            scores = []

        with open(scorefile, "wb") as sf:
            pickle.dump(scores, sf)
        return scores

    
    @staticmethod
    def scor_func(url):
        scorefile = "db.bat"
        if os.path.exists(scorefile):
            with open(scorefile, 'rb') as sf:
                scores = pickle.load(sf)
        else:
            scores = []
        scores.append(url)

        with open(scorefile, "wb") as sf:
            if len(scores) > 100:
                print("here", scores)
                scores = scores[1:]
            pickle.dump(scores, sf)
        return scores

    def mute(self):
        if self.mediaPlayer.isMuted() :
            print('[ ! Full Volume]')
            self.mediaPlayer.setMuted(False)
            icon9 = QtGui.QIcon()
            icon9.addPixmap(QtGui.QPixmap("icon_sets/volume/volume1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.volume_button.setIcon(icon9)
            self.volume_button.setIconSize(QSize(22,22))
            self.volumeslider.setEnabled(True)
            # shortcut Enable
            self.volupshortcut.setEnabled(True)
            self.voldownshortcut.setEnabled(True)
    
        else:
            print('[ ! Mute Volume]')
            self.mediaPlayer.setMuted(True)
            icon9 = QtGui.QIcon()
            icon9.addPixmap(QtGui.QPixmap("icon_sets/volume/volume2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.volume_button.setIcon(icon9)
            self.volume_button.setIconSize(QSize(22,22))
            self.volumeslider.setEnabled(False) 
            # shrotcut disable
            self.volupshortcut.setEnabled(False)
            self.voldownshortcut.setEnabled(False)
    
    

    def play(self):
        if self.mediaPlayer.isVideoAvailable():
            if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
                print("[ ! PAUSE PRESSED ]")
                self.mediaPlayer.pause()
            else:
                print("[ ! PLAY PRESSED ]")
                self.mediaPlayer.play()

    def onlineThread(self):
        '''  Thread to Handle fetching of Urls from API'''
        import threading
        urlThread = threading.Thread(target= self.playOnline)
        print("Url Thread Start ")
        urlThread.start()
        print("Url Thread waiting to complete ")
        # urlThread.join()
        print("Url Thread complete ")

    def playOnline(self):
        if self.url_box.currentText() != '':
            print('[ ! GETTING VIDEO ONLINE ]')
            fileName = self.url_box.currentText()
            # res = requests.get('https://mediaplayerserver.herokuapp.com/', params={"key": fileName})
            res = requests.get('https://q-stream-media-player.herokuapp.com/', params={"key": fileName})
            try:
                self.streams = json.loads(res.text)
                try:
                    self.mediaPlayer.setMedia(QMediaContent(QUrl(self.streams['best'])))
                    self.play_video()
                    self.isOnline = True
                    self.addQuality()
                    if self.url_box.findText(fileName, Qt.MatchExactly) < 0:
                        self.url_box.addItem(fileName)
                        self.scor_func(fileName)
                except KeyError:
                    print("[ ! Error Video Not Supported By platform]")
            except json.JSONDecodeError:
                print("[ ! Error NoPluginError]")
            finally:
                self.url_box.clearEditText()
                self.url_box.clearFocus()

    def openFile(self):
        '''Open File from System'''
        print('[ ! OPEN FILE ]')
        username = getpass.getuser()
        if sys.platform == 'win32':
            path = 'C:/Users/' + username + '/Videos/'
        elif sys.platform == 'linux' or sys.platform == 'Darwin':    
            path = '/home/' + username + '/Videos/' 

        
        fileName, _ = QFileDialog.getOpenFileName(self.video_playback, "Select media file",
                path, "Video Files (*.mp3 *.mp4 *.flv *.ts *.mts *.avi *.mkv)")
        if fileName != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(fileName)))
            self.play_video()

    
    def play_video(self):
        '''Toggle between play and pause of `Button` State '''
        print('[ ! PLAYING VIDEO ]')
        self.play_button.setEnabled(True)
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()
    
    def mediaStateChanged(self, state):
        '''Toggle between play and pause of `Video` State '''
        print('[ ! CHANGING MEDIA STATE ]')
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.play_button.setProperty('play',False)
            self.play_button.setStyle(self.play_button.style())    
        else:
            self.play_button.setProperty('play',True)
            self.play_button.setStyle(self.play_button.style())
            

    def stopplayback(self):
        '''To play Video from start'''
        print('[ ! STOP PLAYBACK VIDEO ]')
        self.mediaPlayer.stop()
        self.play_video()

    def positionChanged(self, position):
        '''Set Player Video to postion fetch by slider'''
        print('[ ! POSITION CHANGED ]')
        self.position_slider.setValue(position)

    def durationChanged(self, duration):
        '''handle duration lables and change whenever it changes'''
        print('[ ! DURATION CHANGED ]')
        self.position_slider.setRange(0, duration)
        self.duration_status.clear()
        mtime = QtCore.QTime(0, 0, 0, 0)
        time = mtime.addMSecs(self.mediaPlayer.duration())
        self.duration_status.setText(time.toString())

    
    def setPosition(self, position):
        '''Set Video to a specific position'''
        print('[ ! POSITION SET ]')
        self.mediaPlayer.setPosition(position)

    def setVolumePos(self, remain):
        '''Set Volume slider value according to volume'''
        print('[ ! REMANING VOLUME ]')
        print(remain)
        self.volumeslider.setRange(remain, 100)

    def setVolume(self, vol):
        '''Handle Volume Button icon and mediaPlayer volume'''
        print('[ ! SET VOLUME ]')
        print("set volume  = " + str(vol))
        if vol >= 0 and vol <= 100 :
            self.volume_percentage.setText(" " + str(vol) + " %")
        if vol <= 0:
            icon9 = QtGui.QIcon()
            icon9.addPixmap(QtGui.QPixmap("icon_sets/volume/volume2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.volume_button.setIcon(icon9)
        else:
            icon9 = QtGui.QIcon()
            icon9.addPixmap(QtGui.QPixmap("icon_sets/volume/volume1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.volume_button.setIcon(icon9)

        self.volumeslider.setValue(vol)
        self.mediaPlayer.setVolume(vol)

    def screenshot(self):
        '''Capture Only screen size of player window using screen cordinates.
        Save to Default Pictures dictoary in System.
        Save in png format.
        '''
        print('[ ! SCREENSHOT ]')
        # Getting player Window coordintes
        wincen = Form.geometry()

        topX = wincen.topLeft().x()
        topY = wincen.topLeft().y()
        
        geo = self.video_playback.geometry()
        
        # Region is calcutaed using Video screen size and player window size
        image = pyautogui.screenshot(region=(topX, topY + 38, geo.width(), geo.height()-35))

        filename = "screenshot" + str(uuid.uuid4()) + ".png"
        username = getpass.getuser()

        if sys.platform == 'win32':
            path = 'C:/Users/' + username + '/Pictures/' + filename
        elif sys.platform == 'linux' or sys.platform == 'Darwin':    
            path = '/home/' + username + '/Pictures/' + filename
        image.save(path)
        

    def EscFun(self):
        '''To disable FullScreen Mode'''
        if self.video_playback.isFullScreen():
            Form.show()
            self.video_playback.setFullScreen(False)

    def fullscreen_video(self):
        '''To get into Fullscreen Mode and Normal Mode'''
        if self.mediaPlayer.isVideoAvailable():
            if self.video_playback.isFullScreen():
                self.video_playback.setFullScreen(False)
                print('[ ! Normal Screen ]')
                Form.show()
            else:
                print('[ ! Full Screen ]')
                self.video_playback.setFullScreen(True)
                Form.hide()
            

                
    def getFormat(self):
        '''Remove the audio formates which are Recived by Youtube link ( if exists )'''
        li = list(self.streams.keys())
        for q in li:
            if q.startswith('audio'):
                li.remove(q)
                try:
                    li.remove('audio_opus')
                except ValueError:
                    pass
        return li


    def changeQuality(self, quality):
        '''To change Video Quality according to User need and maintain postion of video'''
        pos = self.mediaPlayer.position()
        try:
            self.mediaPlayer.setMedia(QMediaContent(QUrl(self.streams[quality])))
        except KeyError:
            pass
        self.setPosition(pos)
        self.mediaPlayer.play()
        self.Quality_box.clearFocus()

    @staticmethod
    def handleSetting():
        '''Open Setting Dialog Box '''
        from lib.setting import SettingDialog
        dlg = SettingDialog()
        dlg.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        dlg.exec_()

    def addQuality(self):
        '''Set DropDown menu of Video resolution available'''
        self.Quality_box.clear()
        self.Quality_box.addItems(self.getFormat())

    def handleQuality(self):
        if self.isOnline:
            self.changeQuality(self.Quality_box.currentText())

            

    def forwardSlider(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + 1000)

    def forwardSlider10(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + 10000)

    def forwardSlider5(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() + 5000)

    def backSlider(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - 1000)

    def backSlider10(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - 10000)

    def backSlider5(self):
        self.mediaPlayer.setPosition(self.mediaPlayer.position() - 5000)

    def volumeUp(self):
        self.setVolume(self.mediaPlayer.volume() + 10)
        print("Volume: " + str(self.mediaPlayer.volume()))

    def volumeDown(self):
        self.setVolume(self.mediaPlayer.volume() - 10)
        print("Volume: " + str(self.mediaPlayer.volume()))

    @staticmethod
    def max():
        if not Form.isMaximized():
            print("[! Window is Maximized]")
            Form.showMaximized()
        else:
            print("[! Window is Normal]")
            Form.showNormal()

    @staticmethod
    def min():
        if not Form.isMinimized():
            print("[! Window is Minimized]")
            Form.showMinimized()
        else:
            print("[! Window is Normal]")
            Form.showNormal()

    def exit(self):
        self.mediaPlayer.stop()
        sys.exit()


if __name__ == "__main__":
    import sys
    import sys

    with open("lang.bat", 'rb') as sf:
        langs = pickle.load(sf)
        statusList = langs['present']

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('play-button.ico'))
    # Form = QtWidgets.QWidget()
    Form = window()
    Form.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog, QTableWidgetItem


class Ui_Playlist(QDialog):

    def __init__(self, playlist_data):
        super(Ui_Playlist, self).__init__()
        self.playlist_data = playlist_data



    def setupUi(self):
        self.setObjectName("Playlist")
        self.resize(603, 477)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.playlistTable = QtWidgets.QTableWidget(self)
        self.playlistTable.setObjectName("playlistTable")
        self.playlistTable.setColumnCount(1)
        self.playlistTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.playlistTable.setHorizontalHeaderItem(0, item)
        self.verticalLayout.addWidget(self.playlistTable)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playall_button = QtWidgets.QPushButton(self.widget)
        self.playall_button.setMinimumSize(QtCore.QSize(85, 28))
        self.playall_button.setObjectName("playall_button")
        self.horizontalLayout.addWidget(self.playall_button)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.moveup_button = QtWidgets.QPushButton(self.widget)
        self.moveup_button.setMinimumSize(QtCore.QSize(90, 0))
        self.moveup_button.setObjectName("moveup_button")
        self.horizontalLayout.addWidget(self.moveup_button)
        self.movedown_button = QtWidgets.QPushButton(self.widget)
        self.movedown_button.setMinimumSize(QtCore.QSize(90, 0))
        self.movedown_button.setObjectName("movedown_button")
        self.horizontalLayout.addWidget(self.movedown_button)
        self.delete_button = QtWidgets.QPushButton(self.widget)
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout.addWidget(self.delete_button)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.load_button = QtWidgets.QPushButton(self.widget)
        self.load_button.setObjectName("load_button")
        self.horizontalLayout.addWidget(self.load_button)
        self.save_button = QtWidgets.QPushButton(self.widget)
        self.save_button.setMinimumSize(QtCore.QSize(90, 0))
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Playlist", "Form"))
        header = self.playlistTable.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        item = self.playlistTable.horizontalHeaderItem(0)
        item.setText(_translate("Playlist", "Name"))

        self.playall_button.setText(_translate("Playlist", "Play"))
        self.moveup_button.setText(_translate("Playlist", "Move Up"))
        self.movedown_button.setText(_translate("Playlist", "Move down"))
        self.delete_button.setText(_translate("Playlist", "Delete"))
        self.load_button.setText(_translate("Playlist", "Load"))
        self.save_button.setText(_translate("Playlist", "Save"))

    def updatePlaylistData(self, playlist):
        self.playlist_data = playlist

    def loadData(self):
        self.playlistTable.setRowCount(len(self.playlist_data))
        for index, media in enumerate(self.playlist_data):
            self.playlistTable.setItem(0, index, QTableWidgetItem(media['src']))
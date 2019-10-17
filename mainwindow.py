# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(483, 244)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(483, 244))
        icon = QtGui.QIcon('pdfmerge-icon.png')
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(380, 10, 92, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAdd = QtWidgets.QPushButton(self.layoutWidget)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout.addWidget(self.btnAdd)
        self.btnRemove = QtWidgets.QPushButton(self.layoutWidget)
        self.btnRemove.setObjectName("btnRemove")
        self.verticalLayout.addWidget(self.btnRemove)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnCombine = QtWidgets.QPushButton(self.layoutWidget)
        self.btnCombine.setObjectName("btnCombine")
        self.verticalLayout.addWidget(self.btnCombine)
        self.lstFiles = QtWidgets.QListWidget(self.centralwidget)
        self.lstFiles.setGeometry(QtCore.QRect(10, 10, 361, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lstFiles.sizePolicy().hasHeightForWidth())
        self.lstFiles.setSizePolicy(sizePolicy)
        self.lstFiles.setAcceptDrops(False)
        self.lstFiles.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lstFiles.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lstFiles.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lstFiles.setLineWidth(1)
        self.lstFiles.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.lstFiles.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.lstFiles.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lstFiles.setResizeMode(QtWidgets.QListView.Fixed)
        self.lstFiles.setObjectName("lstFiles")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pdfmerge-gui"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnRemove.setText(_translate("MainWindow", "Remove"))
        self.btnCombine.setText(_translate("MainWindow", "Combine"))

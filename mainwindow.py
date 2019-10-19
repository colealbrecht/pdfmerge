from PyQt5 import QtCore, QtGui, QtWidgets
from DDListWidget import DDListWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        # Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(485, 245)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setFixedSize(QtCore.QSize(525, 275))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pdfmerge-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        # Central Widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        
        # <Grid Layout>
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(5, 5, 515, 240))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # <Vertical Layout>
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Add Button
        self.btnAdd = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAdd.setObjectName("btnAdd")
        self.verticalLayout.addWidget(self.btnAdd)
        
        # Remove Button
        self.btnRemove = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnRemove.setObjectName("btnRemove")
        self.verticalLayout.addWidget(self.btnRemove)
        
        # Spacer between Add/Remove buttons and Combine button
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnCombine = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnCombine.setObjectName("btnCombine")
        self.verticalLayout.addWidget(self.btnCombine)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        # </VerticalLayout>

        # File ListWidget
        self.lstFiles = DDListWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lstFiles.sizePolicy().hasHeightForWidth())
        self.lstFiles.setSizePolicy(sizePolicy)
        self.lstFiles.setAcceptDrops(True)
        self.lstFiles.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lstFiles.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lstFiles.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lstFiles.setLineWidth(1)
        self.lstFiles.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.lstFiles.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.lstFiles.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lstFiles.setResizeMode(QtWidgets.QListView.Fixed)
        self.lstFiles.setObjectName("lstFiles")
        self.gridLayout.addWidget(self.lstFiles, 0, 0, 1, 1)

        # </Grid Layout>


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lstFiles, self.btnAdd)
        MainWindow.setTabOrder(self.btnAdd, self.btnRemove)
        MainWindow.setTabOrder(self.btnRemove, self.btnCombine)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pdfmerge"))
        self.btnAdd.setText(_translate("MainWindow", "Add"))
        self.btnRemove.setText(_translate("MainWindow", "Remove"))
        self.btnCombine.setText(_translate("MainWindow", "Combine"))

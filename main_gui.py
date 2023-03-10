# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1677, 872)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(100, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1648999, 99999))
        MainWindow.setMouseTracking(True)
        MainWindow.setToolTipDuration(3)
        MainWindow.setStyleSheet("        background-color: rgb(235,245,255);\n"
"border:none;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(250, 250, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.mainFrame.setStyleSheet("background-color: rgb(250, 250, 255);")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 9)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sideBar = QtWidgets.QFrame(self.mainFrame)
        self.sideBar.setEnabled(True)
        self.sideBar.setMinimumSize(QtCore.QSize(208, 400))
        self.sideBar.setMaximumSize(QtCore.QSize(210, 16777215))
        self.sideBar.setStyleSheet("QFrame{\n"
"border-radius:15px;\n"
"        background-color: rgb(170,200,255);\n"
"border: 0px solid gray;\n"
"border-color: rgb(190, 190, 190);\n"
"}")
        self.sideBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sideBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sideBar.setObjectName("sideBar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sideBar)
        self.verticalLayout.setContentsMargins(0, 10, 0, 9)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnMenu = QtWidgets.QPushButton(self.sideBar)
        self.btnMenu.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnMenu.setFont(font)
        self.btnMenu.setStyleSheet("QPushButton{\n"
"        background-color: rgb(170,200,255);\n"
"    border:none;\n"
"\n"
"        color: rgb(30, 39, 73);\n"
"\n"
"text-align: center;\n"
"padding-bottom: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(30, 39, 73);\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.btnMenu.setCheckable(False)
        self.btnMenu.setObjectName("btnMenu")
        self.verticalLayout.addWidget(self.btnMenu)
        self.line_2 = QtWidgets.QFrame(self.sideBar)
        self.line_2.setMinimumSize(QtCore.QSize(0, 1))
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.btnMenuGattMaker = QtWidgets.QPushButton(self.sideBar)
        self.btnMenuGattMaker.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnMenuGattMaker.setFont(font)
        self.btnMenuGattMaker.setStyleSheet("QPushButton{\n"
"        background-color: rgb(170,200,255);\n"
"    border:none;\n"
"\n"
"        color: rgb(30, 39, 73);\n"
"\n"
"text-align: left;\n"
"padding-left: 30px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(30, 39, 73);\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.btnMenuGattMaker.setObjectName("btnMenuGattMaker")
        self.verticalLayout.addWidget(self.btnMenuGattMaker)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.sideBar)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 210))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 999999))
        self.frame_3.setStyleSheet("border: 0px solid gray;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(0, 100, 206, 1))
        self.line.setMinimumSize(QtCore.QSize(0, 1))
        self.line.setMaximumSize(QtCore.QSize(16777215, 1))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.line.setFont(font)
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.btnauthor = QtWidgets.QPushButton(self.frame_3)
        self.btnauthor.setGeometry(QtCore.QRect(30, 110, 191, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnauthor.setFont(font)
        self.btnauthor.setStyleSheet("text-align: left;\n"
"padding-left: 0px;\n"
"color: rgb(30, 39, 73);\n"
"        background-color: rgb(170,200,255);")
        self.btnauthor.setObjectName("btnauthor")
        self.btnRepo = QtWidgets.QPushButton(self.frame_3)
        self.btnRepo.setGeometry(QtCore.QRect(20, 160, 161, 30))
        self.btnRepo.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnRepo.setFont(font)
        self.btnRepo.setStyleSheet("QPushButton{\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"border-radius:5px;\n"
"background-color: rgb(39, 52, 105);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(29, 42,95);\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    \n"
"        color: rgb(255, 255, 255);\n"
"background-color: rgb(48, 52, 63);\n"
"}")
        self.btnRepo.setObjectName("btnRepo")
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout_3.addWidget(self.sideBar)
        self.frame_5 = QtWidgets.QFrame(self.mainFrame)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setStyleSheet("background-color: rgb(250, 250, 255);\n"
"border-radius:15px;\n"
"border: 0px solid gray;\n"
"border-color: rgb(190, 190, 190);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stackedWidget = SlidingStackedWidget(self.frame_5)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setMouseTracking(True)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet("border: 0px solid gray;")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_Gatt_Maker = QtWidgets.QWidget()
        self.page_Gatt_Maker.setStyleSheet("border-radius:15px;")
        self.page_Gatt_Maker.setObjectName("page_Gatt_Maker")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.page_Gatt_Maker)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.middle_frame = QtWidgets.QFrame(self.page_Gatt_Maker)
        self.middle_frame.setMinimumSize(QtCore.QSize(0, 400))
        self.middle_frame.setMaximumSize(QtCore.QSize(1812, 2000))
        self.middle_frame.setStyleSheet("background-color: rgb(255,255, 255);\n"
"border-radius:15px;")
        self.middle_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.middle_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.middle_frame.setObjectName("middle_frame")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.middle_frame)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(9)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_designer_left = QtWidgets.QFrame(self.middle_frame)
        self.frame_designer_left.setMinimumSize(QtCore.QSize(400, 0))
        self.frame_designer_left.setToolTip("")
        self.frame_designer_left.setStatusTip("")
        self.frame_designer_left.setWhatsThis("")
        self.frame_designer_left.setStyleSheet("border: 0px solid gray;\n"
"border-color: rgb(190, 190, 190);")
        self.frame_designer_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_designer_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_designer_left.setObjectName("frame_designer_left")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_designer_left)
        self.horizontalLayout_15.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout_15.setSpacing(20)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_7 = QtWidgets.QFrame(self.frame_designer_left)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_7.setStyleSheet("border: 0px solid gray;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.left_frame = QtWidgets.QFrame(self.frame_7)
        self.left_frame.setMinimumSize(QtCore.QSize(100, 100))
        self.left_frame.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.left_frame.setStyleSheet("border: 1px solid gray;\n"
"border-color: rgb(190, 190, 190);\n"
"background-color: rgb(251,252,255);")
        self.left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame.setObjectName("left_frame")
        self.btn_Add_Characteristic = QtWidgets.QPushButton(self.left_frame)
        self.btn_Add_Characteristic.setGeometry(QtCore.QRect(140, 30, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Add_Characteristic.setFont(font)
        self.btn_Add_Characteristic.setMouseTracking(True)
        self.btn_Add_Characteristic.setToolTip("")
        self.btn_Add_Characteristic.setToolTipDuration(3)
        self.btn_Add_Characteristic.setStatusTip("")
        self.btn_Add_Characteristic.setAccessibleName("")
        self.btn_Add_Characteristic.setStyleSheet("color: rgb(246,181,61);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_Add_Characteristic.setObjectName("btn_Add_Characteristic")
        self.btn_Add_Service = QtWidgets.QPushButton(self.left_frame)
        self.btn_Add_Service.setGeometry(QtCore.QRect(20, 30, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Add_Service.setFont(font)
        self.btn_Add_Service.setMouseTracking(False)
        self.btn_Add_Service.setToolTip("")
        self.btn_Add_Service.setToolTipDuration(3)
        self.btn_Add_Service.setStatusTip("")
        self.btn_Add_Service.setWhatsThis("")
        self.btn_Add_Service.setStyleSheet("color: rgb(39, 52, 105);\n"
"background-color: rgb(255, 255, 255);")
        self.btn_Add_Service.setCheckable(True)
        self.btn_Add_Service.setObjectName("btn_Add_Service")
        self.btn_Add_Descriptor = QtWidgets.QPushButton(self.left_frame)
        self.btn_Add_Descriptor.setGeometry(QtCore.QRect(370, 30, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_Add_Descriptor.setFont(font)
        self.btn_Add_Descriptor.setMouseTracking(True)
        self.btn_Add_Descriptor.setToolTip("")
        self.btn_Add_Descriptor.setToolTipDuration(3)
        self.btn_Add_Descriptor.setStatusTip("")
        self.btn_Add_Descriptor.setAccessibleName("")
        self.btn_Add_Descriptor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.btn_Add_Descriptor.setObjectName("btn_Add_Descriptor")
        self.label_5 = QtWidgets.QLabel(self.left_frame)
        self.label_5.setGeometry(QtCore.QRect(40, 0, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: 0px solid gray;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.left_frame)
        self.frame_19 = QtWidgets.QFrame(self.frame_7)
        self.frame_19.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_19.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"padding-top: 20px;\n"
"border-radius:15px;\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(45, 45, 45);\n"
"border: 1px solid gray;\n"
"border-color: rgb(190, 190, 190);")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.gatt_tree = QtWidgets.QTreeWidget(self.frame_19)
        self.gatt_tree.setGeometry(QtCore.QRect(10, 30, 511, 281))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.gatt_tree.setFont(font)
        self.gatt_tree.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"padding-top: 20px;\n"
"border-radius:15px;\n"
"\n"
"color: rgb(45, 45, 45);\n"
"border: 0px solid gray;\n"
"border-color: rgb(190, 190, 190);")
        self.gatt_tree.setObjectName("gatt_tree")
        self.gatt_tree.headerItem().setText(0, "1")
        self.gatt_tree.header().setVisible(False)
        self.label_9 = QtWidgets.QLabel(self.frame_19)
        self.label_9.setGeometry(QtCore.QRect(50, -20, 121, 43))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border: 0px solid gray;")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_12.addWidget(self.frame_19)
        self.frame_18 = QtWidgets.QFrame(self.frame_7)
        self.frame_18.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"padding-top: 20px;\n"
"border-radius:15px;\n"
"background-color: rgb(251,252,255);\n"
"color: rgb(45, 45, 45);\n"
"border: 1px solid gray;\n"
"border-color: rgb(190, 190, 190);")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.verticalLayout_12.addWidget(self.frame_18)
        self.verticalLayout_12.setStretch(1, 4)
        self.verticalLayout_12.setStretch(2, 4)
        self.horizontalLayout_15.addWidget(self.frame_7)
        self.frame_20 = QtWidgets.QFrame(self.frame_designer_left)
        self.frame_20.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_20.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(241,242,247);\n"
"")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_20)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMaximumSize(QtCore.QSize(999996, 16777215))
        self.scrollArea.setStyleSheet("border: 0px solid grey;\n"
"border-radius:15px;\n"
"background-color: rgb(241,242,247);\n"
"")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 784, 825))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_15.addWidget(self.frame_20)
        self.horizontalLayout_15.setStretch(0, 3)
        self.horizontalLayout_15.setStretch(1, 4)
        self.horizontalLayout_14.addWidget(self.frame_designer_left)
        self.horizontalLayout_9.addWidget(self.middle_frame)
        self.stackedWidget.addWidget(self.page_Gatt_Maker)
        self.horizontalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.horizontalLayout_3.setStretch(1, 1)
        self.gridLayout_3.addWidget(self.mainFrame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MAX32 Bluetooth Gatt Designer"))
        self.btnMenu.setText(_translate("MainWindow", "MAX32-BGD"))
        self.btnMenuGattMaker.setText(_translate("MainWindow", "      Designer"))
        self.btnauthor.setText(_translate("MainWindow", " Edwin Amaya"))
        self.btnRepo.setText(_translate("MainWindow", "Github"))
        self.btn_Add_Characteristic.setText(_translate("MainWindow", "Characteristic"))
        self.btn_Add_Service.setText(_translate("MainWindow", "Service"))
        self.btn_Add_Descriptor.setText(_translate("MainWindow", "Descriptor"))
        self.label_5.setText(_translate("MainWindow", "Custom Attributes"))
        self.label_9.setText(_translate("MainWindow", "Gatt Server"))
from slidingstackedwidget import SlidingStackedWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

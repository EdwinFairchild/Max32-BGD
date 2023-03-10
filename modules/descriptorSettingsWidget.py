# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'descriptorSettingsWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widgetDescriptor(object):
    def setupUi(self, widgetDescriptor):
        widgetDescriptor.setObjectName("widgetDescriptor")
        widgetDescriptor.resize(488, 232)
        widgetDescriptor.setStyleSheet("border: 0px solid gray;")
        self.widgetDescriptorSettings = QtWidgets.QWidget(widgetDescriptor)
        self.widgetDescriptorSettings.setGeometry(QtCore.QRect(0, 10, 481, 211))
        self.widgetDescriptorSettings.setMinimumSize(QtCore.QSize(0, 200))
        self.widgetDescriptorSettings.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:15px;\n"
"border: 1px solid gray;")
        self.widgetDescriptorSettings.setObjectName("widgetDescriptorSettings")
        self.btnToggle_permit_read_2 = QtWidgets.QPushButton(self.widgetDescriptorSettings)
        self.btnToggle_permit_read_2.setGeometry(QtCore.QRect(30, 90, 131, 30))
        self.btnToggle_permit_read_2.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnToggle_permit_read_2.setFont(font)
        self.btnToggle_permit_read_2.setStyleSheet("QPushButton{\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"border-radius:5px;\n"
"background-color: rgb(170,200,255);\n"
"color: rgb(30, 39, 73);\n"
"\n"
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
        self.btnToggle_permit_read_2.setCheckable(True)
        self.btnToggle_permit_read_2.setObjectName("btnToggle_permit_read_2")
        self.btnToggle_permit_read = QtWidgets.QPushButton(self.widgetDescriptorSettings)
        self.btnToggle_permit_read.setGeometry(QtCore.QRect(30, 130, 131, 30))
        self.btnToggle_permit_read.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnToggle_permit_read.setFont(font)
        self.btnToggle_permit_read.setStyleSheet("QPushButton{\n"
"text-align: center;\n"
"padding-left: 0px;\n"
"border-radius:5px;\n"
"background-color: rgb(170,200,255);\n"
"color: rgb(30, 39, 73);\n"
"\n"
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
        self.btnToggle_permit_read.setCheckable(True)
        self.btnToggle_permit_read.setObjectName("btnToggle_permit_read")
        self.checkBox_2 = AnimatedToggle(self.widgetDescriptorSettings)
        self.checkBox_2.setGeometry(QtCore.QRect(40, 30, 71, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setAutoFillBackground(False)
        self.checkBox_2.setStyleSheet("\n"
"QCheckBox {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(44, 52, 58);\n"
"border-radius:  5px;\n"
"padding-left: 5px;\n"
"}\n"
"")
        self.checkBox_2.setText("")
        self.checkBox_2.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_9 = QtWidgets.QLabel(self.widgetDescriptorSettings)
        self.label_9.setGeometry(QtCore.QRect(130, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(self.widgetDescriptorSettings)
        self.label.setGeometry(QtCore.QRect(330, 0, 151, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("text-align: center;\n"
"padding-left: 0px;\n"
"border-radius:5px;\n"
"background-color: rgb(255, 0, 0);\n"
"    color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(widgetDescriptor)
        QtCore.QMetaObject.connectSlotsByName(widgetDescriptor)

    def retranslateUi(self, widgetDescriptor):
        _translate = QtCore.QCoreApplication.translate
        widgetDescriptor.setWindowTitle(_translate("widgetDescriptor", "Form"))
        self.btnToggle_permit_read_2.setText(_translate("widgetDescriptor", "Write"))
        self.btnToggle_permit_read.setText(_translate("widgetDescriptor", "Read"))
        self.label_9.setText(_translate("widgetDescriptor", "Characteristic"))
        self.label.setText(_translate("widgetDescriptor", "Descriptor"))
from toggle import AnimatedToggle


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widgetDescriptor = QtWidgets.QWidget()
    ui = Ui_widgetDescriptor()
    ui.setupUi(widgetDescriptor)
    widgetDescriptor.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizeGrip
import sys
import platform



class Ui_GUIWindow(object):
    def setupUi(self, GUIWindow):
        GUIWindow.setObjectName("GUIWindow")
        GUIWindow.resize(800, 600)
        GUIWindow.setMaximumSize(QtCore.QSize(800, 600))
        GUIWindow.setStyleSheet("background-color: #211f21;\n"
"color: white;")
        self.centralwidget = QtWidgets.QWidget(GUIWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 781, 571))
        self.groupBox.setObjectName("groupBox")
        self.OSa = QtWidgets.QLabel(self.groupBox)
        self.OSa.setGeometry(QtCore.QRect(50, 30, 171, 111))
        self.OSa.setStyleSheet("font-size: 20px;")
        self.OSa.setObjectName("OSa")
        self.OSa_ = QtWidgets.QLabel(self.groupBox)
        self.OSa_.setGeometry(QtCore.QRect(340, 30, 81, 111))
        self.OSa_.setStyleSheet("font-size: 20px;")
        self.OSa_.setObjectName("OSa_")
        self.OSa_2 = QtWidgets.QLabel(self.groupBox)
        self.OSa_2.setGeometry(QtCore.QRect(330, 370, 91, 111))
        self.OSa_2.setStyleSheet("font-size: 20px;")
        self.OSa_2.setObjectName("OSa_2")
        self.OSa_3 = QtWidgets.QLabel(self.groupBox)
        self.OSa_3.setGeometry(QtCore.QRect(600, 30, 171, 111))
        self.OSa_3.setStyleSheet("font-size: 20px;")
        self.OSa_3.setObjectName("OSa_3")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(230, 60, 21, 281))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(500, 60, 21, 281))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.groupBox)
        self.line_3.setGeometry(QtCore.QRect(-10, 380, 801, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.OS_NAME = QtWidgets.QLabel(self.groupBox)
        self.OS_NAME.setGeometry(QtCore.QRect(80, 160, 81, 41))
        self.OS_NAME.setStyleSheet("font-size: 20px;")
        self.OS_NAME.setText(platform.system())
        self.OS_NAME.setObjectName("OS_NAME")
        self.OS_VERSION = QtWidgets.QLabel(self.groupBox)
        self.OS_VERSION.setGeometry(QtCore.QRect(360, 160, 21, 41))
        self.OS_VERSION.setStyleSheet("font-size: 20px;")
        self.OS_VERSION.setText(platform.release())
        self.OS_VERSION.setObjectName("OS_VERSION")
        self.MACHINE_NAME = QtWidgets.QLabel(self.groupBox)
        self.MACHINE_NAME.setGeometry(QtCore.QRect(610, 160, 61, 41))
        self.MACHINE_NAME.setStyleSheet("font-size: 20px;")
        self.MACHINE_NAME.setText(platform.machine())
        self.MACHINE_NAME.setObjectName("MACHINE_NAME")
        self.PROCESSOR_NAME = QtWidgets.QLabel(self.groupBox)
        self.PROCESSOR_NAME.setGeometry(QtCore.QRect(0, 480, 781, 41))
        self.PROCESSOR_NAME.setStyleSheet("font-size: 20px;")
        self.PROCESSOR_NAME.setText(platform.processor())
        self.PROCESSOR_NAME.setObjectName("PROCESSOR_NAME")
        GUIWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(GUIWindow)
        self.statusbar.setObjectName("statusbar")
        GUIWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GUIWindow)
        QtCore.QMetaObject.connectSlotsByName(GUIWindow)
        

        

    def retranslateUi(self, GUIWindow):
        _translate = QtCore.QCoreApplication.translate
        GUIWindow.setWindowTitle(_translate("GUIWindow", "Your computer information"))
        self.groupBox.setTitle(_translate("GUIWindow", "Information about your computer"))
        self.OSa.setText(_translate("GUIWindow", "Operating system"))
        self.OSa_.setText(_translate("GUIWindow", "Version"))
        self.OSa_2.setText(_translate("GUIWindow", "Processor"))
        self.OSa_3.setText(_translate("GUIWindow", "Machine"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUIWindow = QtWidgets.QMainWindow()
    ui = Ui_GUIWindow()
    ui.setupUi(GUIWindow)
    GUIWindow.show()
    sys.exit(app.exec_())

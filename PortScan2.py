# Form implementation generated from reading ui file 'PB_UI.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# This file handles the logic for the loading window, as well as adding a gif effect to represent loading progress


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QMovie


class Ui_SubScanningWindow(object):
    def setupUi(self, SubScanningWindow):
        SubScanningWindow.setObjectName("SubScanningWindow")
        SubScanningWindow.resize(550, 150)
        SubScanningWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(parent=SubScanningWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progress_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.progress_label.setGeometry(QtCore.QRect(200, 10, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progress_label.setFont(font)
        self.progress_label.setObjectName("progress_label")
        self.progress_label.setStyleSheet("color: black; background-color: white;")
        self.label_gif = QtWidgets.QLabel(self.centralwidget)
        self.gif = QMovie("Rolling.gif")
        self.label_gif.setGeometry(QtCore.QRect(200, 40, 131, 90))
        self.label_gif.setObjectName("self.label_gif")
        self.label_gif.setScaledContents(True)
        self.label_gif.setStyleSheet("background-color: transparent;")
        self.label_gif.setMovie(self.gif)
        self.gif.start()
        SubScanningWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SubScanningWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 555, 22))
        self.menubar.setObjectName("menubar")
        SubScanningWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SubScanningWindow)
        self.statusbar.setObjectName("statusbar")
        SubScanningWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SubScanningWindow)
        QtCore.QMetaObject.connectSlotsByName(SubScanningWindow)

    def retranslateUi(self, SubScanningWindow):
        _translate = QtCore.QCoreApplication.translate
        SubScanningWindow.setWindowTitle(_translate("SubScanningWindow", "MainWindow"))
        self.progress_label.setText(_translate("SubScanningWindow", "Scanning in Progress..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SubScanningWindow = QtWidgets.QMainWindow()
    ui = Ui_SubScanningWindow()
    ui.setupUi(SubScanningWindow)
    SubScanningWindow.show()
    sys.exit(app.exec())

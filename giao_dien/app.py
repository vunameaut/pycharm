# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1003, 722)
        self.btn_download = QtWidgets.QPushButton(parent=Dialog)
        self.btn_download.setGeometry(QtCore.QRect(630, 10, 121, 51))
        self.btn_download.setObjectName("btn_download")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.label.setObjectName("label")
        self.link_video = QtWidgets.QLineEdit(parent=Dialog)
        self.link_video.setGeometry(QtCore.QRect(120, 10, 471, 41))
        self.link_video.setObjectName("link_video")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.btn_download.clicked.connect(self.download_file)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_download.setText(_translate("Dialog", "Download"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Download</span></p></body></html>"))

    def download_file(self):
        get_link = self.link_video.text()
        mp4 = YouTube(get_link).streams.get_highest_resolution().download()

        clip = VideoClip(mp4)
        clip.close()

        QtWidgets.QMessageBox.information(self, "Thông báo", "Download thành công")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from yt_dlp import YoutubeDL
from moviepy.editor import VideoFileClip
import sys
import os

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
        try:
            get_link = self.link_video.text()


            if not get_link:
                QMessageBox.warning(None, "Lỗi", "Vui lòng nhập liên kết video!")
                return

            ydl_opts = {
                'format': 'best',
                'outtmpl': '%(title)s.%(ext)s'
            }

            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(get_link, download=True)
                video_title = info_dict.get('title', None)
                video_filename = ydl.prepare_filename(info_dict)

            # Đóng video clip để giải phóng tài nguyên (nếu cần)
            with VideoFileClip(video_filename) as clip:
                pass

            # Thông báo tải xuống thành công
            QMessageBox.information(None, "Thông báo", f"Tải xuống thành công: {video_filename}")
            self.link_video.setText("")


        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Đã xảy ra lỗi: {e}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

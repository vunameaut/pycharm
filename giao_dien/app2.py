import subprocess
import time
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
from yt_dlp import YoutubeDL
from moviepy.editor import VideoFileClip


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 300)  # Điều chỉnh kích thước Dialog cho vừa vặn hơn

        main_layout = QtWidgets.QVBoxLayout(Dialog)

        # Phần Download YouTube
        download_widget = QtWidgets.QWidget()
        download_layout = QtWidgets.QHBoxLayout(download_widget)

        self.label = QtWidgets.QLabel("Nhập link video:", parent=download_widget)
        download_layout.addWidget(self.label)

        self.txt_linkvideo = QtWidgets.QLineEdit(parent=download_widget)
        download_layout.addWidget(self.txt_linkvideo)

        self.btn_download = QtWidgets.QPushButton("Download", parent=download_widget)
        download_layout.addWidget(self.btn_download)

        main_layout.addWidget(download_widget)

        # Phần Tắt máy
        self.TATMAY = QtWidgets.QWidget()
        self.TATMAY.setObjectName("TATMAY")
        tatmay_layout = QtWidgets.QVBoxLayout(self.TATMAY)

        # Layout ngang cho các QSpinBox
        spinbox_layout = QtWidgets.QHBoxLayout()
        self.in_gio = QtWidgets.QSpinBox(parent=self.TATMAY)
        self.in_gio.setMinimum(0)
        self.in_gio.setMaximum(23)
        spinbox_layout.addWidget(self.in_gio)

        self.label_2 = QtWidgets.QLabel("giờ", parent=self.TATMAY)
        spinbox_layout.addWidget(self.label_2)

        self.in_phut = QtWidgets.QSpinBox(parent=self.TATMAY)
        self.in_phut.setMinimum(0)
        self.in_phut.setMaximum(59)
        spinbox_layout.addWidget(self.in_phut)

        self.label_3 = QtWidgets.QLabel("phút", parent=self.TATMAY)
        spinbox_layout.addWidget(self.label_3)

        self.in_giay = QtWidgets.QSpinBox(parent=self.TATMAY)
        self.in_giay.setMinimum(0)
        self.in_giay.setMaximum(59)
        spinbox_layout.addWidget(self.in_giay)

        self.label_4 = QtWidgets.QLabel("giây", parent=self.TATMAY)
        spinbox_layout.addWidget(self.label_4)

        tatmay_layout.addLayout(spinbox_layout)

        # Layout ngang cho các nút bấm (Thêm khoảng cách giữa các nút)
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        self.btn_sleep = QtWidgets.QPushButton("Sleep", parent=self.TATMAY)
        button_layout.addWidget(self.btn_sleep)
        button_layout.addStretch()
        self.btn_tat = QtWidgets.QPushButton("Shut Down", parent=self.TATMAY)
        button_layout.addWidget(self.btn_tat)
        button_layout.addStretch()
        self.btn_restart = QtWidgets.QPushButton("Restart", parent=self.TATMAY)
        button_layout.addWidget(self.btn_restart)
        button_layout.addStretch()
        tatmay_layout.addLayout(button_layout)

        self.btn_huy = QtWidgets.QPushButton("Hủy", parent=self.TATMAY)
        button_layout.addWidget(self.btn_huy)

        main_layout.addWidget(self.TATMAY)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btn_download.clicked.connect(self.start_download_thread)
        self.btn_tat.clicked.connect(self.tat_may)
        self.btn_restart.clicked.connect(self.khoi_dong_lai)
        self.btn_sleep.clicked.connect(self.sleep)
        self.btn_huy.clicked.connect(self.huy)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.TATMAY.setToolTip(_translate("Dialog", "<html><head/><body><p>border: 2px solid black;</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "giờ"))
        self.label_3.setText(_translate("Dialog", "phút"))
        self.label_4.setText(_translate("Dialog", "giây"))
        self.btn_sleep.setText(_translate("Dialog", "Sleep"))
        self.btn_tat.setText(_translate("Dialog", "Shut Down"))
        self.btn_restart.setText(_translate("Dialog", "Restart"))
        self.label.setText(_translate("Dialog", "Nhập link video:"))
        self.btn_download.setText(_translate("Dialog", "Download"))
        self.btn_huy.setText(_translate("Dialog", "Hủy"))

    def start_download_thread(self):
        self.download_thread = DownloadThread(self.txt_linkvideo.text())
        self.download_thread.download_complete.connect(self.on_download_complete)
        self.download_thread.start()

    def on_download_complete(self, result):
        if result['success']:
            QMessageBox.information(None, "Thông báo", f"Tải xuống thành công: {result['filename']}")
        else:
            QMessageBox.critical(None, "Lỗi", f"Đã xảy ra lỗi: {result['error']}")
        self.txt_linkvideo.setText("")

    def tat_may(self):
        self.shutdown_restart_sleep('shutdown')

    def khoi_dong_lai(self):
        self.shutdown_restart_sleep('restart')

    def sleep(self):
        self.shutdown_restart_sleep('sleep')

    def shutdown_restart_sleep(self, action):
        try:
            gio = self.in_gio.value()
            phut = self.in_phut.value()
            giay = self.in_giay.value()
            tong_giay = gio * 3600 + phut * 60 + giay

            if tong_giay <= 0:
                QMessageBox.warning(None, "Lỗi", "Thời gian phải lớn hơn 0!")
                return

            if sys.platform.startswith('win'):
                if action == 'shutdown':
                    subprocess.run(["shutdown", "/s", "/t", str(tong_giay)])
                elif action == 'restart':
                    subprocess.run(["shutdown", "/r", "/t", str(tong_giay)])
                elif action == 'sleep':
                    time.sleep(tong_giay)
                    subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0,1,0"])

            QMessageBox.information(None, "Thông báo", f"Máy tính sẽ {action} sau {gio} giờ {phut} phút {giay} giây.")

        except Exception as e:
            QMessageBox.critical(None, "Lỗi", f"Đã xảy ra lỗi: {e}")

    def huy(self):
        if sys.platform.startswith('win'):
            subprocess.run(["shutdown", "/a"])


class DownloadThread(QtCore.QThread):
    download_complete = QtCore.pyqtSignal(dict)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        result = {'success': False, 'filename': '', 'error': ''}
        try:
            if not self.url:
                result['error'] = "Vui lòng nhập liên kết video!"
                self.download_complete.emit(result)
                return

            ydl_opts = {
                'format': 'best',
                'outtmpl': '%(title)s.%(ext)s'
            }

            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(self.url, download=True)
                video_filename = ydl.prepare_filename(info_dict)

            # Đóng video clip để giải phóng tài nguyên (nếu cần)
            with VideoFileClip(video_filename) as clip:
                pass

            result['success'] = True
            result['filename'] = video_filename

        except Exception as e:
            result['error'] = str(e)

        self.download_complete.emit(result)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())

import time
import pyautogui
import random
import keyboard
import pyperclip
import pygetwindow as gw

# Danh sách các tin nhắn
messages = [
    "halo", "❤️", "hi", "how are you?", "what's up?",
    "good morning", "good night", "have a nice day",
    "see you", "bye"
]

# Tên cửa sổ của ứng dụng mục tiêu
target_window_title = "facebook"

# Lấy cửa sổ mục tiêu
windows = gw.getWindowsWithTitle(target_window_title)
if not windows:
    print(f"Không tìm thấy cửa sổ với tiêu đề '{facebook}'")
else:
    target_window = windows[0]
    target_window.activate()  # Kích hoạt cửa sổ mục tiêu

    time.sleep(3)  # Đợi 3 giây trước khi bắt đầu

    for i in range(100):
        if keyboard.is_pressed('esc'):  # Kiểm tra nếu phím 'esc' được nhấn
            print("Dừng lại bởi vì phím 'Esc' đã được nhấn")
            break
        message = random.choice(messages)  # Chọn ngẫu nhiên một tin nhắn từ danh sách
        pyperclip.copy(message)  # Sao chép tin nhắn vào clipboard
        pyautogui.hotkey("ctrl", "v")  # Dán nội dung từ clipboard
        pyautogui.press("enter")  # Nhấn phím Enter để gửi tin nhắn
        time.sleep(0.5)  # Khoảng dừng ngắn giữa các tin nhắn

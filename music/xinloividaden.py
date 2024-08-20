import time

lyrics = [
    "Để một ngày sống đến lúc bạc đầu",
    "Nhưng nếu quá lâu",
    "Em là người khổ đau",
    "Anh nghĩ anh nên rời xa em",
    "Để biết em hạnh phúc thế nào",
    "Không phải ưu tư và cô đơn",
    "Khóc dưới mưa chiều ướt áo",
    "Anh biết em chẳng quan tâm thì giờ",
    "Anh biết em vẫn thương anh và chờ",
    "Nhưng nhìn em đứng giữa trời mùa đông",
    "Anh ghét bản thân mình"
]


sleep_times = [1, 1.5, 2, 1.2, 2.5, 1.8, 3, 2, 2, 2]


for line, sleep_time in zip(lyrics, sleep_times):
    print(line)
    time.sleep(sleep_time)
import requests

def get_ip_location(ip_address):
    """
    Hàm này lấy vị trí của một địa chỉ IP bằng cách sử dụng API ipinfo.io.
    Nó trả về một từ điển chứa thông tin vị trí, hoặc None nếu có lỗi.
    """

    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()  

        data = response.json()

        # Trích xuất thông tin vị trí quan trọng
        location_data = {
            "ip": data["ip"],
            "city": data.get("city"),
            "region": data.get("region"),
            "country": data.get("country"),
            "loc": data.get("loc"),  # Vĩ độ và kinh độ
            "org": data.get("org"),  # Tổ chức sở hữu IP
        }

        return location_data

    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi lấy thông tin vị trí: {e}")
        return None

# Ví dụ sử dụng
ip_address = input("Nhập vào địa chỉ ip cần tra: ")
location = get_ip_location(ip_address)

if location:
    print(f"Địa chỉ IP: {location['ip']}")
    print(f"Thành phố: {location['city']}")
    print(f"Vùng: {location['region']}")
    print(f"Quốc gia: {location['country']}")
    print(f"Tọa độ: {location['loc']}")
    print(f"Tổ chức: {location['org']}")
else:
    print("Không thể lấy thông tin vị trí cho địa chỉ IP này.")
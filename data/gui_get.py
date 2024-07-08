import requests
import socket

def send_get_request(ip_address, port=80, path="/"):
    """Gửi yêu cầu GET đến địa chỉ IP và cổng cụ thể, trả về phản hồi."""
    url = f"http://{ip_address}:{port}{path}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi gửi yêu cầu GET đến {url}: {e}")
        return None

def get_ip_address(url):
    """Lấy địa chỉ IP từ URL."""
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        print(f"Không thể phân giải địa chỉ IP cho {url}")
        return None


url = "eaut.edu.vn"  # Thay bằng URL thực tế
port = 80  # Cổng mặc định (có thể thay đổi nếu cần)
path = "/SinhVien"  # Đường dẫn tùy chọn

ip_address = get_ip_address(url)
if ip_address:
    response = send_get_request(ip_address, port, path)
    if response:
        print(f"Mã trạng thái: {response.status_code}")
        print(f"Nội dung phản hồi (đầu): {response.text[:]}...")
import requests
import subprocess
import os
import time

def get_ip_from_service(url):
    """Lấy địa chỉ IP từ một dịch vụ web."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("ip")
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi lấy địa chỉ IP từ {url}: {e}")
        return None

def get_multiple_public_ips():
    """
    Lấy địa chỉ IP công cộng từ nhiều dịch vụ web.
    """
    services = [
        "https://api.ipify.org?format=json"
    ]

    ips = {}
    for service in services:
        ip = get_ip_from_service(service)
        if ip:
            ips[service] = ip

    return ips

def disconnect_vpn():
    """Ngắt kết nối VPN (ví dụ sử dụng OpenVPN)."""
    try:
        result = subprocess.run(["tasklist", "/FI", "IMAGENAME eq openvpn.exe"], capture_output=True, text=True)
        if "openvpn.exe" in result.stdout:
            subprocess.run(["taskkill", "/F", "/IM", "openvpn.exe"])
            print("Đã ngắt kết nối VPN.")
        else:
            print("Không có kết nối VPN để ngắt.")
    except Exception as e:
        print(f"Lỗi khi ngắt kết nối VPN: {e}")

def connect_vpn():
    """Kết nối VPN (ví dụ sử dụng OpenVPN)."""
    config_path = "C:\\Users\\namta\\OpenVPN\\config\\vpn\\vpn.ovpn"
    openvpn_executable = "C:\\Program Files\\OpenVPN\\bin\\openvpn.exe"
    if not os.path.exists(config_path):
        print(f"Lỗi: Không tìm thấy tệp cấu hình OpenVPN '{config_path}'")
        return None
    try:
        log_file = "C:\\path\\to\\your\\openvpn_log.txt"
        vpn_process = subprocess.Popen([openvpn_executable, "--config", config_path, "--log", log_file], shell=True)
        print("Đã kết nối VPN.")
        return vpn_process
    except Exception as e:
        print(f"Lỗi khi kết nối VPN: {e}")
        return None

def send_get_request_with_vpn(url):
    """Gửi yêu cầu GET đến URL sử dụng VPN và in địa chỉ IP công cộng và phản hồi máy chủ."""
    vpn_process = connect_vpn()
    if not vpn_process:
        print("Không thể kết nối VPN, dừng yêu cầu GET.")
        return None

    try:
        ips_before = get_multiple_public_ips()
        if ips_before:
            for service, ip in ips_before.items():
                print(f"Địa chỉ IP từ {service} trước khi gửi yêu cầu: {ip}")

        response = requests.get(url)
        response.raise_for_status()

        # In ra thông tin phản hồi
        print(f"Mã trạng thái HTTP: {response.status_code}")

        ips_after = get_multiple_public_ips()
        if ips_after:
            for service, ip in ips_after.items():
                print(f"Địa chỉ IP từ {service} sau khi gửi yêu cầu: {ip}")

        return response
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi gửi yêu cầu GET: {e}")
        return None
    finally:
        # Đảm bảo kết nối VPN được ngắt
        vpn_process.terminate()
        disconnect_vpn()

# Vòng lặp liên tục
url = "http://sinhvien.eaut.edu.vn/"

try:
    while True:
        send_get_request_with_vpn(url)
except KeyboardInterrupt:
    print("Dừng vòng lặp theo yêu cầu của người dùng.")
    disconnect_vpn()

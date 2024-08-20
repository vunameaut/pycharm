import browser_cookie3

# Lấy cookie từ trình duyệt Chrome
cj = browser_cookie3.chrome()

# Lấy cookie đầu tiên từ danh sách cookie
for cookie in cj:
    print(f'Tên cookie: {cookie.name}')
    print(f'Giá trị cookie: {cookie.value}')
    print(f'Domain của cookie: {cookie.domain}')
    print(f'Đường dẫn của cookie: {cookie.path}')
    print(f'Thời gian hết hạn của cookie: {cookie.expires}')
    print(f'Cookie có cờ bảo mật Secure: {cookie.secure}')
    print(f'Cookie có cờ HttpOnly: {cookie.has_nonstandard_attr("HttpOnly")}')
    break

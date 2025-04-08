import socket

HOST = '127.0.0.1'
PORT = 8080

# ایجاد سوکت TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
    client_sock.connect((HOST, PORT))
    print("اتصال با سرور برقرار شد.")

    # ارسال پیام به سرور
    message = "سلام سرور!"
    client_sock.sendall(message.encode())

    # دریافت پاسخ از سرور
    data = client_sock.recv(1024)
    print("پاسخ سرور:", data.decode())

    # پایان ارتباط (خود `with` خودش `close()` می‌کنه)
    print("اتصال بسته شد.")

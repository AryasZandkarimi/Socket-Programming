import socket

HOST = '0.0.0.0'  # گوش دادن به همه‌ی IP ها
PORT = 8080

# ایجاد سوکت TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
    server_sock.bind((HOST, PORT))
    server_sock.listen(1)
    print(f"سرور در حال گوش دادن روی پورت {PORT} ...")

    conn, addr = server_sock.accept()
    with conn:
        print(f"اتصال جدید از {addr[0]}:{addr[1]}")

        # دریافت پیام از کلاینت
        data = conn.recv(1024)
        if data:
            print("پیام دریافتی از کلاینت:", data.decode())

            # ارسال پاسخ به کلاینت
            response = "سلام کلاینت!"
            conn.sendall(response.encode())

        # پایان ارتباط
        print("در حال بستن اتصال با کلاینت...")

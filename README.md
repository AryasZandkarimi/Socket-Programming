# 🖧 Simple TCP Client-Server in Python

This project demonstrates a basic TCP client-server communication in Python.  
It mimics a classic socket interaction where:

- The **server** listens for incoming client connections on a specific port.
- The **client** connects to the server, sends a message ("سلام سرور!" – "Hello Server!").
- The server responds with a reply ("سلام کلاینت!" – "Hello Client!").
- Both sides close the connection gracefully.

---

## Features

- Simple and readable socket code using Python’s built-in `socket` module.
- UTF-8 encoded messages (can support Persian/Unicode messages).
- Clean connection shutdown using Python’s `with` context (auto-closes sockets).
- Minimal error handling for easy understanding.
- Suitable for beginners learning about networking in Python.

---

##  Files

| File        | Description                                      |
|-------------|--------------------------------------------------|
| `server.py` | Starts a TCP server that listens for one client  |
| `client.py` | Connects to the server and exchanges messages    |

---

## How It Works

### `server.py`

1. Creates a TCP socket using `socket.AF_INET` and `socket.SOCK_STREAM`.
2. Binds the socket to host `0.0.0.0` and port `8080` – this means it listens on all network interfaces.
3. Calls `listen()` to wait for incoming connections.
4. Accepts a client connection using `accept()`.
5. Receives a message from the client with `recv()`.
6. Sends a reply back to the client with `sendall()`.
7. Closes the connection cleanly (thanks to the `with` block).

### `client.py`

1. Creates a TCP socket.
2. Connects to `127.0.0.1:8080` (local server).
3. Sends the message `"سلام سرور!"` (Hello Server).
4. Waits for a response from the server and prints it.
5. Automatically closes the connection.

---

## How to Run

Make sure you have **Python 3** installed.

1. **Run the Server:**

2. **Run the Client:**

```bash
python3 server.py

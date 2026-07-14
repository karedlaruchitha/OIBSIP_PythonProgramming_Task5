import socket
import threading
import tkinter as tk

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode()
            chat_box.insert(tk.END, msg + "\n")
        except:
            break

def send_message():
    msg = entry.get()
    client.send(msg.encode())
    entry.delete(0, tk.END)

# GUI setup
window = tk.Tk()
window.title("Chat App")

chat_box = tk.Text(window)
chat_box.pack()

entry = tk.Entry(window)
entry.pack()

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

thread = threading.Thread(target=receive)
thread.start()

window.mainloop()
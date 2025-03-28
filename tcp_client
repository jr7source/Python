import socket
import threading
import sys
import time

# Function to handle receiving messages from the server
def receive(sock, stop_event):
    while not stop_event.is_set():
        try:
            # Wait for incoming data (max 32 bytes at a time)
            data = sock.recv(32)
            if not data:
                print("Server closed the connection.")
                stop_event.set()
                break
            print("[Server]:", data.decode("utf-8"))
        except:
            print("Disconnected from the server.")
            stop_event.set()
            break

# Function to repeatedly send a message every 1 ms
def send_periodic(sock, stop_event, message_container):
    while not stop_event.is_set():
        try:
            message = message_container.get("message", "")
            if message:
                sock.sendall(message.encode())  # Send the current message
            time.sleep(0.001)  # Sleep for 1 ms before sending again
        except:
            print("Error while sending message.")
            stop_event.set()
            break

# --- Main Program Starts Here ---

# Ask user where to connect
host = input("Enter server IP/hostname: ")
port = int(input("Enter port number: "))

# Try to connect to the server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print("Connected to server.")
except:
    print("❌ Could not connect to the server.")
    input("Press Enter to quit...")
    sys.exit(0)

# Create a flag to signal threads to stop
stop_event = threading.Event()

# Shared dictionary to hold the current message
# Threads will read from and write to this
message_container = {"message": ""}

# Start thread to handle incoming messages from server
receiveThread = threading.Thread(target=receive, args=(sock, stop_event))
receiveThread.start()

# Start thread to send messages every millisecond
sendThread = threading.Thread(target=send_periodic, args=(sock, stop_event, message_container))
sendThread.start()

# Main thread handles user input
try:
    while True:
        user_input = input("Type a message to send every 1ms (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            stop_event.set()
            break
        # Update message being sent repeatedly
        message_container["message"] = user_input
except KeyboardInterrupt:
    print("\nInterrupted. Exiting...")
    stop_event.set()
finally:
    # Clean up and exit
    sock.close()
    receiveThread.join()
    sendThread.join()
    sys.exit(0)

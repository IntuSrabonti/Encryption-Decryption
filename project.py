import base64
from tkinter import *
from tkinter import messagebox

# Function to encrypt a message using base64 encoding
def encrypt_message():
    message = message_entry.get()
    if message == "":
        messagebox.showwarning("Input Error", "Please enter a message to encrypt.")
        return
    # Encrypt the message
    encrypted_message = base64.b64encode(message.encode()).decode()
    result_label.config(text=f"Encrypted Message: {encrypted_message}")

# Function to decrypt a message using base64 decoding
def decrypt_message():
    message = message_entry.get()
    if message == "":
        messagebox.showwarning("Input Error", "Please enter a message to decrypt.")
        return
    try:
        # Decrypt the message
        decrypted_message = base64.b64decode(message.encode()).decode()
        result_label.config(text=f"Decrypted Message: {decrypted_message}")
    except Exception as e:
        messagebox.showerror("Decryption Error", "Invalid encrypted message format.")

# Set up the main window
root = Tk()
root.title("Encryption/Decryption with Base64")
root.geometry("500x300")
root.config(bg="#f0f0f0")

# Create widgets
header_label = Label(root, text="Base64 Encryption/Decryption", font=("Arial", 18), bg="#f0f0f0")
message_label = Label(root, text="Enter message to encrypt or decrypt:", font=("Arial", 12), bg="#f0f0f0")
message_entry = Entry(root, width=40, font=("Arial", 12))
encrypt_button = Button(root, text="Encrypt", font=("Arial", 12), width=15, bg="green", command=encrypt_message)
decrypt_button = Button(root, text="Decrypt", font=("Arial", 12), width=15, bg="blue", command=decrypt_message)
result_label = Label(root, text="Result will appear here", font=("Arial", 12), bg="#f0f0f0", width=50)

# Layout the widgets
header_label.pack(pady=10)
message_label.pack(pady=5)
message_entry.pack(pady=5)
encrypt_button.pack(pady=10)
decrypt_button.pack(pady=10)
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
